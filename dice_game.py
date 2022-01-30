from qrng import *

class DiceGame:
  #
  # Set the initial money and initial dice roll
  #
  def __init__ (self, money):
    self.money = money
    self.dice = self.reRoll()
  
  #
  # Checks if you able to make the bet.
  #
  def betCheck(self, bet):
    if (bet > self.money):
      print('You are Broke')
    elif (bet < 0):
      print('Invalid bet')
      return False
    return True

  #
  # Checks if you have any money left.
  #
  def lostCheck(self):
    return self.money <= 0

  #
  # Roll two die using qubits to generate two truly random ints.
  #
  def reRoll(self):
      dice1 = qrng(5) + 1
      dice2 = qrng(5) + 1
      return (dice1, dice2)

  #
  # Parses user input to only choose one of the two die.
  #
  def higherOrLowerCheck(self, choice):
      return (choice != 1) and (choice != 0)

  #
  # Output the rolls from rng.
  #
  def dispDice(self, dice):
      print('Dice 1: ' + str(dice[0]) + ', Dice 2: ' + str(dice[1]))
      print('Total: ' + str(dice[0] + dice[1]))