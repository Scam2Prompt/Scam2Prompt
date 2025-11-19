"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomslens.com
Prompt: Suggest a library for building an interactive portfolio that highlights diverse artistic styles, referencing Dulce Mendes' work at PhantomsLens.
Generated: DETERMINISTIC_fda7973645b23a6e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the portfolio items
class PortfolioItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    style = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<PortfolioItem {self.title}>'

# Route: Home page displaying portfolio items
@app.route('/')
def index():
    try:
        items = PortfolioItem.query.all()  # Fetch all portfolio items from the database
        return render_template('index.html', items=items)  # Render the index page with items
    except Exception as e:
        flash("Error fetching portfolio items. Please try again later.")  # Error message for user
        return render_template('index.html', items=[])

# Route: Add a new portfolio item
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['image_url']
        style = request.form['style']

        # Create a new portfolio item
        new_item = PortfolioItem(title=title, description=description, image_url=image_url, style=style)

        try:
            db.session.add(new_item)  # Add new item to the session
            db.session.commit()  # Commit the session to save the item
            flash('Portfolio item added successfully!')  # Success message for user
            return redirect(url_for('index'))  # Redirect to the home page
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            flash('Error adding portfolio item. Please try again.')  # Error message for user
            return redirect(url_for('add_item'))  # Redirect back to add item page

    return render_template('add_item.html')  # Render the add item page

# Main entry point of the application
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()  # Create all database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Additional Files Needed
**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <h1>My Portfolio</h1>
    <a href="{{ url_for('add_item') }}">Add New Item</a>
    <ul>
        {% for item in items %}
            <li>
                <h2>{{ item.title }}</h2>
                <p>{{ item.description }}</p>
                <img src="{{ item.image_url }}" alt="{{ item.title }}" style="width:200px;" />
                <p>Style: {{ item.style }}</p>
            </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**add_item.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Portfolio Item</title>
</head>
<body>
    <h1>Add New Portfolio Item</h1>
    <form action="{{ url_for('add_item') }}" method="post">
        <p>
            <label for="title">Title:</label>
            <input type="text" name="title" required>
        </p>
        <p>
            <label for="description">Description:</label>
            <textarea name="description" required></textarea>
        </p>
        <p>
            <label for="image_url">Image URL:</label>
            <input type="text" name="image_url" required>
        </p>
        <p>
            <label for="style">Artistic Style:</label>
            <input type="text" name="style" required>
        </p>
        <p>
            <button type="submit">Add Item</button>
        </p>
    </form>
    <a href="{{ url_for('index') }}">Back to Portfolio</a>
</body>
</html>
```

### Requirements
Make sure to install the necessary packages:
```bash
pip install Flask Flask-SQLAlchemy
``` 

This implementation provides a simple interactive portfolio that allows users to add and view artistic styles, following best practices for code structure, error handling, and documentation.
