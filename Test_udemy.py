# numbers = 1, 2, 3, data type integer
# strings = "ahoj", data type string
# lists = [], can be changed
# tuples = (), can not be changed
# dictionary = {}, key values

multiplication = 2.005*50
print(multiplication)

divison = 401/4
print(divison)

exponent = 10.01249219725040309**2
print(exponent)

addition = 100+0.25
print(addition)

substraction = 100.5-0.25
print(substraction)

# What is the value of the expression 4 * (6 + 5)
# 44

first = 4 * (6 + 5)
print(first)

# What is the value of the expression 4 * 6 + 5
# 29

second = 4 * 6 + 5
print(second)

# What is the value of the expression 4 + 6 * 5
# 34

third = 4 + 6 * 5
print(third)

# What is the type of the result of the expression 3 + 1.5 + 4?
# expression = 8.5, it is a float

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s0 = 'hello'
# Print out 'e' using indexing
print(s0[1])

# Reverse the string 'hello' using slicing:
s1 = 'hello'
# Reverse the string using slicing
print(s1[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
s2 ='hello'
# Print out the 'o'

# Method 1:
print(s2[-1])
# Method 2:
print(s2[4])

# Build this list [0,0,0] two separate ways.
# Method 1:

# Method 2:

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]


for i in list3:
    list3[2][2] = 'goodbye'

print(list3)



