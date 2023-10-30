setup:
	pip install -r requirements.txt

build:
	python main.py

dist: build
	rm -rf dist
	mkdir dist
	cp -R assets imgs js css *.html projects dist/
