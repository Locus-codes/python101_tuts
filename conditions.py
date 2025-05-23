cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Equality
if cars[0] == 'audi':
    print("True")

# Checking for Inequality
if cars[2] != 'toyota':
    print("False")

values = [2, 3, 4, 2, 5, 2]

values = [2, 3, 4, 2, 5, 2]

# Show the boolean result
print("Condition 1 check:", values[2] > 8 and values[3] > 9)
print("Condition 2 check:", values[1] > 2 or values[2] < 1)

# First check: both must be true
if values[2] > 8 and values[3] > 9:
    print("Condition 1 is True: both > 8 and > 9")

# Second check: at least one must be true
elif values[1] > 2 or values[2] < 1:
    print("Condition 2 is True: either > 2 or < 1")


# Using the not statement
if not (values[0] == 2):  # False because values[0] *is* 2
    print("It's not 2")
else:
    print("It is 2")

# Example 2
banned_users = ['andrew','isaac','michael']
user = 'marie'

if user not in banned_users:
    print(user.title() + " is not in the banned list")

# Using elif statements
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is " + str(price)  + ".")

# using a series of if blocks to act on all conditions that come out true
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese'in requested_toppings:
    print("Adding extra cheese")

print("Finishes making your pizza!")

# Alien game with multiple if blocks
alien_color = ['green','yellow','red']

if 'green' in alien_color:
    print("Player just earned 5 points.")
if 'red' in alien_color:
    print("Player just earned 3 points.")
if 'blue' in alien_color:
    print("Player earned 10 points.")

# Alien game with an if-else chain
alien_colors = ['green','blue','aqua']

if alien_colors == 'green':
    print("Player just earned 5 points!")
else:
    print("Player just earned 10 points!")

print("הוּא כְּבָר כָּלֹּי")



