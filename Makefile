# List of pseudo targets
.PHONY: install dist livinglogic

install:
	python$(PYVERSION) setup.py install

dist:
	rm -rf dist/*
	python$(PYVERSION) setup.py sdist --formats=bztar,gztar
	python$(PYVERSION) -mll.scripts.ucp -v -uftp -gftp dist/*.tar.gz dist/*.tar.bz2 ssh://root@isar.livinglogic.de/~ftp/pub/livinglogic/aplora/

livinglogic:
	python$(PYVERSION) setup.py sdist --formats=bztar,gztar
	python$(PYVERSION) -mll.scripts.ucp -v dist/*.tar.gz dist/*.tar.bz2 ssh://intranet@intranet.livinglogic.de/~/documentroot/intranet.livinglogic.de/python-downloads/
