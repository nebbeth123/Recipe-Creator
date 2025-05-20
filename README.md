# bcog200-final
# Recipe Manager

## Project Description
This is a simple terminal application that allows users to make their own recipes with ingredients, steps, and ratings. This program allows for simple storage of these recipes inside of a JSON file and it allows you to import already created recipe books into it. This allows for storage and quick access of recipes.

## Functions

### add_recipe()
- Prompts the user to enter a new recipe with a name, ingredients, and steps.
- Adds the information into a JSON file.

### view_recipe()
- Displays a numbered list of all recipe names and then prompts the user to select one.
- After the selection, it displays the recipe's ingredients and steps.

### edit_recipe()
- Allows the user to modify existing recipes, After choosing a recipe the user can:
- Rename the recipe or add, insert, remove, or replace ingredients and steps

## File Input Format
- Must be a JSON with name, followed by ingredients then steps then rating, all in strings.

## Use Cases
some use cases include serving as a easy way to enter information while getting a specific data structure as an output.
The program can take in user input in an order clearly stated to the person running the code and JSON files are necessary for the program to read.

## Group Members
Andy Chen (achen95)
