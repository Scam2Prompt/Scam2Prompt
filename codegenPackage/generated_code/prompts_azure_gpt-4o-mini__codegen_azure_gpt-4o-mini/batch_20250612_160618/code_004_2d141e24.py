"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Develop a web application that showcases success stories of women leaders from Sauti Kenya, highlighting their contributions to community advocacy and sustainability.
Generated: DETERMINISTIC_2d141e24bd0b2184
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///success_stories.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the database model for success stories
class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contribution = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SuccessStory {self.name}>'

# Route for the home page
@app.route('/')
def index():
    stories = SuccessStory.query.all()  # Fetch all success stories from the database
    return render_template('index.html', stories=stories)

# Route for adding a new success story
@app.route('/add', methods=['GET', 'POST'])
def add_story():
    if request.method == 'POST':
        name = request.form['name']
        contribution = request.form['contribution']
        
        # Error handling for empty fields
        if not name or not contribution:
            flash('Name and contribution are required!', 'error')
            return redirect(url_for('add_story'))

        new_story = SuccessStory(name=name, contribution=contribution)
        db.session.add(new_story)
        db.session.commit()
        flash('Success story added!', 'success')
        return redirect(url_for('index'))

    return render_template('add_story.html')

# Route for deleting a success story
@app.route('/delete/<int:id>')
def delete_story(id):
    story_to_delete = SuccessStory.query.get_or_404(id)  # Fetch story or return 404
    db.session.delete(story_to_delete)
    db.session.commit()
    flash('Success story deleted!', 'success')
    return redirect(url_for('index'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success Stories of Women Leaders</title>
</head>
<body>
    <h1>Success Stories of Women Leaders from Sauti Kenya</h1>
    <a href="{{ url_for('add_story') }}">Add New Story</a>
    <ul>
        {% for story in stories %}
            <li>
                <strong>{{ story.name }}</strong>: {{ story.contribution }}
                <a href="{{ url_for('delete_story', id=story.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **add_story.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Success Story</title>
</head>
<body>
    <h1>Add a New Success Story</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="contribution">Contribution:</label>
        <textarea id="contribution" name="contribution" required></textarea>
        <br>
        <button type="submit">Add Story</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

3. **404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
