#!/usr/bin/env python3

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

def write_trips(trips):
    #write data from trips to csv named trips.csv
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def read_trips():
    #reads data from trips.csv file and returns a list names trips
    trips = []
    with open("trips.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips

def list_trips(trips):
    for trip in trips:
        print(trip)


def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()
    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        trip = [str(miles_driven), str(gallons_used), str(mpg)]
        trips.append(trip)
        list_trips(trips)
        print()
        print()
        
        more = input("More entries? (y or n): ")
    
    write_trips(trips)
    print("Bye")

if __name__ == "__main__":
    main()

