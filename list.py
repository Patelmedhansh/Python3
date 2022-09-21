# Working with list in python 
fruits = ["apple " , "mango ", "banana ", "cherry"]  
print(fruits) 

# You can put any peice of data inside pf list , lke strings , numbers , boolean etc ..
# laist is a well organised set of data 

# We can acess individual value by the use of indexing method 

print(fruits[0]) # this will give apple as an output 

# if we put negative value such as -1 , it will give us items from the back of the list 

print(fruits[-1]) #this will give banana as output

print(fruits[1:]) # this will print the values from positon 1 to remaining 

# we can provide range by this method 

print(fruits[1 : 3])  # this will print items from positon 1 to 3 , excluding the item at 3rd position 

# you can manupulate list 

fruits[0] = "kiwi"
# this will replace apple with kiwi 
print(fruits) 

# These were some basics of listas in python , now let us see functions we can perform in list 

# Extend Function 
# this allows us to append another list to the original one 

friends =["vedant", "VTNT"]
 
fruits.extend(friends) 
print(fruits) 
# now along with the list of fruits the friends list will be added 
# in order to add individual value to a list we can use append 

fruits.append("watermelon") 
print(fruits) 

#Note :- Append function is always going to add the element at the end of the list 

# if you want to add the element in the middle / at any specific position in list you can use inssert function 

fruits.insert( 1 , "orange") # insert function takes two parameter , first one is the index position and second one is the value 
print(fruits) 

# to remove any value we use remove 
fruits.remove("orange") 
print(fruits) # orange will be removed  

# if you want to reset the whole list 
friends.clear() 
print(friends)  # all the elements of friends list will be deleted 

fruits.pop() #this will delete the value at the last position in list 
print(fruits) 

print(fruits.index("cherry")) # this will give me the index position of cherry 

print(fruits.count("banana") ) # this will show us how many times the mentioned element is reapeated in the list .

fruits.sort() # it will sort the list in assending order 
print(fruits) 

fruits.reverse() # it will reverse the list 
print(fruits) 

fruits2 = fruits.copy() 
print(fruits2) # now fruits2 will have all the elements of fruits 
