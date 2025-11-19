"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: How can I create a web application that allows users to view and book properties like those listed on the Moms PG site, including amenities and pricing details?
Generated: DETERMINISTIC_31b2ca31b9167a07
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Property {self.name}>'

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to display all properties
@app.route('/')
def index():
    properties = Property.query.all()  # Fetch all properties from the database
    return render_template('index.html', properties=properties)

# Route to add a new property
@app.route('/add', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        name = request.form['name']
        amenities = request.form['amenities']
        price = request.form['price']
        
        new_property = Property(name=name, amenities=amenities, price=price)  # Create new property
        
        try:
            db.session.add(new_property)  # Add to the session
            db.session.commit()  # Commit the changes
            flash('Property added successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()  # Rollback in case of error
            flash('Error adding property!', 'danger')  # Flash error message

    return render_template('add_property.html')  # Render add property form

# Route to book a property (Placeholder for actual implementation)
@app.route('/book/<int:property_id>', methods=['POST'])
def book_property(property_id):
    property_to_book = Property.query.get_or_404(property_id)  # Fetch property or return 404
    
    # Placeholder for booking logic (e.g., save booking to database)
    flash(f'You have booked {property_to_book.name}!', 'success')  # Flash booking success message
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render 404 template

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to True for development; set to False in production
```

### HTML Templates (Assumed to be in a 'templates' folder)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Listing</title>
</head>
<body>
    <h1>Available Properties</h1>
    <ul>
        {% for property in properties %}
        <li>
            <h2>{{ property.name }}</h2>
            <p>Amenities: {{ property.amenities }}</p>
            <p>Price: ${{ property.price }}</p>
            <form action="{{ url_for('book_property', property_id=property.id) }}" method="POST">
                <button type="submit">Book Now</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_property') }}">Add New Property</a>
</body>
</html>
```

**add_property.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Property</title>
</head>
<body>
    <h1>Add New Property</h1>
    <form action="{{ url_for('add_property') }}" method="POST">
        <label for="name">Property Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="amenities">Amenities:</label>
        <input type="text" id="amenities" name="amenities" required>
        <br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" required step="0.01">
        <br>
        <button type="submit">Add Property</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Property List</a>
</body>
</html>
```

**404.html**
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
    <a href="{{ url_for('index') }}">Go back to the home page</a>
</body>
</html>
```

### Note
- Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
- Replace `'your_secret_key'` with an actual secret key for session management in production.
