# List of pseudo targets
.PHONY: install dist windist

install:
	python$(PYVERSION) setup.py install

dist:
	python$(PYVERSION) setup.py sdist --formats=bztar,gztar

windist:
	python$(PYVERSION) setup.py sdist --formats=zip
