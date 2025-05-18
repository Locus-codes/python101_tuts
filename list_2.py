#This program explores the organization of lists

places = ['paris','carlifonia','berlin','london','sydney']
print("This is the original order of the list: ")
print(places)

print("This is a sorted list: ")
print(sorted(places)) #this method prints a temporarily sorted list 

print("This is the original list again: ")
print(places)

print(sorted (places , reverse = True )) #temporarily reverse sort the list
print("This is the original order again: ")
print(places)

# Using the reverse method to change the order of a list 
places.reverse()
print(places)

#reversing back to the original order
places.reverse()
print(places)

# Using the sort() method to alphabetically sort a list
places.sort()
print(places)

places.sort(reverse = True)   # Reversing the order back
print(places)

# Checking the length of the list 
print(len(places))
print("C'est fin")


