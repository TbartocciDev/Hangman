import sys

sentence = sys.argv[1] 

incorrect_guesses = 0
hidden_sentence = ""

guessed_characters =[]
correct_guesses = []
incorrect_characters = []

correct_letters = []

for each_new_letter in sentence:
    if correct_letters.__contains__(each_new_letter.lower()):
        print("")
    elif each_new_letter == " ":
        print("")
    else:
        correct_letters.append(each_new_letter)


def win_game():
    print("\n---------------------------\nCongratulations! You win!\n---------------------------\n")
    print("The sentence was:\n\n" + sentence)
    exit()

def lose_game():
    print("\n---------------------------\nYou lose, play again!\n---------------------------\n")
    print("The sentence was:\n\n" + sentence)
    exit()

def check_for_multiple(some_letter):
    if guessed_characters.__contains__(some_letter):
        print("\nYou have already guessed this.\n")
        return True
    else:
        return False

def update_game(new_letter):

    if len(correct_guesses) == len(correct_letters):
        win_game()

    new_sentence = ""

    for character in sentence:
        if correct_guesses.__contains__(character.upper()):
            new_sentence += str(character + " ")
        elif character == " ":
            new_sentence += "  "
        else:
            new_sentence += "_ "

    
    print_current_figure(len(incorrect_characters))

    print(new_sentence)
    print("")



def print_current_figure(guesses):
    print("Current Figure:\n")

    if guesses == 0:
        print("     _________")
        print("             |")
        print("             |")
        print("             |")
        print("            _|_")
    elif guesses == 1:
        print("     _________")
        print("      O      |")
        print("             |")
        print("             |")
        print("            _|_")
    elif guesses == 2:
        print("     _________")
        print("      O      |")
        print("      |      |")
        print("             |")
        print("            _|_")
    elif guesses == 3:
        print("     _________")
        print("      O      |")
        print("      |      |")
        print("     /       |")
        print("            _|_")
    elif guesses == 4:
        print("     _________")
        print("      O      |")
        print("      |      |")
        print("     / \\     |")
        print("            _|_")
    elif guesses == 5:
        print("     _________")
        print("      O      |")
        print("     /|      |")
        print("     / \\     |")
        print("            _|_")
    elif guesses == 6:
        print("     _________")
        print("      O      |")
        print("     /|\\     |")
        print("     / \\     |")
        print("            _|_")

        lose_game()
    print("")




def ask_for_guess():

    # print("\n-----------------------------------------------------")
    
    # print_current_figure(len(incorrect_characters))
    if len(guessed_characters) == 0:
        print("")
    else:
        print("Guessed letters or words:")
        print(guessed_characters)
        print("\n-----------------------------------------------------")
        print("")

    print("")

    some_guess = input("...Guess a letter or the sentence...\n")

    if some_guess == "exit".lower():
        print("exiting...")
        exit()

    if check_for_multiple(some_guess):
        ask_for_guess()
    else:
        guessed_characters.append(some_guess)
        if sentence.lower() == some_guess.lower():
            win_game()
        elif sentence.lower().__contains__(some_guess.lower()):
            if len(some_guess) == 1:
                print("\nYou found a letter!\n")
                correct_guesses.append(some_guess.upper())           
                update_game(some_guess)
                ask_for_guess()
                
            else:
                print("\nThat sentence is incorrect.")
                incorrect_characters.append(some_guess)
                update_game(some_guess)
                ask_for_guess()

        else:
            print("\nThis is an incorrect character, try again!")
            incorrect_characters.append(some_guess)
            update_game(some_guess)
            ask_for_guess()
    
for num in range(0,15):
    print("")

for each_character in sentence:
    if each_character == " ":
        hidden_sentence += "  "
    else:
        hidden_sentence += "_ "

print("\nWelcome to hang man!, your word/sentence is:")
print(hidden_sentence)
print("\nBegin!")
ask_for_guess()
