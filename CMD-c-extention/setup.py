from distutils.core import setup, Extension
setup(name='supermodule', version='1.0',  \
      ext_modules=[Extension('supermodule', ['main.c'])])
