from recipe_functions import (    
    add_recipe,
    view_recipe,
    list_recipes,
    edit_recipe,
    save_recipes,
    load_recipes,
    delete_recipe,
    rate_recipe)

def main():
    print("📘 Welcome to Your Recipe Book!")
    load_recipes()
    while True:
        print("Choose an option:")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. List Recipes")
        print("4. Edit Recipes")
        print("5. Save Recipes")
        print("6. Delete Recipe")
        print("7. Rate Recipe")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipe()
        elif choice == '3':
            list_recipes()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            save_recipes()
        elif choice == '6':
            delete_recipe()
        elif choice == '7':
            rate_recipe()
        elif choice == '8':
            save_recipes()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
