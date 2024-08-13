from guess import GuessTheWord
from guess import TileColour

import unittest

class TestClass(unittest.TestCase):
    def test_get_word_function_common(self):
        """Test for the get word function - common words"""
        game_instance = GuessTheWord()
        # Testing words in Common Words
        result = game_instance.get_word(1, 2)
        self.assertEqual(len(result), 2)
        result = game_instance.get_word(1, 10)
        self.assertEqual(len(result), 10)
        
    def test_get_word_function_nouns(self):
        """Test for the get word function - nouns"""
        game_instance = GuessTheWord()
        # Testing words in Nouns 
        result = game_instance.get_word(2, 2)
        self.assertEqual(len(result), 0) # No 2 letter words in nouns
        
    def test_get_word_function_adverbs(self):
        """Test for the get word function - adverbs"""
        game_instance = GuessTheWord()
        # Testing words in Advebs
        result = game_instance.get_word(3, 2)
        self.assertEqual(len(result), 0) # No 2 letter words in nouns
        
    def test_tile_pattern_one_letter(self):
        """Test for the tile sequence function - 1 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("A", "A")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        
    def test_tile_pattern_two_letter(self):
        """Test for the tile sequence function - 2 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("CD", "CA")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        
    def test_tile_pattern_three_letter_one(self):
        """Test for the tile sequence function - 3 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("CAT", "TAC")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        
    def test_tile_pattern_three_letter_two(self):
        """Test for the tile sequence function - 3 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("CAT", "TCA")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        
    def test_tile_pattern_six_letter_one(self):
        """Test for the tile sequence function - 6 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("LITTLE", "LOOSEN")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[3].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[4].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[5].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        
    def test_tile_pattern_six_letter_two(self):
        """Test for the tile sequence function - 6 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("BROKEN", "BOTTOM")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[3].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[4].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[5].split('[')[1].split(']')[0], TileColour.tileColour_grey)

    def test_tile_pattern_ten_letter_one(self):
        """Test for the tile sequence function - 10 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("PHOTOGRAPH", "PHOOORGABH")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[3].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[4].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[5].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[6].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[7].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[8].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[9].split('[')[1].split(']')[0], TileColour.tileColour_green)

    def test_tile_pattern_ten_letter_two(self):
        """Test for the tile sequence function - 10 letter word"""
        game_instance = GuessTheWord()
        pattern = game_instance.get_tile_sequence("TANGERINES", "TELEVISION")
        self.assertEqual(pattern[0].split('[')[1].split(']')[0], TileColour.tileColour_green)
        self.assertEqual(pattern[1].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[2].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[3].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[4].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[5].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[6].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[7].split('[')[1].split(']')[0], TileColour.tileColour_grey)
        self.assertEqual(pattern[8].split('[')[1].split(']')[0], TileColour.tileColour_yellow)
        self.assertEqual(pattern[9].split('[')[1].split(']')[0], TileColour.tileColour_yellow)

if __name__ == "__main__":
    unittest.main()