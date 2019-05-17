import pandas as pd
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
#print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
print (series_rt[0:5])

from pandas import Series
film_names = series_film.values
#print type(film_names)
#print film_names
rt_scores = series_rt.values
#print rt_scores
print(film_names)
series_custom = Series(rt_scores , index=film_names)
print(rt_scores)
print(series_custom[['Minions (2015)', 'Leviathan (2014)']])



original_index = series_custom.index.tolist()
#print original_index
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()


import numpy as np
# Add each value with each other
print(np.add(series_custom, series_custom))
# Apply sine function to each value
np.sin(series_custom)
# Return the highest value (will return a single value not a Series)
np.max(series_custom)


series_custom > 50
series_greater_than_50 = series_custom[series_custom > 50]

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(both_criteria)



rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users)/2

print(rt_mean)