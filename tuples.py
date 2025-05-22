# Introduction to tuples - immutable lists
dimensions = (200,300)
print("This is the original version: ")
print(dimensions)

dimensions = (5,9)
print("This a modified version: ")
print(dimensions)

dimensions[0] = 4  # This will raise a type error

# tuple implementation
foods = ('rice','fufu','porridge','pasta','pizza')

print("This is the original tuple")
# Using for loop to print the elements of a tuple 
for food in foods:
    print(food)
print("\n")

# Writing over the tuple since tuples are immutable
foods = ('rice','chip','burger','pasta','pizza')

print("This is the modified tuple")
for food in foods:
    print(food)
