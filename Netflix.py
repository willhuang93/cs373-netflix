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
# mov_yearly_rating = None	# {(m_id, year): rating, ...}
# usr_decade_rating = None	# {usr_id: {year : rating, ...}}
# usr_yearly_rating = None	# {(usr_id, year) : rating, ...}
movie_years = None
total_avg = 0

# ------------
# netflix_eval
# ------------
def netflix_eval (year, movie_avg, usr_avg) :
	
	"""
	calculates the estimate value for a predicated customer movie rating
	first accounts for the movie's rating relative to the average rating of all the movies in mov_offset
	then accounts how critical the user is relative to the movie in usr_offset
	then uses how old the movie is as an offset to determine the trend of ratings for movies released in different movie_years
	uses the movie average as a base line and add the 3 factors to it to get the estimate
	"""

	assert (movie_avg >= 0)
	assert (usr_avg >= 0)

	tot_avg = 3.2281371945001136
	
	year_diff = 0
	mov_offset = movie_avg - tot_avg # 1.771862805
	usr_offset = usr_avg - movie_avg
	
	
	# if year > 2004:
	# 	year_diff = -0.45
	if year > 2003:
		year_diff = -0.425
	elif year > 2002:
		year_diff = -0.4
	elif year > 2001:
		year_diff = -0.375
	elif year > 2000:
		year_diff = -0.3
	elif year > 1995:
		year_diff = -0.3
	elif year > 1990:
		year_diff = -0.28
	elif year > 1985:
		year_diff = -0.27
	elif year > 1980:
		year_diff = -0.3
	elif year > 1975:
		year_diff = -0.2
	elif year > 1970:
		year_diff = -0.15
	elif year > 1965:
		year_diff = -0.1
	elif year > 1960:
		year_diff = -0.05
	elif year > 1955:
		year_diff = 0
	elif year > 1950:
		year_diff = 0.05
	elif year > 1945:
		year_diff = 0.1
	elif year > 1940:
		year_diff = 0.11
	elif year > 1930:
		year_diff = 0.12
	elif year > 1920:
		year_diff = 0.13
	elif year > 1910:
		year_diff = 0.14
	elif year > 1900:
		year_diff = 0.15

	estimate = movie_avg + mov_offset + usr_offset + year_diff

	if estimate > 5:
		estimate = 5
	elif estimate < 0:
		estimate = 0

	assert (estimate >= 0 and estimate <= 5)
	

	return estimate

# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :

	"""
	feeds 2 lists to RMSE(a, b), the list containing true values, and the list containing estimated values, matched by the movie being compared
	calls netflix_eval to predicate customer rating for a movie
	takes input and iterates over each movie, predicating a rating for each customer
	uses cache values in predications
	returns overall RMSE for TestNetflix.py
	"""

	open_caches()	# reading in caches from files
	
	global movie_avg
	global usr_stats
	global total_avg
	global movie_years

	# ----------
	# processing 
	# ----------

	m_cnt = 0
	year = 0
	estimates = []
	true_vals = []
	output = dict()
	temp = []

	for k in iter(movie_avg.keys()):
		total_avg += movie_avg[k]
		m_cnt += 1

	total_avg = total_avg / m_cnt

	for line in r:
		if ":" in line:
			m_id = int(line.replace(":", "").replace("\n", ""))
			if movie_years[m_id] is not None:
				year = int(movie_years[m_id])
			temp = []
			output[m_id] = temp
		else:
			u_id = int(line)
			result = netflix_eval(year, movie_avg[m_id], usr_stats[u_id])
			true_vals.append(int(true_cache[m_id][u_id]))
			estimates.append(result)
			temp.append(result)

	a = RMSE(true_vals, estimates)

	sorted(output.items(), key = lambda output : output[0] )
	
	netflix_print(w, a, output)

	return int(a)
	# ----------
	# processing 
	# ----------

#--------------
# netflix_print
#--------------
def netflix_print(w, rmse, output):

	"""
	prints the movie id, followed by a list of customers predicated ratings, and the final overall RMSE
	"""

	for k in iter(output.keys()):
		# print(str(k).strip(' \t'), ":")
		w.write(str(k) + ":\n")
		for x in output[k] :
			w.write(str(round(x, 1)) + "\n")

	w.write("RMSE: " + str(rmse))


# ----------------------
# Root Mean Square Error
# ----------------------
def RMSE(true_vals, estimates):

	"""
	calculates RMSE using fastest method taught in class, i.e. numpy
	"""
	return sqrt(mean(square(subtract(true_vals, estimates))))

# ----------
# open_cache
# ----------
def open_caches():
	"""
	Open all relevant caches to be used and make them globally available in the program
	"""

	global movie_avg
	global true_cache
	global usr_stats
	# global mov_yearly_rating
	# global usr_decade_rating
	# global usr_yearly_rating
	global movie_years
	
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

	# if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-avg_customer_rating_per_movie_decade.pickle') :
	# 	f4 = open('/u/downing/public_html/netflix-caches/mdg7227-avg_customer_rating_per_movie_decade.pickle','rb')
	# 	usr_decade_rating = pickle.load(f4)
	# else:
	# 	bytes4 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-avg_customer_rating_per_movie_decade.pickle').content
	# 	usr_decade_rating = pickle.loads(bytes4)

	# if os.path.isfile('/u/downing/public_html/netflix-caches/pas2465-movie_year_avgs2.pickle') :
	# 	f5 = open('/u/downing/public_html/netflix-caches/pas2465-movie_year_avgs2.pickle','rb')
	# 	mov_yearly_rating = pickle.load(f5)
	# else:
	# 	bytes5 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/pas2465-movie_year_avgs2.pickle').content
	# 	mov_yearly_rating = pickle.loads(bytes5)

	# if os.path.isfile('/u/downing/public_html/netflix-caches/pas2465-user_year_avgs2.pickle') :
	# 	f6 = open('/u/downing/public_html/netflix-caches/pas2465-user_year_avgs2.pickle','rb')
	# 	usr_yearly_rating = pickle.load(f6)
	# else:
	# 	bytes6 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/pas2465-user_year_avgs2.pickle').content
	# 	usr_yearly_rating = pickle.loads(bytes6)

	if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-all_movie_years.pickle') :
		f7 = open('/u/downing/public_html/netflix-caches/mdg7227-all_movie_years.pickle','rb')
		movie_years = pickle.load(f7)
	else:
		bytes7 = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-all_movie_years.pickle').content
		movie_years = pickle.loads(bytes7)



