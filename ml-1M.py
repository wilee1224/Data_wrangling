import pandas as pd
import os
import sys
reload(sys)
# encoding = 'latin1'

upath = os.path.expanduser('users.dat')
rpath = os.path.expanduser('ratings.dat')
mpath = os.path.expanduser('movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding, engine='python')
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding, engine='python')
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding, engine='python')

# mean_ratings = mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# data = pd.merge(pd.merge(ratings, users), movies)
