# A program to print a receipt after gas is pumped

# Import statements
import datetime

# Global variable declaration
numberOfGallons = 13.000
costPerGallon   = 2.05
totalCost       = numberOfGallons * costPerGallon
stationName     = "Chevron"
stationLocation = "Peoria"
fuelType        = "unleaded"
date            = datetime.datetime.now().strftime("%m/%d/%y")

# Functions

# Classes

# Main program

# Display the station name and location
print("\n\n-= Thank you for shopping at {} ({}) =-").format(stationName, stationLocation)
# Date of the receipt is being issued/given
print(date)
# Type of Gas
print("Fuel type: " + fuelType.capitalize())
# The number of gallons, cost per gallon, and total cost
print("{:.3f} gallons x {:.2f} = ${:.2f}\n\n").format(numberOfGallons, costPerGallon, totalCost)