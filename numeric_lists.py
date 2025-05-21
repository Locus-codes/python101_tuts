#Counting from 1 to 20 using the range function
for value in range(1,21):
    print(value)

#Counting from 1 to 5 and then adding them as list items
numbers = [] #first create an empty list

for value in range(1,6):
    numbers.append(value)
print(numbers)

#An altenate way of Counting from 1 to 1000000 and then adding them as list items called list comprehension
numbers = [value for value in range(1,1000001)]
print(numbers)
print("The minimum value is " + str(min(numbers)))  #finding the minimum value in the list
print("The maximum value is " + str(max(numbers)))  #finding the maximum value in the list
print("The sum of all the values in the list is " + str(sum(numbers)))  #summing up all the values in the list

# Creating a list of odd numbers from 1 to 20
numbers = [] #first create an empty list

for value in range(1,20,2):
    numbers.append(value)
print("This is a list of odd numbers from 1 to 20: " + str(numbers))

# Creating a list of multiples of 3 upto 30
numbers = [] #first create an empty list

for value in range(3,31,3):
    numbers.append(value)
print("This is a list of multiples of 3 upto 30: " + str(numbers))



