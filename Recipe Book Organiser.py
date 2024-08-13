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

    