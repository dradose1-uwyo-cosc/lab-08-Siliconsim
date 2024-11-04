# Jake Huggins  
# UWYO COSC 1010
# 11/4/2024 
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:
# https://www.geeksforgeeks.org/convert-string-to-float-in-python/

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

import math as math

def is_string(converting_string):
    try:
        num = float(converting_string)
    except:
        return False

    if (type(num) == float):
        num = round(num, 1)
    else:
        num = int(converting_string)
    return num

print(is_string("39.44"))
print(is_string("39"))
print(is_string("This is not a number"))

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def calculate_values(slope, intercept, lower_x, upper_x):
    values = []
    if lower_x > upper_x:
        temp = lower_x
        lower_x = upper_x
        upper_x = temp

    for i in range(lower_x, upper_x + 1):
        value = int((slope * i) + intercept)
        values.insert(value, value)
    return values

print("*" * 75)
slope = 0
intercept = 0
lower_x = 0
upper_x = 0

while (True):
    try:
        slope = float(input("Please input a proper value for the slope: "))
        intercept = float(input("Please input a proper value for the y-intercept: "))
        lower_x = int(input("Please input a proper value for the lower x bound: "))
        upper_x = int(input("Please input a proper value for the upper x bound: "))
        break
    except:
        print('Invalid Input!')
        continue

print(calculate_values(slope, intercept, lower_x, upper_x))

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def calculate_roots(a, b, c):
    determinant = (b * b) - (4*a*c)
    print(determinant)
    if determinant < 0:
        return "No real solutions"
    
    positive_root = ((-b) + math.sqrt(determinant)) / (2*a)
    negative_root = ((-b) - math.sqrt(determinant)) / (2*a)

    if (positive_root == negative_root):
        return positive_root
    return [positive_root, negative_root]

a, b, c = 0, 0, 0
while (True):
    try:
        a = int(input("Please input a proper value for the a value: "))
        b = int(input("Please input a proper value for the b value: "))
        c = int(input("Please input a proper value for the c value: "))
        break
    except:
        print('Invalid Input!')
        continue

print(calculate_roots(a,b,c))