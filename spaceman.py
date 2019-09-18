from random import choice


def print_green(input_string):
    print("\033[92m{}\033[00m" .format(input_string))


def print_red(input_string):
    print("\033[91m{}\033[00m" .format(input_string))


def load_word():
    possible_words = []

    with open("words_to_use.txt", "r") as f:
        for line in f:
            for word in line.split(" "):
                possible_words.append(word)

    return choice(possible_words)


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += (letter + " ")
        else:
            guessed_word += "_ "

    return guessed_word


def is_guess_in_word(guess, secret_word):
    return guess in secret_word


def print_welcome_message():
    print("-------------------------------------------------------------------------------------------------")
    print("Welcome! This is a game of Spaceman")
    print("I have thought of a word, and it is your job to guess it letter by letter in no particular order")
    print("You can guess the wrong letter at most 7 times, if you make 8 mistakes or more, I win! ")
    print("If you are able to guess the word within 7 strikes, then you win! Happy playing! ")
    print("--------------------------------------------------------------------------------------------------")


def get_input_letter(letters_guessed):
    letter_input = ""

    while True:
        letter_input = input("Please enter a letter: ")
        if validate_input(letter_input):
            # Checks if letter has been guessed already
            if letter_input in letters_guessed:
                print_red("You already entered " + letter_input + ". Try again!")
            else:
                break
        else:
            print_red("You entered an invalid letter, try again!")

    return letter_input.lower()


def validate_input(input):
    return len(input) == 1 and input.isalpha()


def test_is_guess_in_word():
    assert is_guess_in_word('a', ['f', 'a', 'l', 'l']) == True
    assert is_guess_in_word('b', ['b', 'o', 'b']) == True


def test_validate_input():
    assert validate_input('4') == False
    assert validate_input('A') == True
    assert validate_input('a') == True
    assert validate_input('') == False


def test_is_word_guessed():
    assert is_word_guessed(['a', 'b', 's'], ['a', 'b', 's']) == True
    assert is_word_guessed(['a', 'b', 's'], []) == False
    assert is_word_guessed(['a', 'b', 's'], ['a', 'b', 'd', 'n']) == False


def main():

    print_welcome_message()

    while True:
        # Some variables
        chosen_word = load_word()
        chosen_word_in_chars = list(chosen_word)
        length_of_chosen_word = len(chosen_word_in_chars)

        letters_guessed = []

        strikes_remaining = length_of_chosen_word

        # Game control
        while strikes_remaining > 0 and not is_word_guessed(chosen_word_in_chars, letters_guessed):
            print("The length of the word is: " + str(length_of_chosen_word) + " and you have " + str(strikes_remaining) + " strikes remaining")
            input_letter = get_input_letter(letters_guessed)

            letters_guessed.append(input_letter)

            if not is_guess_in_word(input_letter, chosen_word_in_chars):
                strikes_remaining -= 1
                print_red("Incorrect guess")

            print_green(get_guessed_word(chosen_word_in_chars, letters_guessed))

        if strikes_remaining == 0:
            print("I am very sorry, but you have lost :(")
            print_green("The word was: " + chosen_word)
        else:
            print(chosen_word + " is the word!! You have won!!!")

        # Ask user to play again
        if input("Please enter Y if you want to play again, any other character to quit: ").lower() == "y":
            print("------------------------------------------------")
            print("Ok! Get ready to play again! ")
            print("------------------------------------------------")
        else:
            print("Sad to see you go, hope to see you soon again!!")
            break


if __name__ == "__main__":
    main()
