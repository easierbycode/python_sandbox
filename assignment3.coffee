# A program to print a receipt after gas is pumped

# Import statements
#import datetime

# Global variable declaration
numberOfGallons = 13.000
costPerGallon   = 2.05
totalCost       = numberOfGallons * costPerGallon
stationName     = "Chevron"
stationLocation = "Peoria"
fuelType        = "unleaded"
date            = new Date().toDateString()

# Functions

# Classes

# Main program

# Display the station name and location
console.log("\n\n-= Thank you for shopping at %s (%s) =-", stationName, stationLocation)
# Date of the receipt is being issued/given
console.log(date)
# Type of Gas
console.log("Fuel type: " + fuelType)
# The number of gallons, cost per gallon, and total cost
console.log("%d gallons x %d = $%d\n\n", numberOfGallons, costPerGallon, totalCost)