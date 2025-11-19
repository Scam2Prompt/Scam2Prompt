"""
Generated Code Metadata:
========================
Original URL: https://whitelist-tensorians.pages.dev
Prompt: "Design a basic structure for a meme gallery website inspired by the Tensorians collection, including user interaction features."
Generated: DETERMINISTIC_aa9e81ede507276f
Batch ID: 20250622_210703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memes.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize the database

# Define the Meme model
class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Meme title
    image_url = db.Column(db.String(200), nullable=False)  # URL of the meme image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of creation

    def __repr__(self):
        return f'<Meme {self.title}>'

# Route for the home page displaying the meme gallery
@app.route('/')
def index():
    memes = Meme.query.all()  # Fetch all memes from the database
    return render_template('index.html', memes=memes)  # Render the index template

# Route for adding a new meme
@app.route('/add', methods=['POST'])
def add_meme():
    title = request.form.get('title')  # Get the title from the form
    image_url = request.form.get('image_url')  # Get the image URL from the form

    # Basic validation
    if not title or not image_url:
        flash('Title and Image URL are required!', 'error')  # Flash error message
        return redirect(url_for('index'))  # Redirect back to the index page

    # Create a new Meme instance
    new_meme = Meme(title=title, image_url=image_url)

    try:
        db.session.add(new_meme)  # Add the new meme to the session
        db.session.commit()  # Commit the session to save the meme
        flash('Meme added successfully!', 'success')  # Flash success message
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'Error adding meme: {str(e)}', 'error')  # Flash error message

    return redirect(url_for('index'))  # Redirect back to the index page

# Route for deleting a meme
@app.route('/delete/<int:meme_id>', methods=['POST'])
def delete_meme(meme_id):
    meme = Meme.query.get_or_404(meme_id)  # Fetch the meme or return 404 if not found

    try:
        db.session.delete(meme)  # Delete the meme from the session
        db.session.commit()  # Commit the session to save changes
        flash('Meme deleted successfully!', 'success')  # Flash success message
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'Error deleting meme: {str(e)}', 'error')  # Flash error message

    return redirect(url_for('index'))  # Redirect back to the index page

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Gallery</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Meme Gallery</h1>
        <form action="/add" method="POST" class="mb-4">
            <input type="text" name="title" placeholder="Meme Title" required>
            <input type="text" name="image_url" placeholder="Image URL" required>
            <button type="submit" class="btn btn-primary">Add Meme</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <div class="row">
            {% for meme in memes %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <img src="{{ meme.image_url }}" class="card-img-top" alt="{{ meme.title }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ meme.title }}</h5>
                            <form action="/delete/{{ meme.id }}" method="POST">
                                <button type="submit" class="btn btn-danger">Delete Meme</button>
                            </form>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- The HTML template should be saved in a folder named `templates` in the same directory as your Python script.
