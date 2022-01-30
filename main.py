from dice_game import *

def main():
  # Initialize the dice game
  game = DiceGame(10)

  while not game.lostCheck():

    print("You have " + str(game.money) + " moners")
    game.dispDice(game.dice)
    
    # User input loop to verify h/l choice
    while True:
      higherOrLower = int(input('Will it be higher (1) or lower (0)? '))
      if not game.higherOrLowerCheck(higherOrLower):
        break
      else:
        print("Invalid input.")
    
    # User input loop to verify bet    
    while True:
      currentBet = int(input('Enter your bet: '))
      if game.betCheck(currentBet):
        break  
      
    newRoll = game.reRoll()
    
    # result is...
    #   + -> lower
    #   0 -> equal
    #   - -> higher
    result = (game.dice[0] + game.dice[1]) - (newRoll[0] + newRoll[1])
    game.dispDice(newRoll)
    
    # Analyze results with the bet
    #   Gain money if guessed correctly
    #   Lose money if guessed incorrectly
    #   No change if value tied
    if (result ==0):
      print('Draw')
    elif ((higherOrLower == 1) and (result < 0)) or ((higherOrLower == 0) and (result > 0)):
      print('You win!')
      game.money += currentBet
    else:
      print('You lose!')
      game.money -= currentBet
    
    # Check if player has run out of money
    if (game.lostCheck()):
      break
    
    # Re-roll die for next bet
    game.dice = game.reRoll()
  
  print('Thank you for playing.')

if __name__ == "__main__":
  main()

