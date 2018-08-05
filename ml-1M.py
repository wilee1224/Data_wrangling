import pandas as pd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# encoding = 'latin1'

upath = os.path.expanduser('users.dat')
rpath = os.path.expanduser('ratings.dat')
mpath = os.path.expanduser('movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, engine='python')
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, engine='python')
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, engine='python')

# data = pd.merge(pd.merge(ratings, users), movies)
# mean_ratings = mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

