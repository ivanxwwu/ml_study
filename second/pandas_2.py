import pandas
food_info = pandas.read_csv("food_info.csv")
# print(food_info.loc[0])
# print(food_info.loc[3:6])
#
# print(food_info["NDB_No"])

columns = ["Zinc_(mg)", "Copper_(mg)"]
zipc_copper = food_info[columns]
#print(zipc_copper)

cols_names = food_info.columns.tolist()
#print(cols_names)
gram_columns = []
for c in cols_names:
    if c.endswith('(g)'):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
#print(gram_df.head(3))

#print(food_info["Iron_(mg)"])
div_1000 = food_info["Iron_(mg)"] / 1000
#print(div_1000)

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
iron_grams = food_info["Iron_(mg)"] / 1000
food_info["Iron_(g)"] = iron_grams
print(food_info.shape)

weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
initial_rating = weighted_protein + weighted_fat

max_calories = food_info["Energ_Kcal"].max()
# Divide the values in "Energ_Kcal" by the largest value.
normalized_calories = food_info["Energ_Kcal"] / max_calories
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat


food_info.sort_values("Sodium_(mg)", inplace=True)
print(food_info["Sodium_(mg)"])
#Sorts by descending order, rather than ascending.
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
print(food_info["Sodium_(mg)"])


