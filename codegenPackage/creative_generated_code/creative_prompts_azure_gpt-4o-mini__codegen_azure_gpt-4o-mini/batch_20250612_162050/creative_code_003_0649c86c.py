"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: What are the best practices for developing user-friendly web applications, and how can I apply these principles in a project similar to those showcased by CTIAR?
Generated: DETERMINISTIC_0649c86c4b797fab
Batch ID: 20250612_162050
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Error handler for HTTP errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return custom error messages."""
    return f"Error {e.code}: {e.description}", e.code

# Route for the home page
@app.route('/')
def home():
    """Render the home page with a list of users."""
    users = User.query.all()
    return render_template('home.html', users=users)

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the database."""
    try:
        username = request.form['username']
        email = request.form['email']
        
        if not username or not email:
            flash('Username and email are required!', 'danger')
            return redirect(url_for('home'))
        
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback the session on error
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('home'))

# Main block to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Enable debug mode for development
```

### home.html (Sample HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.username }} - {{ user.email }}</li>
        {% endfor %}
    </ul>

    <h2>Add User</h2>
    <form method="POST" action="{{ url_for('add_user') }}">
        <input type="text" name="username" placeholder="Username" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Add User</button>
    </form>

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

### Requirements
- To run this code, you need to have Flask installed. You can install it via pip:
  ```
  pip install Flask Flask-SQLAlchemy
  ```
- Ensure to replace `'your_secret_key'` with a strong secret key for production use.
