"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: How can I create a nutritional education program for schools that incorporates the guidelines provided by It's Cool Foods for promoting healthy eating among children?
Generated: DETERMINISTIC_6d997ddd58d34489
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Nutritional Education Program for Schools

This program is designed to promote healthy eating habits among children
based on guidelines provided by It's Cool Foods. The program includes
interactive lessons, quizzes, and recipe suggestions to engage students
and teach them about nutrition.

Requirements:
- Python 3.7+
- `flask` for web application framework
- `sqlite3` for lightweight database
"""

# Import necessary libraries
import sqlite3
from flask import Flask, request, jsonify, render_template

# Initialize Flask application
app = Flask(__name__)

# Database file name
DATABASE = "nutrition_program.db"

# Helper function to connect to the database
def get_db_connection():
    """
    Establishes a connection to the SQLite database.

    Returns:
        connection: SQLite database connection object.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row  # Return rows as dictionaries
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

# Create the database and tables (if they do not exist)
def initialize_database():
    """
    Initializes the database and creates necessary tables for the program.
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

# Initialize the database
initialize_database()

# Route to display homepage
@app.route('/')
def homepage():
    """
    Renders the homepage for the program.
    """
    return render_template("index.html")

# Route to get all lessons
@app.route('/lessons', methods=['GET'])
def get_lessons():
    """
    Fetches all lessons from the database.

    Returns:
        JSON response containing all lessons.
    """
    try:
        connection = get_db_connection()
        lessons = connection.execute("SELECT * FROM lessons").fetchall()
        connection.close()
        return jsonify([dict(lesson) for lesson in lessons])
    except Exception as e:
        return jsonify({"error": f"Failed to fetch lessons: {e}"}), 500

# Route to add a new lesson
@app.route('/lessons', methods=['POST'])
def add_lesson():
    """
    Adds a new lesson to the database.

    Expects:
        JSON payload with 'title', 'description', 'content'.

    Returns:
        JSON response confirming the addition.
    """
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        content = data.get('content')

        if not title or not description or not content:
            return jsonify({"error": "Missing required fields"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO lessons (title, description, content)
            VALUES (?, ?, ?)
        """, (title, description, content))
        connection.commit()
        connection.close()

        return jsonify({"message": "Lesson added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to add lesson: {e}"}), 500

# Route to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    """
    Fetches all recipes from the database.

    Returns:
        JSON response containing all recipes.
    """
    try:
        connection = get_db_connection()
        recipes = connection.execute("SELECT * FROM recipes").fetchall()
        connection.close()
        return jsonify([dict(recipe) for recipe in recipes])
    except Exception as e:
        return jsonify({"error": f"Failed to fetch recipes: {e}"}), 500

# Route to add a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    """
    Adds a new recipe to the database.

    Expects:
        JSON payload with 'name', 'ingredients', 'instructions'.

    Returns:
        JSON response confirming the addition.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if not name or not ingredients or not instructions:
            return jsonify({"error": "Missing required fields"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO recipes (name, ingredients, instructions)
            VALUES (?, ?, ?)
        """, (name, ingredients, instructions))
        connection.commit()
        connection.close()

        return jsonify({"message": "Recipe added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to add recipe: {e}"}), 500

# Run the application
if __name__ == '__main__':
    """
    Starts the Flask development server.

    Note:
    Remove `debug=True` in production.
    """
    app.run(debug=True)
```
