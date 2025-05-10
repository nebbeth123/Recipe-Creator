import json

#running recipe book
recipe_book = {}

# adding new recipe
def add_recipe():
    name = input("Enter the recipe name: ").strip()

    
    ingredients = []
    print("Enter ingredients one by one.")
    while True:
        ingredient = input("Ingredient: ").strip()
        if ingredient:
            ingredients.append(ingredient)
        more = input("Add another ingredient? (y/n): ").strip().lower()
        if more != 'y':
            break

    
    steps = []
    print("\nEnter steps one by one.")
    while True:
        step = input("Step: ").strip()
        if step:
            steps.append(step)
        more = input("Add another step? (y/n): ").strip().lower()
        if more != 'y':
            break

    recipe_book[name] = {
        "ingredients": ingredients,
        "steps": steps
    }

    print("\nRecipe '{name}' added successfully!\n")

def view_recipe():
    
    print("\nAvailable Recipes:")
    recipe_names = list(recipe_book.keys())
    for i, name in enumerate(recipe_names, 1):
        print(f"{i}. {name}")

    
    choice = int(input("\nEnter the number of the recipe you want to view: "))
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
    


#list recipes
def list_recipes():
    if recipe_book:
        print("\nRecipes in your book:")
        for name in recipe_book:
            print(f"- {name}")
        print()
    else:
        print("No recipes yet.\n")



# save local recipe
def save_recipes():
    with open("recipes.json", "w") as f:
        json.dump(recipe_book, f, indent=4)
    print("Recipes saved to 'recipes.json'.\n")

# load from file
def load_recipes():
    global recipe_book
    
    with open("recipes.json", "r") as f:
        recipe_book = json.load(f)
    print("Recipes loaded from 'recipes.json'.\n")
    

def main():
    print("📘 Welcome to Your Recipe Book!")
    load_recipes()
    while True:
        print("Choose an option:")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. List Recipes")
        print("4. Save Recipes")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipe()
        elif choice == '3':
            list_recipes()
        elif choice == '4':
            save_recipes()
        elif choice == '5':
            save_recipes()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
