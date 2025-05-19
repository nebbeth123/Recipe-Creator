#This program will have instructions for what to do for you once you run it. Input data can be whatever you want it to be.
#Once you save your recipes, there will be a JSON file with all of your updated recipes.

import unittest
from unittest.mock import patch
from io import StringIO
import main 

class TestRecipeBook(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'Pasta',          #Recipe name
        'noodles',        #Ingredient
        'sauce',
        'done',
        'boil water',     #Step
        'cook pasta',
        'done'
    ])

    #Tests the add_recipe function to make sure it adds ingredients and steps correctly
    def test_add_recipe(self, mock_input):
        main.recipe_book.clear()
        result = main.add_recipe()
        self.assertEqual(result['name'], 'Pasta')
        self.assertIn('Pasta', main.recipe_book)
        self.assertEqual(main.recipe_book['Pasta']['ingredients'], ['noodles', 'sauce'])
        self.assertEqual(main.recipe_book['Pasta']['steps'], ['boil water', 'cook pasta'])

    @patch('builtins.input', side_effect=[
        '1'  #Select first recipe
    ])

    #Tests view recipe function to make sure it displays the correct recipe
    def test_view_recipe(self, mock_input):
        main.recipe_book.clear()
        main.recipe_book['Omelette'] = {
            "ingredients": ["eggs", "salt"],
            "steps": ["crack eggs", "fry eggs"]
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            main.view_recipe()
            output = mock_stdout.getvalue()
            self.assertIn("--- Omelette ---", output)
            self.assertIn("- eggs", output)
            self.assertIn("1. crack eggs", output)

    @patch('builtins.input', side_effect=[
        '1',  #Choose recipe
        '5'   #Give a 5-star rating
    ])

    #Tests the rate_recipe function to make sure it sets the rating correctly
    def test_rate_recipe(self, mock_input):
        main.recipe_book.clear()
        main.recipe_book['Toast'] = {
            "ingredients": ["bread"],
            "steps": ["toast bread"]
        }
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            main.rate_recipe()
            output = mock_stdout.getvalue()
            self.assertIn("Rating for 'Toast' set to 5 stars.", output)
            self.assertEqual(main.recipe_book['Toast']['rating'], 5)


if __name__ == '__main__':
    unittest.main()
