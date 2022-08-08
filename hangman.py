import random
with open("wordlist.txt", "r") as file:
    all_words = file.read().split()

# initialize variables
word = None
guess = None
guesses = []
guessed = []
incorrects = []
hanging = []

# change picture
def update_man(wrongs): 
  if wrongs == 1:
    hanging[2] = " |    O"
    hanging[3] = " |    |"
  elif wrongs == 2:
    hanging[3] = " |   \|"
  elif wrongs == 3:
    hanging[3] = " |   \|/"
  elif wrongs == 4:
    hanging[4] = " |    |"
  elif wrongs == 5:
    hanging[5] = " |   /  "
  elif wrongs == 6:
    hanging[5] = " |   / \ "

# clear game
def generate_blank(): 
  global guesses
  global guessed
  global word
  global hanging
  global incorrects

  hanging = [
        "_______",
        " |    |",
        " |",
        " |",
        " |",
        " |",
        " |",
        "_|_____"
    ]
  
  word = random.choice(all_words)
  guesses = []
  guessed = []
  incorrects = []
  for char in word:
    guesses.append("_")

# ask for user to guess
def prompt_guess():
  global guess
  guess = (input("guess a letter: ")).lower()
  return guess

# update blanks
def update_guess():
  global word
  global guesses
  global guessed
  global guess
  global incorrects

  guessed.append(guess)
  if guess in word:
    print("ya got one!")
    for i in range(0, len(word)):
      if guess == word[i]:
        guesses[i] = guess
  else:
    incorrects.append("X")
    update_man(len(incorrects))
    print("WRONG")


# check if guess is valid
def validate_guess():
  global guess
  global guessed

  if guess.isalpha():
    if len(guess) != 1:
      print("ONE letter please")
    elif guess in guessed:
      print("you already guessed that silly goose")
    else:
      update_guess()
  else:
    print("um that's not a letter")


# play one round
def play_round():
  global incorrects
  global guesses
  
  update_man(0)
  generate_blank()

  while len(incorrects) <= 5:
    if "_" not in guesses:
      break
    print(*hanging, sep="\n")
    print("\nwhat's this word? ", *guesses, sep="")
    prompt_guess()
    validate_guess()

  if "_" in guesses:
    print(*hanging, sep="\n")
    print("\naaaaaand he died...\ncus the word was", word, "\n")
  else:
    print("\nyou saved him !!\n")

# main
while True:
  choice = input("want to hang a man? i mean, play hangman? (y/n) ")
  if choice.lower() == "y":
    play_round()
  else:
    print("okay. fine. see if i care!\n")
    break
