import random
import os
import json
import re
import sys

from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt

from string import ascii_letters

console = Console()

class TileColour:   
    tileColour_green = "bold white on green"
    tileColour_yellow = "bold white on yellow"
    tileColour_grey = "white on #666666"
    tileColour_invalid = "dim"


class GuessTheWord:

    def display_main_menu(self):  
        """
        Displays the main menu
        """      
        # Types of categories
        categories = {1:"Common Words", 2:"Nouns", 3:"Adverbs"}
        self.refresh_page("GUESS THE WORD!")

        # The GAME LOOP
        while True:
            # Print the game menu   
            for key in categories:
                console.print("Press", key, "to select", categories[key])
            console.print("Press", len(categories)+1, "to quit\n")  
            
            # Handling the player category choice
            try:            
                choice = int(Prompt.ask("Enter your category"))
            except ValueError:
                console.print("\n[bold white on red]There was an error. Please select a choice from the following list.\n")
                continue
    
            # Sanity checks for input
            if choice > len(categories)+1:
                console.print("\n[bold white on red]There was an error. Please select a choice from the following list.\n")
                continue   
    
            # The EXIT choice   
            elif choice == len(categories)+1:
                console.print("\nThank you for playing.")
                break
                    
            # Handle the player's number of letters choice
            try:
                num_of_letters = int(Prompt.ask("Enter the number of letters in word"))
            except ValueError:
                console.print("\n[bold white on red]There was an error. Please enter a number.\n")
                continue
    
            # The word randomly selected
            the_word = self.get_word(choice, num_of_letters)

            # Check that a word exist for the category
            if len(the_word) > 0:
                # Start game
                self.start_game(the_word)
            else:
                console.print(f"\n[bold white on red]There are no words in {categories[choice]} with {num_of_letters} letters[/]\n")
                continue

            break


    def get_word(self, category, length):
        """
        Gets a random word from the dictionary given the category and length of word

        Parameters:
            category (int): Category the player had selected.
            length (int): Length of word.

        Returns:
            str: Random word from dictionary, empty string if word does not exist.
        """
        # Open the JSON file
        file_name = ''
        data_name = ''
        match category:
            case 1:
                file_name = 'dict_common.json'
                data_name = 'commonWords'
            case 2:
                file_name = 'dict_nouns.json'
                data_name = 'nouns'
            case 3:
                file_name = 'dict_adverbs.json'
                data_name = 'adverbs'
            case _:
                console.clear()
                console.print("Error")

        file = open(file_name)

        # Returns JSON object as a list
        data = json.load(file)

        word_list = []
        # Get words that are the length of chosen category
        for i in data[data_name]:
            if len(i) == length:
                word_list.append(i.upper())
        
        the_word = ""
        if len(word_list) > 0:        
            the_word = random.choice(word_list)

        # Close the file
        file.close()

        return the_word


    def refresh_page(self, headline): 
        """
        Clears and refreshes the page
        """     
        os.system('cls')
        console.clear()
        console.rule(f"[bold blue]:smiley: {headline} :smiley:[/]")


    def get_tile_sequence(self, guess, word):  
        """
        Helper function that returns the coloured patterns based on the given word
        If the letter is in the position, the tile will be green coloured
        If the letter exists in the word but in the incorrect location, the tile
        will be yellow
        Other letters will be coloured grey

        Parameters:
            guess (str): The guess word to compare.
            word (str): The correct word to be compared with.

        Returns:
            array: Tile pattern.
        """      
        len_word = len(word)
        styled_guess = [""] * len_word
        letters_left_in_word = word
        # First iteration places correct letters in the correct position and removes that letter from the list
        index = 0
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = TileColour.tileColour_green 
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
                style = TileColour.tileColour_yellow
            elif letter in ascii_letters:
                style = TileColour.tileColour_grey
            else:
                style = TileColour.tileColour_invalid     
            styled_guess[index] = f"[{style}]{letter}[/]"
            index += 1
            # Remove this letter from the word so that we do not highlight it as yellow when it was already green      
            letters_left_in_word = letters_left_in_word.replace(letter, '', 1)

        return styled_guess


    def start_game(self, the_word):
        """
        Main body of the game

        Parameters:
            the_word (str): Word to guess.
        """  
        list_of_guesses = []
        self.refresh_page(headline=f"Guess {len(list_of_guesses) + 1}")

        num_of_guesses = 0
        max_guesses = 5
        while True:
            try:    
                console.print(f"\n[bold]{len(the_word)} letter word starting with {the_word[0]}[/]")
                console.print(f"\n[bold]You have {max_guesses-num_of_guesses} guesses left[/]")
                guess_word = Prompt.ask("Your guess")
                guess_word = guess_word.upper()
                # Strip any non ascii_letters letters
                guess_word = re.sub(r'[^A-Z]', "", guess_word) 
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
                if len(guess_word) != len(the_word):
                    console.print(f"\n[bold white on red]Word must be {len(the_word)} letters[/]")
                elif guess_word[0] != the_word[0]:
                    console.print(f"\n[bold white on red]Word must start with {the_word[0]}[/]")
                else:
                    num_of_guesses +=1
                    if num_of_guesses >= max_guesses:
                        console.print(f"\n[bold white on red]You have exceeded number of guesses, the word is {the_word}[/]")
                        break
                    else:
                        list_of_guesses.append(guess_word)
                        self.refresh_page(headline=f"Guess {len(list_of_guesses) + 1}")                  
                        for guess in list_of_guesses:            
                            styled_guess = self.get_tile_sequence(guess, the_word)            
                            # Print the word
                            console.print("".join(styled_guess), justify="center")


# Main
if __name__ == "__main__":
    game_instance = GuessTheWord()
    game_instance.display_main_menu()

    
