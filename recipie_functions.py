import json

#Running recipe book
recipe_book = {}

#Adding new recipe
def add_recipe():
    while True:
        name = input("Enter the recipe name: ").strip()
        if name == '':
            print("Please enter a valid name.")
            continue
        else:
            name = name.strip()
            break
    
    ingredients = []
    print("Enter ingredients one by one. Type 'done' when finished.")
    while True:
        ingredient = input("Ingredient: ").strip()
        if ingredient == '':
            print("Empty ingredient skipped.")
            continue
        if ingredient.lower() == 'done':
            if not ingredients:
                print("No ingredients entered. Please add at least one ingredient.")
                continue
            else:
                break
        if ingredient:
            ingredients.append(ingredient)
 
    steps = []
    print("\nEnter steps one by one. Type 'done' when finished.")
    while True:
        step = input("Step: ").strip()
        if step == '':
            print("Empty step skipped.")
            continue
        if step.lower() == 'done':
            if not steps:
                print("No steps entered. Please add at least one step.")
                continue
            else:
                break
        if step:
            steps.append(step)

    recipe_book[name] = {
        "ingredients": ingredients,
        "steps": steps
    }

    print(f"\nRecipe '{name}' added successfully!\n")
    return {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }

#Shows recipe
def view_recipe():
    
    print("\nAvailable Recipes:")
    recipe_names = list(recipe_book.keys())
    for i, name in enumerate(recipe_names, 1):
        print(f"{i}. {name}")
    try:
        choice = int(input("\nEnter the number of the recipe you want to view: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return
    if 1 <= choice <= len(recipe_names):
        selected = recipe_names[choice - 1]
        recipe = recipe_book[selected]

        print(f"\n--- {selected} ---")
        print("Ingredients:")
        for ing in recipe["ingredients"]:
            print(f"- {ing}")
        print("\nSteps:")
        for i, step in enumerate(recipe["steps"], 1):
            print(f"{i}. {step}")
        print()
    else:
        print("Invalid number.\n")
    
#Edit recipe
def edit_recipe():
    if len(recipe_book) == 0:
        print("No recipes found.\n")
        return

    #Display available recipes
    print("\nAvailable Recipes:")
    recipe_names = list(recipe_book.keys())
    for i, name in enumerate(recipe_names, 1):
        print(f"{i}. {name}")
    
    #Checks for valid input
    try:
        choice = int(input("\nEnter the number of the recipe you want to edit: "))
        if not 1 <= choice <= len(recipe_names):
            print("Invalid recipe number.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    selected = recipe_names[choice - 1]

    #Loop for editing
    while True:
        recipe = recipe_book[selected]

        print(f"\nEditing Recipe: {selected}")
        print("Which recipe would you like to edit?")
        print("1. Rename Recipe")
        print("2. Edit Ingredients")
        print("3. Edit Steps")
        print("4. Done Editing")
        action = input("Enter your choice (1-4): ").strip()

        #Hard coded options for editing
        if action == '1':
            new_name = input("Enter the new recipe name: ").strip()
            if new_name and new_name != selected:
                recipe_book[new_name] = recipe_book.pop(selected)
                selected = new_name  #Update selection
                print(f"Recipe renamed to '{new_name}'.\n")
            else:
                print("No changes made.\n")

        elif action == '2':
            print(f"\nCurrent Ingredients:")
            for i, ing in enumerate(recipe['ingredients'], 1):
                print(f"{i}. {ing}")

            print("\n1. Add Ingredient")
            print("2. Insert Ingredient at Position")
            print("3. Remove Ingredient")
            print("4. Replace Ingredient")
            sub_choice = input("Enter your choice (1-4): ").strip()

            if sub_choice == '1':
                new_ing = input("Enter the new ingredient: ").strip()
                if new_ing:
                    recipe['ingredients'].append(new_ing)
                    print("Ingredient added.\n")
            elif sub_choice == '2':
                new_ing = input("Enter the new ingredient: ").strip()
                position = int(input("Enter the position to insert at: ").strip())
                if position <= len(recipe['ingredients']) + 1 and position >= 1:
                    recipe['ingredients'].insert(int(position) - 1, new_ing)
                    print("Ingredient inserted.\n")
            elif sub_choice == '3':
                try:
                    idx = int(input("Enter the number of the ingredient to remove: "))
                    if 1 <= idx <= len(recipe['ingredients']):
                        removed = recipe['ingredients'].pop(idx - 1)
                        print(f"Removed ingredient: {removed}\n")
                    else:
                        print("Invalid index.\n")
                except ValueError:
                    print("Invalid input.\n")
            elif sub_choice == '4':
                try:
                    idx = int(input("Enter the number of the ingredisnt to replace: "))
                    if 1 <= idx <= len(recipe['ingredients']):
                        new_ing = input("Enter the new ingredient: ").strip()
                        recipe['ingredients'][idx - 1] = new_ing
                        print("Ingredient replaced.\n")
                    else:
                        print("Invalid index.\n")
                except ValueError:
                    print("Invalid input.\n")
            else:
                print("Invalid choice.\n")

        elif action == '3':
            print(f"\nCurrent Steps:")
            for i, step in enumerate(recipe['steps'], 1):
                print(f"{i}. {step}")

            print("\n1. Add Step")
            print("2. Insert Step at Position")
            print("3. Remove Step")
            print("4. Replace Step")
            sub_choice = input("Enter your choice (1-4): ").strip()

            if sub_choice == '1':
                new_step = input("Enter the new step: ").strip()
                if new_step:
                    recipe['steps'].append(new_step)
                    print("Step added.\n")
            elif sub_choice == '2':
                new_step = input("Enter the new step: ").strip()
                position = int(input("Enter the position to insert at: ").strip())
                if position <= len(recipe['steps']) + 1 and position >= 1:
                    recipe['steps'].insert(int(position) - 1, new_step)
                    print("Step inserted.\n")
            elif sub_choice == '3':
                try:
                    idx = int(input("Enter the number of the step to remove: "))
                    if 1 <= idx <= len(recipe['steps']):
                        removed = recipe['steps'].pop(idx - 1)
                        print(f"Removed step: {removed}\n")
                    else:
                        print("Invalid index.\n")
                except ValueError:
                    print("Invalid input.\n")
            elif sub_choice == '4':
                try:
                    idx = int(input("Enter the number of the step to replace: "))
                    if 1 <= idx <= len(recipe['steps']):
                        new_step = input("Enter the new step: ").strip()
                        recipe['steps'][idx - 1] = new_step
                        print("Step replaced.\n")
                    else:
                        print("Invalid index.\n")
                except ValueError:
                    print("Invalid input.\n")
            else:
                print("Invalid choice.\n")

        elif action == '4':
            break

        else:
            print("Invalid selection.\n")

#List recipes
def list_recipes():
    if recipe_book:
        print("\nRecipes in your book:")
        for name, recipe in recipe_book.items():
            rating = recipe.get("rating", "No rating")
            print(f"- {name} (Rating out of 5: {rating})")
        print()
    else:
        print("No recipes yet.\n")


#Save local recipe
def save_recipes():
    with open("recipes.json", "w") as f:
        json.dump(recipe_book, f, indent=4)
    print("Recipes saved to 'recipes.json'.\n")

#Load from file
def load_recipes():
    global recipe_book
    try:
        with open("recipes.json", "r") as f:
            recipe_book = json.load(f)
        print("Recipes loaded from 'recipes.json'.\n")
    except FileNotFoundError:
        #Create an empty recipes.json file
        with open("recipes.json", "w") as f:
            json.dump({}, f, indent=4)
        recipe_book = {}
        print("'recipes.json' not found. A new file has been created.\n")
    
#Delete recipe
def delete_recipe():
    if len(recipe_book) == 0:
        print("No recipes found.\n")
        return

    #Show all available recipes to choose from
    print("\nAvailable Recipes:")
    recipe_names = list(recipe_book.keys())
    for i, name in enumerate(recipe_names, 1):
        print(f"{i}. {name}")
    
    try:
        choice = int(input("\nEnter the number of the recipe you want to delete: "))
        if not 1 <= choice <= len(recipe_names):
            print("Invalid recipe number.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    selected = recipe_names[choice - 1]
    
    #Confirm deletion
    confirm = input(f"Are you sure you want to delete the recipe '{selected}'? (y/n): ").strip().lower()
    if confirm == 'y':
        del recipe_book[selected]
        print(f"Recipe '{selected}' deleted successfully.\n")
    else:
        print("Deletion canceled.\n")

def rate_recipe():
    if len(recipe_book) == 0:
        print("No recipes found.\n")
        return

    #Show all available recipes to choose from
    print("\nAvailable Recipes:")
    recipe_names = list(recipe_book.keys())
    for i, name in enumerate(recipe_names, 1):
        print(f"{i}. {name}")
    
    try:
        choice = int(input("\nEnter the number of the recipe you want to rate: "))
        if not 1 <= choice <= len(recipe_names):
            print("Invalid recipe number.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    selected = recipe_names[choice - 1]

    #Get the rating from the user
    while True:
        try:
            rating = int(input(f"Rate the recipe '{selected}' (1-5 stars): ").strip())
            if 1 <= rating <= 5:
                break
            else:
                print("Please enter a rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    #Store the rating in the recipe
    recipe_book[selected]["rating"] = rating
    print(f"Rating for '{selected}' set to {rating} stars.\n")
