#!/usr/bin/env python

__revision__ = "test/option-l.py __REVISION__ __DATE__ __DEVELOPER__"

import TestSCons
import string
import sys

test = TestSCons.TestSCons()

test.write('SConstruct', "")

test.run(arguments = '-l 1')

test.fail_test(test.stderr() !=
		"Warning:  the -l option is not yet implemented\n")

test.run(arguments = '--load-average=1')

test.fail_test(test.stderr() !=
		"Warning:  the --load-average option is not yet implemented\n")

test.run(arguments = '--max-load=1')

test.fail_test(test.stderr() !=
		"Warning:  the --max-load option is not yet implemented\n")

test.pass_test()
 
