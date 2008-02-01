Requirements
============

To use this script you need the following software packages:

	1.	Python_ (any version supported by cx_Oracle should do);
	2.	Apache_ (2.0.46 or later, although it's possible to get it to work with
		Apache 1.3 by removing a few of the fields);
	3.	cx_Oracle_ (4.3 or later);

	.. _Python: http://www.python.org/
	.. _Apache: http://httpd.apache.org/
	.. _cx_Oracle: http://www.python.net/crew/atuining/cx_Oracle/


Installation
============

distutils is used for installation, so it's rather simple. Execute the following
command::

	$ python setup.py install

This will copy aplora.py to ``/usr/local/bin``. If you want to install the
script somewhere else you can use the :option:`--install-scripts` option.

There is no Windows binary.

To create the database table and the stored procedure use ``aplora.sql``.

If you have difficulties installing this software, send a problem report
to Walter Dörwald (walter@livinglogic.de).


Configuration
=============

First you have to define the logging format to be used by aplora. Put
the following two lines into your ``httpd.conf``::

	LogFormat "%v\t%{%s}t\t%D\t%a\t%{User-Agent}i\t%U\t%q\t%m\t%>s\t0\t0\t%B\t%{Referer}i\t%{Content-Type}o\t%{JSESSIONID}C\t%{Set-Cookie}o" aplora
	CustomLog "|/usr/local/bin/aplora.py -o ORACLE_HOME -c user/pass@db -p log_insert" aplora

Replace ``ORACLE_HOME`` with the content of your ``ORACLE_HOME`` environment
variable (e.g. ``/oracle/Client``) and ``user/pass@db`` with the appropriate
connect string. The option :option:`-p` can be used to specify a different
insert procedure.

Note that this will only work for virtual hosts, if they don't have a
``CustomLog`` or ``ErrorLog`` directive. In this case you have to add the
``CustomLog`` specification from above to each virtual host section. This means
that you will have more aplora jobs running and more database connections will
be consumed.
