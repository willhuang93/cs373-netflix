#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

import os, pickle, requests
from numpy import mean, sqrt, square, subtract

movie_avg = None
usr_stats = None
true_cache = None
m_avg = 0

# ------------
# netflix_eval
# ------------
def netflix_eval (movie_id, usr_id, movie_avg, usr_avg) :
	
	"""
	"""

	global true_cache
	global m_avg

	mov_offset = movie_avg - movie_avg
	usr_offset = usr_avg - movie_avg

	estimate = movie_avg + mov_offset + usr_offset

	# print("Movie: [", movie_id, "]\t\tEstimate: ", estimate, "\t\tTrue: ", true_cache[movie_id][usr_id])

	return estimate

# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :

	open_caches()
	# reading in caches from files
	global movie_avg
	global usr_stats
	global m_avg

	# calculations 

	m_cnt = 0
	estimates = []
	true_vals = []
	
	# print(true_cache)

	for k in iter(movie_avg.keys()):
		m_avg += movie_avg[k]
		m_cnt += 1

	m_avg = m_avg / m_cnt

	for line in r:
		if ":" in line:
			movie_id = int(line.replace(":", "").replace("\n", ""))
		else:
			usr_id = int(line)
			result = netflix_eval(movie_id, usr_id, movie_avg[movie_id], usr_stats[usr_id])
			print(true_cache[movie_id][usr_id], " ", result)
			true_vals.append(int(true_cache[movie_id][usr_id]))
			estimates.append(result)

	a = RMSE(true_vals, estimates)

	print("RMSE", a)

	# keys = sorted(iter(t.keys()))

	# for x in keys:
	# 	w.write("customer: " + x + "\n")
	# 	for y in t[x]:
	# 		a = usr_stats[int(y)]
	# 		out = str(a)
	# 		w.write(y + "\t" + out + "\n")
	# 	w.write("\n")


	#	print(cache)
	#	print(bytes)
	#	print(cache[2043])



# ----------------------
# Root Mean Square Error
# ----------------------
def RMSE(true_vals, estimates):
	return sqrt(mean(square(subtract(true_vals, estimates))))

# ----------
# open_cache
# ----------
def open_caches():
	global movie_avg
	global true_cache
	global usr_stats
	
	if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle') :
		f1 = open('/u/downing/public_html/netflix-caches/kh549-movie_average.pickle','rb')
		movie_avg = pickle.load(f1)
	else:
		bytes1 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-movie_average.pickle').content
		movie_avg = pickle.loads(bytes1)

	if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle') :
		f2 = open('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle','rb')
		usr_stats = pickle.load(f2)
	else:
		bytes2 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle').content
		usr_stats = pickle.loads(bytes2)

	if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle') :
		f3 = open('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle', 'rb')
		true_cache = pickle.load(f3)
	else:
		bytes3 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-real_scores.pickle').content
		true_cache= pickle.load(bytes3)




