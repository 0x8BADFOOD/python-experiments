
## Sample of c extention for python

Build so:

    gcc -shared -o supermodule.so main.c -framework Python

Install:

    python setup.py install

Usage:

    ./sample_usage.py
