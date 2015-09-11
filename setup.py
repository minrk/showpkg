#  Copyright (c) Min RK.
#  Distributed under the terms of the 2-clause BSD License.

from __future__ import print_function

import sys

if 'bdist_wheel' in sys.argv:
    import setuptools

from distutils.core import setup

with open('showpkg.py') as f:
    for line in f:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=', 1)[1])
            break

setup_args = dict(
    name = "showpkg",
    version = __version__,
    py_modules = ["showpkg"],
    author = "Min Ragan-Kelley",
    author_email = "benjaminrk@gmail.com",
    url = 'http://github.com/minrk/showpkg',
    description = "Show packages",
    long_description = "",
    license = "BSD",
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

setup(**setup_args)

