phrase = "Python tutorial "
print(phrase + "by Medhansh ")            # concatenation , appending another strings 

# FUNCTIONS 
# functions are blocks of code which you can use 


# string functions 
# you can perform multiple functions  on a string 
# for examples 

print(phrase.upper()) # this will print the string in upper case 
print(phrase.lower()) # this will print the string in lower case 
print(phrase.isupper()) # checks if the whole string is in upper case ( will give output as true or false ) 
# Note - you can check same for lower case as well 

# you can combine two fuctions as well 

print(phrase.upper().isupper()) # this will first convert the string into upper case and then will check if it is in upper case or not 

print(len(phrase)) # to check the length of the string 

print(phrase[0]) # in order to grab a letter at a specified opsition ( this will give the letter at the first position)
# [] is where we specify the index at wich we want the output 
# in python when we perform indexing on a string we start with 0
# example 
# PYTHON
# 012345

# IF I WANTED TO PRINT Y 

print(phrase[1])

#index function 
# it basically tells us where a specific character or string is located 

print(phrase.index("h"))   # so here we gave a value to the function , which is called passing a parameter to the function 
print(phrase.index("Python")) 

# replace function 

print(phrase.replace("Python","java")) # In this we can pass two parameters  

# Note - these were some basic functions you can apply on strings , there are more functions you can work  with  
# for more you can google the list of functions applicable on strings :)
 