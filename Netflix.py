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
	true_cache, bytes = None
	# <your code>
	if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle') :
		f = open('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle')
		true_cache = pickle.load(f)
	else:
		bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-real_scores.pickle').content
		true_cache= pickle.load(bytes)
	
	return 1

# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :

	# reading in caches from files
	movie_avg = None
	usr_stats = None

	if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle') :
		# Read cache from file system
		f = open('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle','rb')
		movie_avg = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-movie_average.pickle').content
		movie_avg = pickle.loads(bytes)

	if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle') :
		# Read cache from file system
		f = open('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle','rb')
		usr_stats = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle').content
		usr_stats = pickle.loads(bytes)


	# print(type(usr_stats))
	# for x in usr_stats:
	# 	for y in x:
	# 		print(x, ": ", y)

	# calculations 
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
		w.write("customer: " + x + "\n")
		for y in t[x]:
			a = usr_stats[int(y)]
			out = str(a)
			w.write(y + "\t" + out + "\n")
		w.write("\n")


	#	print(cache)
	#	print(bytes)
	#	print(cache[2043])



