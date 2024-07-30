import random
import os
import json
import re

from rich.console import Console
from rich.theme import Theme

from string import ascii_letters

console = Console()


# Function opens the dictionary file and gets words based on the input length
def get_word(category, length):
    # Open the JSON file
    file_name = ''
    data_name = ''
    match category:
        case 1:
            file_name = 'common.json'
            data_name = 'commonWords'
        case 2:
            file_name = 'nouns.json'
            data_name = 'nouns'
        case 3:
            file_name = 'adverbs.json'
            data_name = 'adverbs'
        case _:
            console.clear()
            console.print("Error")

    f = open(file_name)

    # Returns JSON object as a list
    data = json.load(f)

    word_list = []
    # Get words that are the length of chosen category
    for i in data[data_name]:
        if len(i) == length:
            word_list.append(i.upper())
    
    the_word = ""
    if len(word_list) > 0:        
        the_word = random.choice(word_list)

    # Close the file
    f.close()

    return the_word


# Function refreshes the page
def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:smiley: {headline} :smiley:[/]")


# Function prints the list of guesses
def show_guesses(guesses, word):
    len_word = len(word)
    for guess in guesses:
        styled_guess = [""] * len_word
        letters_left_in_word = word
        # First iteration places correct letters in the correct position and removes that letter from the list
        index = 0
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"   
                styled_guess[index] = f"[{style}]{letter}[/]"
                # Remove this letter from the word so that we do not highlight it as yellow when it was already green      
                letters_left_in_word = letters_left_in_word.replace(letter, '', 1)               
            index += 1

        # Second iteration places letters that are in the wrong places
        index = 0
        for letter, correct in zip(guess, word):
            if letter == correct:
                # Skip. This position has been filled
                index += 1
                continue
            elif letter in letters_left_in_word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"       
            styled_guess[index] = f"[{style}]{letter}[/]"
            index += 1
            # Remove this letter from the word so that we do not highlight it as yellow when it was already green      
            letters_left_in_word = letters_left_in_word.replace(letter, '', 1)
        
        # Print the word
        console.print("".join(styled_guess), justify="center")


# Main body of the game
def start_game(the_word):
    list_of_guesses = []
    refresh_page(headline=f"Guess {len(list_of_guesses) + 1}")

    num_of_guesses = 0
    max_guesses = 5
    while True:
        try:    
            console.print(f"\n[bold]{len(the_word)} letter word starting with {the_word[0]}[/]")
            console.print(f"\n[bold]You have {max_guesses-num_of_guesses} guesses left[/]")
            console.print(the_word)
            guess_word = str(input("Your guess: "))
            guess_word = guess_word.upper()
        except ValueError:
            console.clear()
            console.print("Invalid entry, please try again.")
            continue

        # Correct guess
        if guess_word == the_word:
            console.print(f"\n[bold white on green]Correct, the word is {the_word}![/]")
            break
        else:
            # Check word entered
            # Strip any non ascii_letters capital letters
            guess_word = re.sub(r'[^A-Z]', "", guess_word) 
            if guess_word[0] != the_word[0]:
                console.print(f"\n[bold white on red]Word must start with {the_word[0]}[/]")
            elif len(guess_word) != len(the_word):
                console.print(f"\n[bold white on red]Word must be {len(the_word)} letters[/]")
            else:
                num_of_guesses +=1
                if num_of_guesses >= max_guesses:
                    console.print(f"\n[bold white on red]You have exceeded number of guesses, the word is {the_word}[/]")
                    break
                else:
                    list_of_guesses.append(guess_word)
                    refresh_page(headline=f"Guess {len(list_of_guesses) + 1}")
                    show_guesses(list_of_guesses, the_word)


# Main
if __name__ == "__main__":

    # Types of categories
    categories = {1: "Common Words", 2:"Nouns", 3:"Adverbs"}
     
    # The GAME LOOP
    while True:
        # Print the game menu
        console.clear()
        console.rule("[bold blue] GUESS THE WORD! ")
        
        for key in categories:
            console.print("Press", key, "to select", categories[key])
        console.print("Press", len(categories)+1, "to quit")    
        console.print()
        
        # Handling the player category choice
        try:
            choice = int(input("Enter your category: "))
        except ValueError:
            console.clear()
            console.print("Invalid entry, please try again.")
            continue
 
        # Sanity checks for input
        if choice > len(categories)+1:
            console.clear()
            console.print("Invalid entry, please try again.")
            continue   
 
        # The EXIT choice   
        elif choice == len(categories)+1:
            console.print()
            console.print("Thank you for playing.")
            break
                 
        # Handle the player's number of letters choice
        try:
            num_of_letters = int(input("Enter the number of letters in word: "))
        except ValueError:
            console.clear()
            console.print("Invalid entry, please try again.")
            continue
 
        # The word randomly selected
        the_word = get_word(choice, num_of_letters)

        # Check that a word exist for the category
        if len(the_word) > 0:
            # Start game
            start_game(the_word)
        else:
            console.print(f"\n[bold white on red]There are no words in {categories[choice]} with {num_of_letters} letters[/]")

        break
