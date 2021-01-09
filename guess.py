import random
from os import system

print("\n\nWelcome To The Guessing Game!\n")

word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)

lives = len(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    system('\ncls')
    print("\nWelcome To The Gussing Game!\n")
    

    if guess in display:
        print(f"\nYou have already guessed {guess}")

    for position in range(0,len(chosen_word)): 
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print("\nLetter not in word")
        lives -= 1
        print("\nlives left",lives)
        if lives == 0:
            end_of_game = True
            print("\nYou lose")

    if "_" not in display:
        end_of_game = True
        print('\nYou win')
