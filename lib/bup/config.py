"""bup configuration information"""

# Copyright (C) 2015 Rob Browning
#
# This code is covered under the terms of the GNU Library General
# Public License as described in the bup LICENSE file.

from inspect import getfile
from os import path
import errno

def _chomp(s):
    return s[:-1] if s.endswith('\n') else s

configdir = path.join(path.dirname(getfile(_chomp)), 'config')

def read_mandir(configdir=configdir):
    try:
      f = open(path.join(configdir, 'mandir'), 'r')
    except IOError as ex:
        if ex.errno == errno.ENOENT:
            return None
        raise ex
    try:
        lines = f.readlines()
        assert(len(lines) == 1)
        return _chomp(lines[0])
    finally:
        f.close()

def read_version(configdir=configdir):
    with open(path.join(configdir, 'version'), 'r') as f:
        lines = f.readlines()
        assert(len(lines) == 3)
        return dict(zip(['name', 'commit', 'date'],
                        [_chomp(x) for x in lines]))

mandir = read_mandir()
version = read_version()
