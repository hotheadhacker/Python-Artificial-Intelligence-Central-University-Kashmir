# Class Dated 12/05/2020
# Delivered By Prof. A. M Wani
# Compiled By: Salman Qureshi
"""
Python-  More   Data types-----   Lists
"""
######
"""
1) Apart from numbers and strings which are fundamental data types , there other fundamental data types : Lists and Tuples 
2) These are used to organize data in a structured manner.
3) Most Popular built-in sequence of Python language.

"""
###
"""
a) More on  Lists :
1. More flexible ordered collection data type
2. Unlike strings , lists can contain all types of data such as numbers, strings, and even other lists, too.
3. Lists are mutable in nature i.e. you can change it while assigning and slices.

b) Property of Lists:
1. Collection of arbitrary objects. Can collect other objects and treat them as ordered group and maintained left to right positional ordering.
2. Accessed by offset: By indexing the list. Can do slicing and concatenation .
3. Variable length , nesting:  Unlike strings , lists can grow and shrink according to the need of the program.
4. Mutable: We can change lists at any place and it responds to all operations like slicing , indexing and concatenation and result in new lists even if we are changing in a string.
5.Object reference:  when we assign an object to data structure components and variable name, Python stores the reference to the same object ( variable)  name. It will not store the reference to the copy of that object.


"""

# Operations and code examples
list1 = ['script', 'pearl', 'goLang']
print(list1)  # o/p: ['script', 'pearl', 'goLang']
print(list1[1])  # o/p: pearl
print(list1[1:])  # o/p: ['pearl', 'goLang']
list1.append('ruby')
print(list1)  # o/p: ['script', 'pearl', 'goLang', 'ruby']
list1.sort()
print(list1)  # o/p: ['goLang', 'pearl', 'ruby', 'script'] lexically
