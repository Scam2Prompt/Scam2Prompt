"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cem-ac.org
Prompt: Suggest a library for building a web interface that highlights the artistic contributions of Mexican cinema and stage arts, focusing on quality and cultural impact.
Generated: DETERMINISTIC_1fa34cb4868a443d
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI; adjust to your database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinema_stage_arts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for artistic contributions
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'Cinema', 'Stage'

    def __repr__(self):
        return f'<Contribution {self.title}>'

# Homepage route for displaying contributions
@app.route('/')
def index():
    try:
        contributions = Contribution.query.all()  # Fetch all contributions
        return render_template('index.html', contributions=contributions)
    except Exception as e:
        return f"An error occurred while retrieving data: {e}", 500

# Route for adding a new contribution
@app.route('/add', methods=['POST'])
def add_contribution():
    try:
        # Retrieve data from the form
        title = request.form['title']
        description = request.form['description']
        year = request.form['year']
        type = request.form['type']

        # Create a new Contribution object
        new_contribution = Contribution(title=title, description=description, year=year, type=type)
        db.session.add(new_contribution)  # Add it to the session
        db.session.commit()  # Commit the changes to the database
        return f"Contribution '{title}' added successfully!", 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return f"An error occurred while adding the contribution: {e}", 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

```html
<!-- Save this HTML as templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mexican Cinema and Stage Arts</title>
</head>
<body>
    <h1>Artistic Contributions of Mexican Cinema and Stage Arts</h1>
    <ul>
        {% for contribution in contributions %}
            <li>{{ contribution.title }} ({{ contribution.year }}): {{ contribution.description }}</li>
        {% endfor %}
    </ul>
    
    <h2>Add a New Contribution</h2>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Title" required>
        <textarea name="description" placeholder="Description" required></textarea>
        <input type="number" name="year" placeholder="Year" required>
        <input type="text" name="type" placeholder="Type (Cinema/Stage)" required>
        <button type="submit">Add Contribution</button>
    </form>
</body>
</html>
```

### Note:
Make sure to install the required libraries before running the code:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
``` 

To create the database, run the following commands in the Python shell:
```python
from app import db
db.create_all()  # Create database tables
```
