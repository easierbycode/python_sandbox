# Import Statements

import assignment4


# Global variable declaration

houseScore  = 0
playerScore = 0


# Functions

def rollDice():
  reload( assignment4 )

def displayDiceValuesAndScores():
  # displaying text value print out of dice that are displayed
  print( '\n\t.. rolled {} and {}'.format( assignment4.diceValue1, assignment4.diceValue2 ) )
  # TODO: display score ( probably not needed, but let's debug )
  # print( '\tPLAYER\tHOUSE' )
  # print( '\t{}\t{}'.format( playerScore, houseScore ) )
  if playerScore > houseScore:
    print( '\t... player won round' )
  else:
    print( '\t... house won round' )

def displayResults():
  if playerScore > houseScore:
    print '\n\tYOU WIN!\n'
  else:
    print '\n\tYOU LOSE!\n'


# Main program

# roll the pair of dice three times
for diceRoll in range( 1, 4 ):

  doubles       = assignment4.diceValue1 == assignment4.diceValue2  
  sumOfTheDice  = assignment4.results['addition result']
  craps         = sumOfTheDice in ( 7, 11 )
  valuesAreEven = doubles and assignment4.diceValue1 % 2 == 0
  valuesAreOdd  = doubles and assignment4.diceValue1 % 3 == 0
  
  if craps:
    print '\n\t-= CRAPS =-'
    houseScore  += 2

  if doubles and valuesAreEven:
    playerScore += 2

  if doubles and valuesAreOdd:
    houseScore  += 2

  if not craps and not doubles:
    if sumOfTheDice < 7:
      houseScore  += 2
    else:
      playerScore += 2

  displayDiceValuesAndScores()
  
  if diceRoll < 3:
    rollDice()

displayResults()