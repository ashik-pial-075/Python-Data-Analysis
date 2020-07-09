opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)

header = apps_data[0]
apps_data = apps_data[1:]

rating_sum = 0 

for index in apps_data:
    rating = float(index[7])
    rating_sum += rating

avg_rating = rating_sum / len(apps_data)

print(avg_rating)
