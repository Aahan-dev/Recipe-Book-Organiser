class Recipe:
    def __init__(self, name, ingredients, category): # Innitialize the Recipe class with name, ingredients, and category.
        
        self.name = name
        self.ingredients = ingredients
        self.category = category

    def __str__(self): # Define a stringg representation of the recipe.
        
        return f"Recipe Name: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCategory: {self.category}"

class RecipeBook:
    def __init__(self): # Initialize the RecipeBook class with an empty list of recipes.
        
        self.recipes = []

    def add_recipe(self, name, ingredients, category): # Aadds a new recipe to the book
        
        recipe = Recipe(name, ingredients, category) # Asks for the specifics of the recipe
        self.recipes.append(recipe) # Adds a new recipe to the book
        print(f"Recipe '{name}' added successfully.")

    def edit_recipe(self, name, new_name=None, new_ingredients=None, new_category=None): # Allows to edit a recipe
        
        for recipe in self.recipes:
            if recipe.name == name:
                if new_name:
                    recipe.name = new_name
                if new_ingredients:
                    recipe.ingredients = new_ingredients
                if new_category:
                    recipe.category = new_category
                print(f"Recipe '{name}' updated successfully.")
                return
        print(f"Recipe '{name}' not found.")

    def search_recipes(self, query): # Searches for a recipe
       
        found_recipes = [recipe for recipe in self.recipes if query in recipe.ingredients or query in recipe.category]
        if found_recipes:
            print("\nFound Recipes:")
            for recipe in found_recipes:
                print(recipe)
        else:
            print("No recipes found.")

    def view_recipes(self): # Displays all recipes
       
        if not self.recipes:
            print("No recipes available.")
        else:
            print("\nAll Recipes:")
            for recipe in self.recipes:
                print(recipe)

def main(): # Main function to run the recipe book organizer
   
    recipe_book = RecipeBook()  # Create aan instance of RecipeBook

    while True:
        print("\nRecipe Book Organizer")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Search Recipes")
        print("4. View All Recipes")
        print("5. Exit")

        choice = input("Choose an option: ")


        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            category = input("Enter category: ")
            recipe_book.add_recipe(name, [ingredient.strip() for ingredient in ingredients], category)


        elif choice == '2':
            name = input("Enter the recipe name to edit: ")
            new_name = input("Enter new recipe name (leave blank to keep unchanged): ")
            new_ingredients = input("Enter new ingredients (comma-separated, leave blank to keep unchanged): ")
            new_category = input("Enter new category (leave blank to keep unchanged): ")
            recipe_book.edit_recipe(name, new_name if new_name else None,
                                    [ingredient.strip() for ingredient in new_ingredients.split(',')] if new_ingredients else None,
                                    new_category if new_category else None)

        elif choice == '3':
            query = input("Enter ingredient or category to search: ")
            recipe_book.search_recipes(query)


        elif choice == '4':
            recipe_book.view_recipes()

        elif choice == '5':
            print("Exiting the Recipe Book application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()  # Run the mainn function