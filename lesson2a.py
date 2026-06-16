# Python List

cars=["Honda" , "Mazda" , "Mercedes" , "Volkswagon" , "Surf"]
# show output
print(cars)

# print item at a given index
# NB: We count from zero index

print(cars[3])
print(cars[2])

# appending new items
# NB: Adds at the end of list

cars.append("BMW")
# show output
print(cars)

cars.append("Rolls Royce")
# show output
print(cars)

# slicing
print(cars[0:2])
print(cars[1:4])

# inserting item at a given index
cars.insert(2, "Toyota")
print(cars)

cars.insert(3, "Range Rover")
print(cars)

