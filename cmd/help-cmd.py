#!/bin/sh
"""": # -*-python-*-
bup_python="$(dirname "$0")/bup-python" || exit $?
exec "$bup_python" "$0" ${1+"$@"}
"""
# end of bup preamble
import sys, os, glob

from bup import config
from bup import options, path
from bup.helpers import log

optspec = """
bup help <command>
"""
o = options.Options(optspec)
(opt, flags, extra) = o.parse(sys.argv[1:])

if len(extra) == 0:
    # the wrapper program provides the default usage string
    os.execvp(os.environ['BUP_MAIN_EXE'], ['bup'])
elif len(extra) != 1:
    o.fatal("exactly one command name expected")

if not config.mandir:
    log("error: manpages weren't installed; no mandir in %r\n"
        % config.configdir)
    sys.exit(1)

docname = (extra[0]=='bup' and 'bup' or ('bup-%s' % extra[0]))
origmp = os.environ.get('MANPATH', None)
manpath = config.mandir + ':' + origmp if origmp else config.mandir
try:
    os.environ['MANPATH'] = manpath
    os.execvp('man', ['man', docname])
except OSError, e:
    sys.stderr.write('Unable to run man command: %s\n' % e)
    sys.exit(1)
finally:
    if origmp:
        os.environ['MANPATH'] = origmp
    else:
        del os.environ['MANPATH']
