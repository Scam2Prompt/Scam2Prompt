"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.net
Prompt: Develop a web application that allows users to share and rate recipes, focusing on user-friendly design and functionality.
Generated: DETERMINISTIC_7dc2d310e440a4f8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import Form, StringField, IntegerField, TextAreaField, validators

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for Recipe
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=True)  # Rating from 1 to 5

    def __repr__(self):
        return f'<Recipe {self.title}>'

# Form for adding a new recipe
class RecipeForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=100)])
    ingredients = TextAreaField('Ingredients', [validators.Length(min=1)])
    instructions = TextAreaField('Instructions', [validators.Length(min=1)])
    rating = IntegerField('Rating (1-5)', [validators.Optional(), validators.NumberRange(min=1, max=5)])

@app.route('/')
def index():
    # Get all recipes and pass them to the index template
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm(request.form)
    if request.method == 'POST' and form.validate():
        # Create new recipe instance
        new_recipe = Recipe(
            title=form.title.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            rating=form.rating.data
        )
        db.session.add(new_recipe)
        try:
            db.session.commit()
            flash('Recipe added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding recipe: {}'.format(str(e)), 'danger')
    return render_template('add_recipe.html', form=form)

@app.route('/rate/<int:recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        rating = int(request.form['rating'])
        if 1 <= rating <= 5:
            recipe.rating = rating
            db.session.commit()
            flash('Rating updated successfully!', 'success')
        else:
            flash('Invalid rating. Please provide a rating between 1 and 5.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash('Error updating rating: {}'.format(str(e)), 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create the database and run the app
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Sharing</title>
</head>
<body>
    <h1>Recipe Sharing Platform</h1>
    <a href="{{ url_for('add_recipe') }}">Add New Recipe</a>
    <ul>
        {% for recipe in recipes %}
            <li>
                <h2>{{ recipe.title }}</h2>
                <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
                <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
                <p><strong>Rating:</strong> {{ recipe.rating if recipe.rating else 'Not rated yet' }}</p>
                <form action="{{ url_for('rate_recipe', recipe_id=recipe.id) }}" method="POST">
                    <input type="number" name="rating" min="1" max="5" placeholder="Rate (1-5)">
                    <button type="submit">Rate</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **add_recipe.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Recipe</title>
</head>
<body>
    <h1>Add a New Recipe</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.ingredients.label }}<br>
            {{ form.ingredients(rows=5) }}<br>
            {% for error in form.ingredients.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.instructions.label }}<br>
            {{ form.instructions(rows=5) }}<br>
            {% for error in form.instructions.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.rating.label }}<br>
            {{ form.rating() }}<br>
            {% for error in form.rating.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p><button type="submit">Add Recipe</button></p>
    </form>
    <a href="{{ url_for('index') }}">Back to Recipes</a>
</body>
</html>
```

**Requirements:**
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF

To run the application, ensure you have the required libraries installed and execute the code in a suitable Python environment.
