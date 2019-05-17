import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
print(type(fandango))
fandango_films = fandango.set_index('FILM', drop=False)
#print(fandango_films.index)
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
#print types
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]
#print float_df
# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_user.apply(lambda x: np.std(x), axis=1)


