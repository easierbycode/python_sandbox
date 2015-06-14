# Program generates two random dice values between 1 and 6 (one value for each dice).   
# Program displays the values of both dice. 
# Program displays the values of multiplication, division, addition, subtraction, and average of the dice in a nicely formatted display.

# Import Statements

from random import randint

# Global variable declaration

asciiArt = {
  'dice1' : '''
        .-------.
       /       /|
      /_______/ |
      |       | |
      |   o   | /
      |       |/
      '-------' ''',
  'dice2' : '''
        .-------.
       /       /|
      /_______/ |
      | o     | |
      |       | /
      |     o |/
      '-------' ''',
  'dice3' : '''
        .-------.
       /       /|
      /_______/ |
      | o     | |
      |   o   | /
      |     o |/
      '-------' ''',
  'dice4' : '''
        .-------.
       /       /|
      /_______/ |
      | o   o | |
      |       | /
      | o   o |/
      '-------' ''',
  'dice5' : '''
        .-------.
       /       /|
      /_______/ |
      | o   o | |
      |   o   | /
      | o   o |/
      '-------' ''',
  'dice6' : '''
        .-------.
       /       /|
      /_______/ |
      | o o o | |
      | o o o | /
      | o o o |/
      '-------' '''
}

# Functions

def generateTwoRandomDiceValues( max ):
  return [ randint( 1, max ), randint( 1, max ) ]

# Classes

# Main program

[ diceValue1, diceValue2 ] = generateTwoRandomDiceValues( 6 )

results = {
  'multiplication result'  : diceValue1 * diceValue2,
  'division result'        : diceValue1 / diceValue2,
  'addition result'        : diceValue1 + diceValue2,
  'subtraction result'     : diceValue1 - diceValue2,
  'average result'         : sum( [diceValue1, diceValue2] ) / 2
}

print( asciiArt['dice' + str( diceValue1 )] );
print( asciiArt['dice' + str( diceValue2 )] );

# for k, v in results.iteritems():
#   whitespace = ' ' * (23 - len( k ))
#   print( '{}{}: {}' ).format( k, whitespace, v )