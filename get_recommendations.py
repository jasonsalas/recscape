from __future__ import (absolute_import, division, print_function, unicode_literals)
from collections import defaultdict
from surprise import Dataset, Reader, evaluate, dump
import os, io


# load the trained and serialized model
predictions, algorithm = dump.load('serialized_model')


def resolve_ids_to_names():
	# map usernames and movie names to their IDs in their respective files
	users_file = os.path.expanduser('users.txt')
	movies_file = os.path.expanduser('movies.txt')
	movie_titles = {}
	user_names = {}

	with io.open(movies_file, 'r', encoding='ISO-8859-1') as movies:
		for movie in movies:
			movie = movie.split('|')
			movie_titles[movie[0]] = movie[1]

	with io.open(users_file, 'r', encoding='ISO-8859-1') as users:
		for user in users:
			user = user.split('|')
			user_names[user[0]] = user[1]

	return movie_titles, user_names 

def get_recommendations(predictions, top_n=10):
	# borrowed from http://surprise.readthedocs.io/en/stable/FAQ.html#how-to-get-the-top-n-recommendations-for-each-user
	recommendations = defaultdict(list)

	for uid, iid, true_r, est, _ in predictions:
		recommendations[uid].append((iid, est))

	for uid, user_ratings in recommendations.items():
		user_ratings.sort(key=lambda x:x[1], reverse=True)
		recommendations[uid] = user_ratings[:top_n]

	return recommendations

recommendations = get_recommendations(predictions, top_n=5)
movie_titles, user_names = resolve_ids_to_names()

full_roster_recomendations = []
for uid, user_ratings in recommendations.items():
	full_roster_recomendations.append((user_names[uid], [movie_titles[iid] for (iid, _) in user_ratings]))

userid = raw_input('Enter the userID or ALL:')
if userid == 'all':
	print(full_roster_recomendations)
else:
	print(full_roster_recomendations[int(userid)])