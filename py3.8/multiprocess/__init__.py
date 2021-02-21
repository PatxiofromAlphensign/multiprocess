#
# Package analogous to 'threading.py' but using processes
#
# multiprocessing/__init__.py
#
# This package is intended to duplicate the functionality (and much of
# the API) of threading.py but uses processes instead of threads.  A
# subpackage 'multiprocessing.dummy' has the same API but is a simple
# wrapper for 'threading'.
#
# Copyright (c) 2006-2008, R Oudkerk
# Licensed to PSF under a Contributor Agreement.
#

import sys,os
import importlib

from . import context, process, util

[importlib.__import__(name.split(".")[0]) for name in os.listdir(".") if name.endswith("py") ]

__version__ = '0.70.12.dev0'


