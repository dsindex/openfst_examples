#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
from   optparse import OptionParser
import time

import fst

# code from : https://github.com/vchahun/pyfst/blob/master/examples/edit.py
# for understanding code : http://www.tylerpalsulich.com/blog/2015/05/17/levenshtein-edit-distance-with-fsts/

# --verbose
VERBOSE = 0


def make_edit(sigma):
	"""
	Make an edit distance transducer with operations:
	- deletion:     x:<epsilon>/1
	- insertion:    <epsilon>:x/1
	- substitution: x:x/0 and x/y:1
	"""
	# Create common symbol table
	syms = fst.SymbolTable()

	# Create transducer
	edit = fst.Transducer(syms, syms)
	edit[0].final = True
	for x in sigma:
		edit.add_arc(0, 0, x, fst.EPSILON, 1)
		edit.add_arc(0, 0, fst.EPSILON, x, 1)
		for y in sigma:
			edit.add_arc(0, 0, x, y, (0 if x == y else 1))

	# Define edit distance
	def distance(a, b):
		# Compose a o edit transducer o b
		composed = fst.linear_chain(a, syms) >> edit >> fst.linear_chain(b, syms)
		# Compute distance
		distances = composed.shortest_distance(reverse=True)
		dist = int(distances[0])
		# Find best alignment
		alignment = composed.shortest_path()
		# Re-order states
		alignment.top_sort()
		# Replace <epsilon> -> "-"
		alignment.relabel({fst.EPSILON: '-'}, {fst.EPSILON: '-'})
		# Read alignment on the arcs of the transducer
		arcs = (next(state.arcs) for state in alignment)
		labels = ((arc.ilabel, arc.olabel) for arc in arcs)
		align = [(alignment.isyms.find(x), alignment.osyms.find(y)) for x, y in labels]
		return dist, align

	return distance

def main(a, b):
	"""
	python edit.py atctagctagctagtgctagctgatgctgatcga acgtgtgctagtcgtgatggcatgctg
	Distance: 14
	atctagctagctagtgctagctgat-gc-tgatcga
	a-cgtg-t-gctagt-c--g-tgatggcatgct-g-
	"""

	a = a.decode('utf-8')
	b = b.decode('utf-8')

	edit_distance = make_edit(set(a+b))
	dist, align = edit_distance(a, b)
	print('Distance: {0}'.format(dist))
	x, y = zip(*align)
	print(''.join(x))
	print(''.join(y))


if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()
	
	if options.verbose == 1 : VERBOSE = 1

	startTime = time.time()

	if len(sys.argv) != 3:
		sys.stderr.write('Usage: {0} a b\n'.format(sys.argv[0]))
		sys.exit(1)

	main(*sys.argv[1:])	

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
