"""
Generated Code Metadata:
========================
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for selling feminine and masculine shoes, including sandals and social shoes.
Generated: DETERMINISTIC_02435c1f09e05462
Batch ID: 20250622_212524
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoes.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize the database

# Define the Shoe model
class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'feminine' or 'masculine'
    type = db.Column(db.String(50), nullable=False)  # 'sandals' or 'social'
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Shoe {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    shoes = Shoe.query.all()  # Fetch all shoes from the database
    return render_template('home.html', shoes=shoes)

# Route to add a new shoe
@app.route('/add', methods=['GET', 'POST'])
def add_shoe():
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            type_ = request.form['type']
            price = float(request.form['price'])

            # Create a new Shoe instance
            new_shoe = Shoe(name=name, category=category, type=type_, price=price)
            db.session.add(new_shoe)  # Add the shoe to the session
            db.session.commit()  # Commit the session to save the shoe
            flash('Shoe added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error adding shoe: {str(e)}', 'danger')
    return render_template('add_shoe.html')

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template('error.html', error=e), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shoe Store</title>
</head>
<body>
    <h1>Welcome to the Shoe Store</h1>
    <a href="{{ url_for('add_shoe') }}">Add New Shoe</a>
    <ul>
        {% for shoe in shoes %}
            <li>{{ shoe.name }} - {{ shoe.category }} - {{ shoe.type }} - ${{ shoe.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_shoe.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Shoe</title>
</head>
<body>
    <h1>Add a New Shoe</h1>
    <form method="POST">
        <label for="name">Shoe Name:</label>
        <input type="text" name="name" required>
        <label for="category">Category (feminine/masculine):</label>
        <input type="text" name="category" required>
        <label for="type">Type (sandals/social):</label>
        <input type="text" name="type" required>
        <label for="price">Price:</label>
        <input type="number" step="0.01" name="price" required>
        <button type="submit">Add Shoe</button>
    </form>
</body>
</html>
```

**error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('home') }}">Go back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for session management.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
