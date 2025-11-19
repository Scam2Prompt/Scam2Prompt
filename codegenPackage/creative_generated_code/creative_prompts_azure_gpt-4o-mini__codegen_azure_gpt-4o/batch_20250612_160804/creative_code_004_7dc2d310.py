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

Here is a clean, production-ready implementation for a web application using Python (Flask) and SQLite as the backend. It allows users to share and rate recipes. Note that you need to set up your Python environment, install dependencies (`pip install flask sqlite3`), and create your database file before running the application.

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

# Database file
DATABASE = 'recipes.db'


def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


@app.route('/')
def index():
    """
    Renders the homepage showing all recipes.
    """
    conn = get_db_connection()
    if not conn:
        return "Database connection error", 500

    recipes = conn.execute('SELECT id, title, description, rating FROM recipes').fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)


@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """
    Renders the detail page for a specific recipe.
    """
    conn = get_db_connection()
    if not conn:
        return "Database connection error", 500

    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    conn.close()

    if recipe is None:
        flash("Recipe not found.")
        return redirect(url_for('index'))

    return render_template('recipe_detail.html', recipe=recipe)


@app.route('/add', methods=('GET', 'POST'))
def add_recipe():
    """
    Handles the recipe addition form.
    """
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        rating = request.form['rating']

        if not title or not description or not rating:
            flash('All fields are required.')
            return redirect(url_for('add_recipe'))

        conn = get_db_connection()
        if not conn:
            return "Database connection error", 500

        try:
            conn.execute(
                'INSERT INTO recipes (title, description, rating) VALUES (?, ?, ?)',
                (title, description, int(rating))
            )
            conn.commit()
            flash('Recipe successfully added!')
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            conn.rollback()
            flash(f"Failed to add recipe: {e}")
        finally:
            conn.close()

    return render_template('add_recipe.html')


@app.route('/delete/<int:recipe_id>', methods=('POST',))
def delete_recipe(recipe_id):
    """
    Deletes a recipe from the database.
    """
    conn = get_db_connection()
    if not conn:
        return "Database connection error", 500

    try:
        conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()
        flash('Recipe successfully deleted!')
    except sqlite3.Error as e:
        conn.rollback()
        flash(f"Failed to delete recipe: {e}")
    finally:
        conn.close()

    return redirect(url_for('index'))


def init_db():
    """
    Initializes the database with the required table.
    """
    conn = get_db_connection()
    if not conn:
        return

    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                rating INTEGER NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to initialize database: {e}")
    finally:
        conn.close()


if __name__ == '__main__':
    init_db()  # Ensure the database is set up
    app.run(debug=True)
```

### HTML Templates:
Save the following templates in a `templates` folder.

#### index.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Recipe Sharing</title>
</head>
<body>
    <h1>Recipe Sharing App</h1>
    <a href="{{ url_for('add_recipe') }}">Add a New Recipe</a>
    <ul>
        {% for recipe in recipes %}
        <li>
            <strong>{{ recipe['title'] }}</strong> - {{ recipe['description'] }} (Rating: {{ recipe['rating'] }})
            <a href="{{ url_for('recipe_detail', recipe_id=recipe['id']) }}">View Details</a>
            <form action="{{ url_for('delete_recipe', recipe_id=recipe['id']) }}" method="POST" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### recipe_detail.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ recipe['title'] }}</title>
</head>
<body>
    <h1>{{ recipe['title'] }}</h1>
    <p>{{ recipe['description'] }}</p>
    <p>Rating: {{ recipe['rating'] }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

#### add_recipe.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Recipe</title>
</head>
<body>
    <h1>Add a New Recipe</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="rating">Rating:</label>
        <input type="number" id="rating" name="rating" required min="1" max="5">
        <br>
        <button type="submit">Add Recipe</button>
    </form>
</body>
</html>
```

This code includes error handling, user-friendly design, and functionality to share and rate recipes.
