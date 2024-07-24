# set donot allow duplicate values
# duplicate values will be removed
# Any type of data can be stored
# we can add or remove

a = {1,2,3,4,5,1,3}
print(a) #output - {1, 2, 3, 4, 5}
a.add(6) # we can add values
print(a) #output - {1, 2, 3, 4, 5, 6}
a.remove(1)
print(a) #output - {2, 3, 4, 5, 6}
print(a.pop()) #output - 2 it is an unordered
print(a) #After pop {3, 4, 5, 6}