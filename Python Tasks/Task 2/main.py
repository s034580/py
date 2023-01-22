# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserMedianAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus medianą.
# 2. funkcija "getOldestUser" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins vyriausio vartotojo vardą.

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]



import statistics

def getUserMedianAge(users):
  ages = [user['age'] for user in users]
  median_age = statistics.median(ages)
  return median_age

def getOldestUser(users):
  sorted_users = sorted(users, key=lambda x: x['age'], reverse=True)
  oldest_user = sorted_users[0]
  return oldest_user['name']

median_age = getUserMedianAge(users)
print(f'Median age: {median_age}')

oldest_user = getOldestUser(users)
print(f'Oldest user: {oldest_user}')