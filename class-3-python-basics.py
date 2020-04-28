# Class Dated 28/04/2020
# Delivered By Prof. A. M Wani
# Compiled By: Salman Qureshi

print("Hello Text Editor")
print("Hello Python Interactive")
x = input("Hello How Are You? \n")
print(x)
#Prints Value on terminal

#   """Basic built-in functions:"""

# 3. len()
# This function gets the length of object passed as argument .The object can be a string, a tuple,or a list. 
str1 = "Hello! How are you?"
print(len(str1))

# 4.   str()
# Used to convert object to string type  ???? Check its working
# Dont use str as string variable it will override property  of str

x = str(34)
print(x)

# 5. 	abs():
# 	Same as abolute math function.
# 	Provided absolute value of object.
print(abs(-4))

# 6. help():
# 	Useful for getting info of any function ,method or 	keyword
# help()

# 7.	 min():
# 	Returns the smallest element when multiple 	objects passed or smallest element in an 	iterative object

print(min(2,4,7,89))
# o/p: 2

# 8.	 max():
# 	Returns largest element in the above.
print(max(2,3,6))
# o/p: 6

# 9. 	all():**
# Returns True if   all elements in the iterative object elements are true.
list1 = [1,2,3,4]
list2 = [0,2,3,4]
print(all(list1)) #returns true
print(all(list2)) #returns false because 0 is considered as false

# any():**
# Returns True if any element in the iterative object elements are true.


"""
Python – Variables (values)
"""

name = "Salman"
regNo = "1902CukmrXyz"
print(name)
print(regNo)

# carriage return = CR
"""
datatypes
"""
# Strings
# 1. String  slicing :
# Cutting substring from a string by colon (:)
txt = "Hello World"
txt2=txt[6:11]
print(txt2)

# 2. String  accessing values :
char1="Hello Python"
str1="Python Programming"
print("First value is :", char1)
print("Second value is :", str1)

