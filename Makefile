all:
	python3 setup.py build_ext --inplace
	python3 principal.py
clean:
	rm -rf build *.so *.pyc *.c
	rm *.csv