import pandas

dataframe = pandas.read_csv("GoogleApps.csv")

avg_price = round(dataframe[dataframe['Price'] > 0]['Price'].mean(), 2)
print("Average price:", avg_price, "$")

max_price = dataframe['Price'].max()
print("Max price:", max_price, "$")

min_price = dataframe['Price'].min()
print("Min price:", min_price, "$")

free_amount = dataframe[dataframe['Price'] == 0.0]['Price'].count()
total_amount = dataframe['Price'].count()
free_apps_procente = round(free_amount * 100 / total_amount, 2)
print(str(free_apps_procente) + "%", "- free apps")

print("\n-------------------------------------------------\n")
# dataframe.info()
a = dataframe.groupby(by=['Type', 'Category'])['Rating'].agg(['min', 'max', 'mean', 'count'])
print(a)


