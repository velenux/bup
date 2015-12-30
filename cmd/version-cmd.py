#!/bin/sh
"""": # -*-python-*-
bup_python="$(dirname "$0")/bup-python" || exit $?
exec "$bup_python" "$0" ${1+"$@"}
"""
# end of bup preamble
import sys
from bup import options
from bup.config import version

optspec = """
bup version [--date|--commit|--tag]
--
date    display the date this version of bup was created
commit  display the git commit id of this version of bup
tag     display the tag name of this version.  If no tag is available, display the commit id
"""
o = options.Options(optspec)
(opt, flags, extra) = o.parse(sys.argv[1:])


total = (opt.date or 0) + (opt.commit or 0) + (opt.tag or 0)
if total > 1:
    o.fatal('at most one option expected')

if opt.date:
    print version['date'].split(' ')[0]
elif opt.commit:
    print version['commit']
else:
    print version['name']
