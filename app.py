#Printing my invitattion list and sending messages to the invited guests 
family = ['damian','obed','jessie','ahmed']
print("this is a list of the people i have invited for dinner " + str(family))
print("Can you bring my cat back Mr. " + family[0])
print("Tell my son " + family[1] + " to hold onto his bear")
print(family[2] + " is the son of Mr. David")
print(family[3] + " was my bestfriend when he was alive")
print("I have found a bigger table")

#Printing the name of an absent family member and then replacing him
absent = 'obed'
family.remove(absent)
print(absent.title() + " will not be able to make it unfortunately" )
print(family)
family.insert(1,'michael')
print(family)

#Updating the list
family.insert(0,'joe')
family.insert(3,'russel')
family.append('rodney')

#Printing a new set of invitation messages
print("Hello " + family[-1] + " please honor my invitation to dinner with the boys")
print("My dear bother " + family[0] + " it has been a while")
print("I invite you to dinner with me brother " + family[1])
print("It is a pleasure to dine with you, " + family[2])
print("cannot wait to see you " + family[3])





