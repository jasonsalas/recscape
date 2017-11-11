# recscape
A fun little recommender engine built on top of Surprise ([lib](http://surpriselib.com/)|[docs](http://surprise.readthedocs.io/en/stable/index.html)|[repo](https://github.com/NicolasHug/Surprise)) and the [MovieLens 100K](https://grouplens.org/datasets/movielens/) dataset. Surprise is a delightful library for Python for quick prototyping and evaluation of machine learning recommendation algorithms.

----
## motivation
This project can be used to train a recommender for a model-based movie service. The sample size is intentionally reduced from other projects for quick processing suitable for public demos and to test the levels at which relatively reliable recommendations can be made with small sample sizes, for techniques like [LSI](https://en.wikipedia.org/wiki/Latent_semantic_analysis).

----
## data
The dataset is a mini-version of the titles listed in the MovieLens 100K dataset, being the first 500 listed, with 50 users - the 50 highest quarterbacks with the [most all-time passing yards](https://www.pro-football-reference.com/leaders/pass_yds_career.htm) in NFL history.

The data is contained in three static files - [users.txt](https://github.com/jasonsalas/recscape/blob/master/users.txt), [movies.txt](https://github.com/jasonsalas/recscape/blob/master/movies.txt), and [ratings.txt](https://github.com/jasonsalas/recscape/blob/master/ratings.txt) - emulate the same file structure for datafiles used by MovieLens - just smaller and not with anonymized users.

-----
## memory-based collaborative filtering
The dataset I built is small enough to be able to compute with a memory-based collaborative filtering approach [in a spreadsheet](https://docs.google.com/spreadsheets/d/18S_3gbqkspkFpTKQGFjrmggjzDm3qWfdp9ODuiVtusw/edit?usp=sharing), or as a machine learning problem by training the model and assembling the top-n results for users - either individually or collectively.

The data is raw, but item-item collaborative filtering will likely generate the most practical results.

----
## model-based matrix factorization
[SVD](https://en.wikipedia.org/wiki/Singular-value_decomposition) is used to compute the top-n films recommended to users.

----
## issues
Because the sample size of the data is small - a 50-x-500 matrix that is intentionally sparse - the error is quite large. This is proof-of-concept - more data is needed to make any sort of reliable predictions about ratings of a meaningful top-n list that isn't all over the place. Also, because the [data assembled](https://github.com/jasonsalas/recscape/blob/master/make_recommendations_model.py) in is completely randomized, there's no discernible patterns in the data to be detected. 

----
## naming
I picked **recscape** for the name of this non-commercial project because it sounds cool. If any IP conflicts exist, please do let me know and I'll change it. :)
