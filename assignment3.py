# Print Formatting
# Danelle Chapman
# Date : May 2015

# A program to print a receipt after gas is pumped

# Import statements
import datetime
from datetime import timedelta
import random

# Display the station name and location
# Date of the receipt is being issued/given
# Type of Gas
# Number of Gallons of Gas (a number that is displayed to three decimal places) {0:.3f}.format
# Cost per gallon (this should be a number that is formatted as US currency) ${1:,.2f}
# Total Cost (this should be a number that is formatted as US currency)  ${2:,.2f}

# Global variable declaration

today		= datetime.datetime.now()
oneWeekAgo	= today - timedelta(days=7)

trips		= [
	{
		"stationName": "Chevron",
		"stationLocation": "Peoria",
		"numberOfGallons": 13,
		"costPerGallon": 2.05,
		"fuelType": "UNLD",
		"date": today
	}, {
		"stationName": "QuikTrip",
		"stationLocation": 'Scottsdale',
		"date": oneWeekAgo,
		"fuelType": 'UNLD',
		"numberOfGallons": 12.5,
		"costPerGallon": 2.09
	}
]
# Functions

def red( str ):
	return ''.join( ['\x1b[31;1m', str, '\x1b[m'] )

def green( str ):
	return ''.join( ['\x1b[32;1m', str, '\x1b[m'] )

# Classes

# Main program

def printReceipt( t ):

	lines = [
		'\n\n',
		'-' * 30,
		"\t-= {} =-".format(t['stationName']),
		"{}, Arizona\n".format(t['stationLocation']),
		"DATE\t\tTIME\n"
		"{}\t\t{}\n".format(t['date'].strftime("%-m/%d/%y"), t['date'].strftime("%-H:%M %p")),
		"PUMP\tFUEL",
		"{}\t{}\n".format(random.randint(1, 10), t['fuelType']),
		"GALLONS\t$/G\tTOTAL",
		green("{0:.3f}\t${1:,.2f}\t${2:,.2f}\n".format(t['numberOfGallons'], t['costPerGallon'], t['numberOfGallons'] * t['costPerGallon'])),
		'\t' + red('Thank you!'.upper()) + '\n',
		'-' * 30
	]

	print( '\n'.join( lines ) )


for trip in trips:
	printReceipt( trip )