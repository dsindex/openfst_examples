#!/usr/bin/env python
#-*- coding: utf8 -*-

# reference : https://gist.github.com/tpalsulich/cbbdf3468654051f7493

import os
import sys
from   optparse import OptionParser
import time

# --verbose
VERBOSE = 0

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()
	
	if options.verbose == 1 : VERBOSE = 1

	startTime = time.time()

	# &#949; = lowercase epsilon
	alphabet = "abc"
	weight = {
		"delete": 1.0,
		"insert": 1.0,
		"sub": 1.0
	}

	# No edit
	for l in alphabet:
		print "0 0 %s %s %.3f" % (l, l, 0)

	# Deletes: input character, output epsilon
	for l in alphabet:
		print "0 0 %s &#949; %.3f" % (l, weight["delete"])

	# Insertions: input epsilon, output character
	for l in alphabet:
		print "0 0 &#949; %s %.3f" % (l, weight["insert"])

	# Substitutions: input one character, output another
	for l in alphabet:
		for r in alphabet:
			if l is not r:
				print "0 0 %s %s %.3f" % (l, r, weight["sub"])

	# Final state
	print 0

	durationTime = time.time() - startTime
	sys.stderr.write("duration time = %f\n" % durationTime)
