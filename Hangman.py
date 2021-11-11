# sequence of stage in a list
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# some random words 
word_list = ["banana", "pear", "strawberry", "watermelon", "mango", "durian", "grapes", "orange", "kiwi", "lemon"]

# randomly selected the word
import random
word_list = word_list[random.randint(0,len(word_list)-1)] # supposed to use random.choice() but nah

# for testing puposes
print("Hint: its fruits..goodluck..hehe..")

# storing and displaying the "_" (blankspace) based on length of word
display = []
for idx in range(len(word_list)):
  display+= "_"
print(display)
win_lose = False

# number of user life
num_life = len(stages)

# the main loop for the game
while not win_lose: # will stop if number of life =0

  #display total/remaining life
  print(f"Your number of live is {num_life}")

  # user input
  guess = input("Guess the letter hehe: ").lower()

  # looping to check/replace the letter based on list index
  for idx in range(len(word_list)):
      if list(word_list)[idx] == guess:
        display[idx] = guess
  # hehehe ... the penalty give to the user when giving the wrong letter      
  if guess not in word_list:
      num_life -= 1
      print(stages[num_life])

  # displaying the remaining blankspace
  print(display)

  if "_" not in display:
    state = "win"
    win_lose = True
  elif num_life == 0:
      win_lose = True
      state = "lose"

print(f"You {state}!")
