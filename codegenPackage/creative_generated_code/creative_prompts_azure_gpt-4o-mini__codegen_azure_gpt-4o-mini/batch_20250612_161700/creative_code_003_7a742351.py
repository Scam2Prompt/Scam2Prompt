"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Develop a web application that showcases art collaborations, similar to the community-focused approach of Kroo Nation.
Generated: DETERMINISTIC_7a742351302caeb7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_collaborations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this for production

# Initialize the database
db = SQLAlchemy(app)

# Define the ArtCollaboration model
class ArtCollaboration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Collaboration {self.title}>'

# Route for the homepage
@app.route('/')
def index():
    collaborations = ArtCollaboration.query.all()  # Fetch all collaborations from the database
    return render_template('index.html', collaborations=collaborations)

# Route to add a new collaboration
@app.route('/add', methods=['GET', 'POST'])
def add_collaboration():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if not title or not description:
            flash('Title and description are required!', 'danger')
            return redirect(url_for('add_collaboration'))

        new_collab = ArtCollaboration(title=title, description=description)
        db.session.add(new_collab)

        try:
            db.session.commit()  # Commit the new collaboration to the database
            flash('Collaboration added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error occurred while adding collaboration: ' + str(e), 'danger')
    
    return render_template('add_collaboration.html')

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main block to run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Set debug to False for production

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Art Collaborations</title>
</head>
<body>
    <h1>Art Collaborations</h1>
    <a href="{{ url_for('add_collaboration') }}">Add New Collaboration</a>
    <ul>
        {% for collaboration in collaborations %}
            <li>{{ collaboration.title }} - {{ collaboration.description }} ({{ collaboration.created_at }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_collaboration.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Collaboration</title>
</head>
<body>
    <h1>Add New Collaboration</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

```bash
# requirements.txt
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
```

To run this application:
1. Save the Python code in a file named `app.py`.
2. Create a directory called `templates` and place the HTML files inside.
3. Create a `requirements.txt` file with the specified dependencies.
4. Install the dependencies with `pip install -r requirements.txt`.
5. Run the application using `python app.py`.
