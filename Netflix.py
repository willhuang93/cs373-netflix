#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

import os, pickle, requests

# ----------------------------------------------------
# cache is initialized with lazy values which will get
# updated with each call if new values are discovered
# ----------------------------------------------------

# ------------
# netflix_read
# ------------
def netflix_read (s) :
	"""

	"""

# ------------
# netflix_eval
# ------------
def netflix_eval (i, j) :
	"""
	"""
	# <your code>
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
		
	print(cache)
	print(bytes)

	# for s in r :
	#     i, j = netflix_read(s)
	#     v    = netflix_eval(i, j)
	#     netflix_print(w, i, j, v)
