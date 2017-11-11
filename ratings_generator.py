from random import randint
import io

'''
    assembles a generic rating data file
    ==========================================================================
    - dataset: https://docs.google.com/spreadsheets/d/18S_3gbqkspkFpTKQGFjrmggjzDm3qWfdp9ODuiVtusw/edit?usp=sharin
g    - the demo matrix is 50-x-500 using the top passing quarterbacks in NFL history as usernames (https://www.pro-football-reference.com/leaders/pass_yds_career.htm) and MovieLens 100K film titles (https://grouplens.org/datasets/movielens/)
    - ratings formatted as pipe-separated values: userID|movieID|rating 
   
'''
NUMBER_OF_USERS = 51
NUMBER_OF_MOVIES = 501

user_index = 1
movie_index = 1

with io.open('ratings.txt', 'w', encoding='ISO-8859-1') as f:
    while user_index < NUMBER_OF_USERS:
        while movie_index < NUMBER_OF_MOVIES:
            # the rating scale is 1-5, but generate a wider range, then ignore the higher values to simulate matrix sparsity
            rating = randint(1,12)    
            if rating <= 5:
                f.write(str(user_index) + '|' + str(movie_index) + '|')
                f.write(str(rating) + '\n')
            
            movie_index = movie_index + 1
            
        movie_index = 1
        user_index = user_index + 1
        
print('ALL DONE.')