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