#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# Setup script for aplora

__version__ = "$Revision$"[11:-2]
# $Source$

from distutils.core import setup
import textwrap

DESCRIPTION = """
ll-aplora is script that can be used with Apaches piped logging facility to
log request to an Oracle database.
"""

CLASSIFIERS="""
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: Python License (CNRI Python License)
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Internet :: WWW/HTTP
Topic :: System :: Logging
"""

KEYWORDS = """
Apache
logging
Oracle
database
piped logging
request
HTTP
"""

DESCRIPTION = "\n".join(textwrap.wrap(DESCRIPTION.strip(), width=64, replace_whitespace=True))

setup(
	name="ll-aplora",
	version="0.2",
	description="Logging Apache requests to an Oracle database",
	long_description=DESCRIPTION,
	author=u"Walter Dörwald",
	author_email="walter@livinglogic.de",
	url="http://www.livinglogic.de/Python/aplora/",
	download_url="http://www.livinglogic.de/Python/aplora/Download.html",
	license="Python",
	classifiers=CLASSIFIERS.strip().splitlines(),
	keywords=",".join(KEYWORDS.strip().splitlines()),
	scripts=["aplora.py" ],
	data_files=[(".", "aplora.sql")]
)
