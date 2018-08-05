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

# 교재에는 encoding = encoding 포함되어 있으나 실행시 encoding 문제로 삭제처리함
users = pd.read_csv(upath, sep='::', header=None, names=unames, engine='python')
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, engine='python')
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, engine='python')

# data = pd.merge(pd.merge(ratings, users), movies)

# 성별에 따른 각 영화의 평균 평점을 구하려면 pivot_table 메서드를 사용하면 된다
# mean_ratings = mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

# 데이터를 영화 제목으로 그룹화하고 size() 함수를 사용해서 제목별 평점 정보 건수를 series 객체로 얻어낸다
# ratings_by_title = data.groupby('title').size()

# 이 중에서 250건 이상의 평점 정보가 있는 영화만 추린다
# active_titles = ratings_by_title.index[ratings_by_title >=250]

# 250건 이상의 평점 정보가 있는 영화에 대한 색인은 mean_ratings에서 항목을 선택하기 위해 사용
# mena_ratings = mean_ratings.ix[active_titles]

# 여성에게 높은 평점을 받은 영화 목록을 확인하기 위해 F열을 내림차순으로 정렬한다
# top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

# 남녀간의 호불호가 갈리는 영화를 찾아보자
# mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']