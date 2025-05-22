pizzas = ['pepperoni','barbecue','pineapple','vegetable']

for pizza in pizzas:
    print("I like " + pizza + " pizza!" )

print("\n" + pizzas[2] + " is my favorite.")
print(pizzas[1] + " is second on the list.")
print("\nI really love pizza!")

# Slicing the original list to create a copy of it
friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('calloni')

print("My favorite pizzas are: ")
print(pizzas)

print("My friend's favorite are: ")
print(friend_pizzas)


animals = ['dogs','horses','cats']

for animal in animals:
    print("I love " + animal)

print("\nAll these animals have 4 limbs.")
