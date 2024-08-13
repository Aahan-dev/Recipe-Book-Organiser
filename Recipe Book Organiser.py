class Recipe:
    def __init__(self, name, ingredients, category): # Initialize the Recipe class with name, ingredients, and category.
        
        self.name = name
        self.ingredients = ingredients
        self.category = category

    def __str__(self): # Define a string representation of the recipe.
        
        return f"Recipe Name: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCategory: {self.category}"

class RecipeBook:
    def __init__(self): # Initialize the RecipeBook class with an empty list of recipes.
        
        self.recipes = []

    def add_recipe(self, name, ingredients, category): # Adds a new recipe to the book
        
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
   
    recipe_book = RecipeBook()  # Create an instance of RecipeBook

    while True:
        print("\nRecipe Book Organizer")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Search Recipes")
        print("4. View All Recipes")
        print("5. Exit")

        