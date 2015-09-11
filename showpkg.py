#!/usr/bin/env python
"""Show package info

Shows location and version info from one or more packages.
"""

# Copyright (c) Min RK.
# Distributed under the terms of the 2-clause BSD License.

from __future__ import print_function

import sys

__version__ = '0.0.1'

def pkg_info(name):
    """Get package info"""
    pkg = __import__(name)
    info = {}
    info['__file__'] = pkg.__file__
    for key in dir(pkg):
        if 'version' not in key.lower():
            continue
        attr = getattr(pkg, key)
        if callable(attr):
            try:
                value = attr()
            except Exception as e:
                continue # ignore?
            key = key + '()'
        else:
            value = str(attr)
        info[key] = value
    return info


def show(name):
    """Show info about a package (location, version)"""
    try:
        info = pkg_info(name)
    except ImportError:
        print('{name}: Not Found'.format(name=name), file=sys.stderr)
        return
    print(name + ':')
    for key in sorted(info, key=lambda x: x.replace('_', ' ')):
        print("  {key} = {value}".format(key=key, value=info[key]))

def main():
    for pkg in sys.argv[1:]:
        show(pkg)

if __name__ == '__main__':
    main()