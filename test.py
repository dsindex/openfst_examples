#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
from   optparse import OptionParser
import time

import pywrapfst as fst

# --verbose
VERBOSE = 0

def num_arcs_and_states(f) :
	return sum(1 + f.num_arcs(s) for s in f.states())

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()
	
	if options.verbose == 1 : VERBOSE = 1

	startTime = time.time()

	f = fst.Fst.read("binary.fst")

	for state in f.states() :
		for arc in f.arcs(state) :
			print state, arc.ilabel, arc.olabel, arc.weight, arc.nextstate

	print "num_arcs_and_states = ", num_arcs_and_states(f)

	print f

	f.draw("f.gv")

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
