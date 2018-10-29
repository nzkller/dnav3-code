"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
pit = type(pi)
print ("Pi value is",pi,"and it's a",pit)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
	print("i is less than 50","i is",i)
elif i > 50:
	print("i is greater than 50","i is",i)
else:
	print("i is equal to 50","i is",i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
	print("oranges are orange")
elif picked_fruit == 'strawberry':
	print("straeberries are red")
else:
	print("bananas are yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult(num1, num2):
	result = num1 * num2
	return result

# TODO: Now call the function a few times to calculate the following answers

First = mult(12,96)
print("12 x 96 =",First)
Second = mult(48,17)
print("48 x 17 =",)
Third = mult (196523,87323)
print("196523 x 87323 =",Third)
