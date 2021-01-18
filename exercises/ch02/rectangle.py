#!/usr/bin/env python3

# display a welcome message
print("The Area & Perimeter Program")
print()

# get input from the user
length= int(input("Please enter the length:"))
width = int(input("Please enter the width:\t"))

# calculate area & perimeter
area = (length * width)
perimeter = (length * 2) + (width * 2)
            
# format and display the result
print()
print("Area =" + " " + str(area))
print("Perimeter =" + " " + str(perimeter))
print()
print("Thanks for using this program!")

