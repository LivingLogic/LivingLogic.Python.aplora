# $Header$

# List of pseudo targets
.PHONY: all clean dist

# Output directory
OUTPUTDIR=$(HOME)/pythonroot

all:
	python$(PYVERSION) setup.py install --install-lib $(OUTPUTDIR)

clean:
	python$(PYVERSION) setup.py clean

install:
	python$(PYVERSION) setup.py install

dist:
	python$(PYVERSION) `which doc2txt.py` --title "History" NEWS.xml NEWS
	python$(PYVERSION) `which doc2txt.py` --title "Requirements, installation and configuration" INSTALL.xml INSTALL
	python$(PYVERSION) setup.py sdist --formats=bztar,gztar
	rm NEWS INSTALL