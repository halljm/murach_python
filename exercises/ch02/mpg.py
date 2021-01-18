#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_gal = float(input("Enter cost per gal:\t"))

# calculate miles per gallon
# mpg = miles_driven / gallons_used
mpg = round((miles_driven / gallons_used), 1)

#calc cost per mile
cost_mile = float((cost_gal * gallons_used) / miles_driven)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print()
print("Total Gas Cost:\t\t" + str(cost_gal * gallons_used))
print("Cost per mile:\t\t" + str(cost_mile))