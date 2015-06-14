# Craps!
# Danelle Chapman
# 6/12/15

# A program that plays craps

# Import statements

from random import randint 

# Global variables

houseScore     = 0
playerScore    = 0
diceValue1     = randint (1,6)
diceValue2     = randint (1,6)
total          = diceValue1 + diceValue2

# Functions

# https://docs.python.org/3/tutorial/controlflow.html

def displayFinalResult():
  if playerScore > houseScore:
    print("WINNER!")
  else:
    print("LOSE!")

def displayRollResult():
  print( "\n\tPLAYER\tHOUSE\t" )
  print( "\t{}\t{}".format( playerScore, houseScore ) )

def displayRollResult():
  print( "\n\tPLAYER\tHOUSE\t" )
  print( "\t{}\t{}".format( playerScore, houseScore ) )

# Classes

# Main program

diceValue1 = randint (1,6)
diceValue2 = randint (1,6)
   
craps   = total in (7,11)
doubles = diceValue1 == diceValue2
# Use the modulo operator with an operand of 2 for determining whether the value is even
valuesAreEven = doubles and diceValue1 % 2 == 0
valuesAreOdd  = doubles and not valuesAreEven

# If the sum of the dice is 7 or 11, display “CRAPS” and increment “house score by 2”
# If the dice are the same value (doubles) and the values are even increment the player score by 2 

print( ".. player rolls" {}.format( diceValue1, diceValue2 ) )

if craps:
    print( 'CRAPS!!!' )
    houseScore += 2

elif doubles:
    if valuesAreEven:
       playerScore += 2
    else:
       houseScore  += 2
       
# If not CRAPS or doubles
else:
    
# and the total is less than 7
  if total < 7:
    houseScore += 2
      
# and the total is greater than 7
  else:
    playerScore += 2

print("Player Score {} House Score {}".format(playerScore, houseScore))



# Determine the winner and display the results (with 3 rolls, there cannot be a tie!)


 
    
