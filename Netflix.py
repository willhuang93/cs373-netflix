#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

import os, pickle, requests

# ------------
# netflix_eval
# ------------
def netflix_eval (i, j) :
	"""
	"""
	cache, bytes = None
	# <your code>
	if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle') :
		f = open('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle')
		cache = pickle.load(f)
	else:
		bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-real_scores.pickle').content
		cache= pickle.load(bytes)
	
	return 1

# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :
	cache = None
	bytes = None
	if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle') :
		# Read cache from file system
		f = open('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle','rb')
		cache = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-movie_average.pickle').content
		cache = pickle.loads(bytes)
	
	# p = iter(r)
	t = dict()
	m = 0 
	for line in r:
		if ":" in line:
			m = line.replace(":", "").replace("\n", "")
			t[m] = []
		else:
			t[m].append(line.replace("\n", ""))
		# w.write(m + "\t" + line)
	keys = sorted(iter(t.keys()))
	for x in keys:
		w.write(x + " ")
		for y in t[x]:
			w.write(y + " ")
		w.write("\n")
	#	print(cache)
	#	print(bytes)
	#	print(cache[2043])

