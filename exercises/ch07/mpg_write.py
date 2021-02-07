100#!/usr/bin/env python3

import csv

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def store_data(trip, trips):
    trips.append(trip)

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()
    trips = [["Distance", "Gallons", "MPG"]]

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        #create a list called "trip" from miles_driven, gallons_used and mpg
        trip = [str(miles_driven), str(gallons_used), str(mpg)]

        #call add to list function and pass the list
        store_data(trip, trips)
        
        more = input("More entries? (y or n): ")
    
    #store data to csv file upon exit
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)
    print("Bye")

if __name__ == "__main__":
    main()

