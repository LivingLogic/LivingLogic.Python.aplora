#!/usr/local/bin/python2.3
# -*- coding: iso-8859-1 -*-

## Copyright 2004/2005 by LivingLogic AG, Bayreuth/Germany.
## Copyright 2004/2005 by Walter Dörwald
##
## All Rights Reserved
##
## Permission to use, copy, modify, and distribute this software and its documentation
## for any purpose and without fee is hereby granted, provided that the above copyright
## notice appears in all copies and that both that copyright notice and this permission
## notice appear in supporting documentation, and that the name of LivingLogic AG or
## the author not be used in advertising or publicity pertaining to distribution of the
## software without specific, written prior permission.
##
## LIVINGLOGIC AG AND THE AUTHOR DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
## INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL
## LIVINGLOGIC AG OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL
## DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
## IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
## IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
This script can be used with Apache's piped logging to log HTTP request
to an Oracle database.
"""

__version__ = "$Revision$"[11:-1]


import os, datetime, cgi, Cookie, urlparse


class Logger(object):
	def __init__(self, oracle, connect, procname):
		os.environ["ORACLE_HOME"] = oracle
		import cx_Oracle
		self.cx_Oracle = cx_Oracle
		db = cx_Oracle.connect(connect)
		self.c = db.cursor()
		self.connect = connect
		self.procname = procname

	def findcoid(self, path, query):
		# Find Content-Object-ID in URL
		coid = None
		pos1 = path.find("_id_")
		if pos1 >= 0:
			pos2 = path.find("_", pos1+4)
			if pos2 >= 0:
				coid = path[pos1+4:pos2]
	
		# Retry with a query parameter
		if coid is None and query:
			query = query[1:] # drop the ?
			query = cgi.parse_qs(query)
			if "id" in query:
				coid = query["id"][0]
		return coid
	
	def findsession(self, sessionin, sessionout, path):
		if sessionout and sessionout != "-":
			cookie = Cookie.SimpleCookie()
			cookie.load(sessionout)
			if "JSESSIONID" in cookie:
				return cookie["JSESSIONID"].value
		(scheme, server, path, params, query, frag) = urlparse.urlparse(path)
		if params.startswith("jsessionid="):
			return params[11:]
		if sessionin and sessionin != "-":
			return sessionin
		return None

	def run(self, stream):
		while True:
			line = stream.readline()
			fields = [field.decode("string-escape").encode("latin-1") for field in line.rstrip("\n").split("\t")]

			field = iter(fields)
			instance = field.next()
			try:
				reqstart = int(field.next())
			except ValueError:
				reqstart = None
			else:
				reqstart = datetime.datetime.fromtimestamp(reqstart)
			reqtime = 1e-6*float(field.next())
			client = field.next()
			useragent = field.next()
			path = field.next()
			query = field.next()
			method = field.next()
			status = int(field.next())
			bytesin = int(field.next())
			bytesout = int(field.next())
			bytesbodyout = int(field.next())
			referer = field.next()
			contenttype = field.next()
			sessionin = field.next()
			sessionout = field.next()
	
			reqstart = self.cx_Oracle.Timestamp(reqstart.year, reqstart.month, reqstart.day, reqstart.hour, reqstart.minute, reqstart.second)
	
			(mimetype, options) = cgi.parse_header(contenttype)
			charset = options.get("charset", None)
	
			data = [
				reqstart,
				reqtime,
				instance,
				client,
				useragent,
				path+query,
				method,
				status,
				bytesin,
				bytesout,
				bytesbodyout,
				None, #req.content_encoding,
				mimetype,
				charset,
				referer,
				self.findsession(sessionin, sessionout, path),
				self.findcoid(path, query),
			]
			self.c.callproc(self.procname, data)


if __name__ == "__main__":
	import sys, optparse
	p = optparse.OptionParser(usage="usage: %prog [options]", version="%%prog %s" % __version__)
	p.add_option("-o", "--oracle", dest="oracle", help="Value for ORACLE_HOME", default="/oracle/Client")
	p.add_option("-c", "--connect", dest="connect", help="Oracle connect string", default=None)
	p.add_option("-p", "--procname", dest="procname", help="Name of insert procedure", default="log_insert")
	(options, args) = p.parse_args()
	logger = Logger(oracle=options.oracle, connect=options.connect, procname=options.procname)
	logger.run(sys.stdin)
