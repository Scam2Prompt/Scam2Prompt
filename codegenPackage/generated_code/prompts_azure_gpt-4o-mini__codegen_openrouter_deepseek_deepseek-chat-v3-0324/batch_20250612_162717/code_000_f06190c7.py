"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Generate a code snippet for a web application that showcases traditional Moroccan food recipes, incorporating unique dishes like couscous and Moroccan street food.
Generated: DETERMINISTIC_f06190c767f11ae0
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import HTTPException
import json
import os

app = Flask(__name__)

# Load recipe data from JSON file
def load_recipes():
    try:
        with open('data/recipes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "Recipe data not found"}, 404
    except json.JSONDecodeError:
        return {"error": "Invalid recipe data format"}, 500

# Route to display all recipes
@app.route('/')
def index():
    recipes = load_recipes()
    if isinstance(recipes, tuple):  # Error case
        return render_template('error.html', message=recipes[0]['error']), recipes[1]
    return render_template('index.html', recipes=recipes)

# Route to display a specific recipe
@app.route('/recipe/<string:recipe_id>')
def recipe(recipe_id):
    recipes = load_recipes()
    if isinstance(recipes, tuple):  # Error case
        return render_template('error.html', message=recipes[0]['error']), recipes[1]
    
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if not recipe:
        return render_template('error.html', message="Recipe not found"), 404
    return render_template('recipe.html', recipe=recipe)

# API endpoint to get all recipes
@app.route('/api/recipes')
def api_recipes():
    recipes = load_recipes()
    if isinstance(recipes, tuple):  # Error case
        return jsonify(recipes[0]), recipes[1]
    return jsonify(recipes)

# API endpoint to get a specific recipe
@app.route('/api/recipe/<string:recipe_id>')
def api_recipe(recipe_id):
    recipes = load_recipes()
    if isinstance(recipes, tuple):  # Error case
        return jsonify(recipes[0]), recipes[1]
    
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipe)

# Error handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error.html', message=e.description), e.code

if __name__ == '__main__':
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Create sample recipe data if it doesn't exist
    if not os.path.exists('data/recipes.json'):
        sample_recipes = [
            {
                "id": "couscous",
                "name": "Moroccan Couscous",
                "description": "Traditional Moroccan couscous with vegetables and spices.",
                "ingredients": ["couscous", "carrots", "zucchini", "chickpeas", "onions", "spices"],
                "steps": ["Prepare vegetables", "Steam couscous", "Combine and simmer"]
            },
            {
                "id": "tagine",
                "name": "Chicken Tagine",
                "description": "Classic Moroccan tagine with chicken, olives, and preserved lemons.",
                "ingredients": ["chicken", "olives", "preserved lemons", "onions", "spices"],
                "steps": ["Brown chicken", "Add ingredients", "Slow cook in tagine"]
            },
            {
                "id": "msemen",
                "name": "Msemen",
                "description": "Moroccan square-shaped flatbread, a popular street food.",
                "ingredients": ["flour", "semolina", "water", "oil", "salt"],
                "steps": ["Mix dough", "Fold layers", "Cook on griddle"]
            }
        ]
        with open('data/recipes.json', 'w', encoding='utf-8') as f:
            json.dump(sample_recipes, f, ensure_ascii=False, indent=2)
    
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moroccan Recipes</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .recipe-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 20px; border-radius: 5px; }
        .recipe-card h2 { color: #c7254e; margin-top: 0; }
    </style>
</head>
<body>
    <h1>Traditional Moroccan Recipes</h1>
    {% for recipe in recipes %}
    <div class="recipe-card">
        <h2><a href="/recipe/{{ recipe.id }}">{{ recipe.name }}</a></h2>
        <p>{{ recipe.description }}</p>
    </div>
    {% endfor %}
</body>
</html>
```

```html
<!-- templates/recipe.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ recipe.name }} - Moroccan Recipes</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #c7254e; }
        .ingredients, .steps { margin-bottom: 20px; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>
    <h1>{{ recipe.name }}</h1>
    <p>{{ recipe.description }}</p>
    
    <div class="ingredients">
        <h2>Ingredients</h2>
        <ul>
            {% for ingredient in recipe.ingredients %}
            <li>{{ ingredient }}</li>
            {% endfor %}
        </ul>
    </div>
    
    <div class="steps">
        <h2>Preparation Steps</h2>
        <ol>
            {% for step in recipe.steps %}
            <li>{{ step }}</li>
            {% endfor %}
        </ol>
    </div>
    
    <a href="/">Back to all recipes</a>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - Moroccan Recipes</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .error { color: #d9534f; }
    </style>
</head>
<body>
    <h1 class="error">Error</h1>
    <p>{{ message }}</p>
    <a href="/">Back to home</a>
</body>
</html>
```
