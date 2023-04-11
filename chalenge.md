Padlock 1

For each of these challenges you will need to write a computer program to work out the padlock code (3-digit number). Your program will need to output the solution of the given hint. You will then be able to input this combination onto the padlock to see if it unlocks it!

Padlock Hint
code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40

#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/

code = 0
#Update the code below to solve this challenge
for i in range(1,41):
print(i)

print("Code:")
print(code)

#Padlock 2

For each of these challenges you will need to write a computer program to work out the padlock code (3-digit number). Your program will need to output the solution of the given hint. You will then be able to input this combination onto the padlock to see if it unlocks it!

Padlock Hint
code = Total number of 3-digit combinations where digit1 < digit2 < digit3

e.g. 123 and 358 count as valid combinations whereas 321 or 011 are invalid combinations.

#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

code = 0
#Update the code below to solve this challenge
for digit1 in range(0,10):
for digit2 in range(0,10):
for digit3 in range(0,10):
print(str(digit1)+str(digit2)+str(digit3))

print("Code:")
print(code)

#PADLOCK 3

For each of these challenges you will need to write a computer program to work out the padlock code (3-digit number). Your program will need to output the solution of the given hint. You will then be able to input this combination onto the padlock to see if it unlocks it!

Padlock Hint
code = Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers

e.g. 024 and 886 count as valid combinations whereas 124 or 456 are invalid combinations.

#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

code = 0
#Update the code below to solve this challenge
for digit1 in range(0,10):
for digit2 in range(0,10):
for digit3 in range(0,10):
print(str(digit1)+str(digit2)+str(digit3))

print("Code:")
print(code)

#PADLOCK 4
For each of these challenges you will need to write a computer program to work out the padlock code (3-digit number). Your program will need to output the solution of the given hint. You will then be able to input this combination onto the padlock to see if it unlocks it!

Padlock Hint
code = Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number

e.g. 034 and 555 count as valid combinations whereas 123 or 468 are invalid combinations.

#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

code = 0
#Update the code below to solve this challenge
for digit1 in range(0,10):
for digit2 in range(0,10):
for digit3 in range(0,10):
print(str(digit1)+str(digit2)+str(digit3))

print("Code:")
print(code)

#PADLOCK 5

For each of these challenges you will need to write a computer program to work out the padlock code (3-digit number). Your program will need to output the solution of the given hint. You will then be able to input this combination onto the padlock to see if it unlocks it!

Padlock Hint
code = Total number of 3-digit combinations where at least two digits are equal.

e.g. 030 and 558 count as valid combinations whereas 123 or 468 are invalid combinations.

#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

code = 0
#Update the code below to solve this challenge
for digit1 in range(0,10):
for digit2 in range(0,10):
for digit3 in range(0,10):
print(str(digit1)+str(digit2)+str(digit3))

print("Code:")
print(code)