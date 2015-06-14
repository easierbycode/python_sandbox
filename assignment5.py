# imports
import assignment3
import assignment4

# Global Variables

houseScore  = 0
playerScore = 0


# Functions

def displayFinalResult():
  if playerScore > houseScore:
    print assignment3.green( '\n\tWINNER!\n' )
  else:
    print assignment3.red( '\n\tLOSE!\n' )

def displayRollResult():
  print '\n\tPLAYER\tHOUSE\t'
  print '\t{}\t{}'.format( playerScore, houseScore )

# Main Program

for diceRoll in range(1, 4):

  sum           = assignment4.results['addition result']
  craps         = sum in ( 7, 11 )
  doubles       = assignment4.diceValue1 == assignment4.diceValue2
  # use the modulo operator with an operand of 2 for determining whether the value is even
  valuesAreEven = doubles and assignment4.diceValue1 % 2 == 0
  valuesAreOdd  = doubles and assignment4.diceValue1 % 3 == 0

  print '\t.. player rolled {} and house rolled {}'.format( assignment4.diceValue1, assignment4.diceValue2 )

  if craps:
    print '\n\tCRAPS!!!'

  # If not CRAPS or doubles
  if not craps and not doubles:

    # and the total is less than 7
    if sum < 7:
      houseScore += 2

    # and the total is greater than 7
    else:
      playerScore += 2

  displayRollResult()

  if diceRoll < 3:
    # on reload, dice are displayed and variables are reloaded
    reload( assignment4 )

# outside of loop
displayFinalResult()

