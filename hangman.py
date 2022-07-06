import random
with open("wordlist.txt", "r") as file:
    all_words = file.read().split()

word = random.choice(all_words)
print(word)

master = [char for char in word]
guesses = ["_" for char in word]
repeats = []

guesses_remaining = 10
score = []

while guesses_remaining >= 0: 
    print(' '.join(guesses))
    user_guess = input('Guess a letter: ')
    guess = user_guess.lower()

    if guess.isalpha() == True and guess not in repeats and len(guess) == 1:
        if guess in master:
            print('Correct \n')
            guesses_remaining -= 1
            for item in master:
                if guess == item: 
                    guesses[master.index(guess)] = guess
                    master[master.index(guess)] = "-"
                    repeats.append(guess)
                    score.append(1)
        else:
            print('Incorrect \n')
            repeats.append(guess)
            guesses_remaining -= 1
    elif guess in repeats:
        print('You already guessed that letter \n')
    elif guess.isalpha() == False or len(guess) != 1:
        print('Please input a valid letter \n')

    if len(score) == len(master): 
        print('You win! The word was', word)
        break
    if guesses_remaining == 0:
        print('You lost! The word was', word)
        break
    