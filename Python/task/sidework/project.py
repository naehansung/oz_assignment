import random

def get_selections(): 
  player_selection = input("Enter a selection(rock, paper, scissors: )")
  options = ["rock","paper","scissors"]
  computer_selection = random.choice(options)
  selections = {"player": player_selection, "computer": computer_selection}
  return selections

selections = get_selections()
print(selections)
