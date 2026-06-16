# Python Dictionary

person={
    "firstname": "Mark" ,
    "lastname" : "Doe" ,
    "age": 24 ,
    "salary": 67000 ,
    "favourite_colors" : ["blue","green"]

}
print(person)

# accessing key-value
print(person["firstname"])
print(person["lastname"])

# update key-value pairs
person["age"]=34
print(person)

person["firstname"]= "Rufus"
person["lastname"]="Kamau"
print(person)

# adding a new key-value there
person["passport"]= "mh7654"
print(person)

# delete the salary
del person["salary"]
print(person)

del person["firstname"]
print(person)