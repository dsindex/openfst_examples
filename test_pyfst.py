#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
from   optparse import OptionParser
import time

import fst

# --verbose
VERBOSE = 0

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()
	
	if options.verbose == 1 : VERBOSE = 1

	startTime = time.time()

	t1 = fst.Transducer()
	t1.add_arc(0, 1, 'a', 'a')
	t1.add_arc(1, 2, 'b', 'b')
	t1.add_arc(2, 2, 'c', 'c')
	t1[2].final = True	
	

	t2 = fst.Transducer()
	t2.add_arc(0, 1, 'c', 'c')
	t2.add_arc(1, 2, 'b', 'b')
	t2.add_arc(2, 3, 'a', 'a')
	t2[3].final = True	

	'''
	while 1 :
		try : line = sys.stdin.readline()
		except KeyboardInterrupt : break
		if not line : break

		line = line.strip()
		if not line : 
			continue
	'''

	durationTime = time.time() - startTime
	sys.stderr.write("duration time = %f\n" % durationTime)
