from random import choice
import re


def load_word():
    possible_words = []

    with open("/Users/andreynovichkov/Desktop/Make-School/Term-1/CS1-1/9.3/spaceman/words_to_use.txt", "r") as f:
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
    print("Welcome! This is a game of Spaceman")
    print("I have thought of a word, and it is your job to guess it letter by letter in no particular order")
    print("You can guess the wrong letter at most 7 times, if you make 8 mistakes or more, I win! ")
    print("If you are able to guess the word within 7 strikes, then you win! Happy playing! ")
    print("--------------------------------------------------------------------------------")


def get_input_letter():
    letter_input = ""

    while True:
        letter_input = input("Please enter a letter: ")
        if validate_input(letter_input):
            break
        else:
            print("You entered an invalid letter, try again!")

    return letter_input.lower()


def validate_input(input):
    return len(input) == 1 and input.isalpha()


def main():
    chosen_word = load_word()
    chosen_word_in_chars = list(chosen_word)
    length_of_chosen_word = len(chosen_word_in_chars)

    letters_guessed = []

    strikes_remaining = 7

    print_welcome_message()

    while strikes_remaining > 0 and not is_word_guessed(chosen_word_in_chars, letters_guessed):
        print("The length of the word is: " + str(length_of_chosen_word) + " and you have " + str(strikes_remaining) + " strikes remaining")
        input_letter = get_input_letter()
        letters_guessed.append(input_letter)

        if not is_guess_in_word(input_letter, chosen_word_in_chars):
            strikes_remaining -= 1
            print("Incorrect guess")

        print(get_guessed_word(chosen_word_in_chars, letters_guessed))

    if strikes_remaining == 0:
        print("I am very sorry, but you have lost :(")
        print("The word was: " + chosen_word)
    else:
        print(chosen_word + " is the word!! You have won!!!")


if __name__ == "__main__":
    main()
