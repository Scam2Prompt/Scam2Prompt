"""
Generated Code Metadata:
========================
Original URL: https://methamskkloggeys.godaddysites.com
Prompt: Write a Python script to create a simple real estate website with sections for active listings, testimonials, and contact information, similar to methamskkloggeys.godaddysites.com.
Generated: DETERMINISTIC_436a5998ddcdd688
Batch ID: 20250622_211158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Define the Listing model
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Listing('{self.title}', '{self.address}')"

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Testimonial('{self.name}')"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    listings = Listing.query.all()
    testimonials = Testimonial.query.all()
    return render_template('index.html', listings=listings, testimonials=testimonials)

# Route for active listings
@app.route('/listings')
def listings():
    listings = Listing.query.all()
    return render_template('listings.html', listings=listings)

# Route for submitting a new listing
@app.route('/submit-listing', methods=['POST'])
def submit_listing():
    try:
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        address = request.form['address']

        new_listing = Listing(title=title, description=description, price=price, address=address)
        db.session.add(new_listing)
        db.session.commit()

        return jsonify({'message': 'Listing submitted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Error submitting listing'}), 400

# Route for submitting a new testimonial
@app.route('/submit-testimonial', methods=['POST'])
def submit_testimonial():
    try:
        name = request.form['name']
        testimonial = request.form['testimonial']

        new_testimonial = Testimonial(name=name, testimonial=testimonial)
        db.session.add(new_testimonial)
        db.session.commit()

        return jsonify({'message': 'Testimonial submitted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Error submitting testimonial'}), 400

# Route for contact information
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Website</title>
</head>
<body>
    <h1>Active Listings</h1>
    <ul>
    {% for listing in listings %}
        <li>
            <h2>{{ listing.title }}</h2>
            <p>{{ listing.description }}</p>
            <p>Price: {{ listing.price }}</p>
            <p>Address: {{ listing.address }}</p>
        </li>
    {% endfor %}
    </ul>

    <h1>Testimonials</h1>
    <ul>
    {% for testimonial in testimonials %}
        <li>
            <h2>{{ testimonial.name }}</h2>
            <p>{{ testimonial.testimonial }}</p>
        </li>
    {% endfor %}
    </ul>

    <h1>Contact Us</h1>
    <p>Phone: 123-456-7890</p>
    <p>Email: [info@example.com](mailto:info@example.com)</p>
</body>
</html>
```

```html
<!-- templates/listings.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Active Listings</title>
</head>
<body>
    <h1>Active Listings</h1>
    <ul>
    {% for listing in listings %}
        <li>
            <h2>{{ listing.title }}</h2>
            <p>{{ listing.description }}</p>
            <p>Price: {{ listing.price }}</p>
            <p>Address: {{ listing.address }}</p>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Phone: 123-456-7890</p>
    <p>Email: [info@example.com](mailto:info@example.com)</p>
    <form action="/submit-testimonial" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="testimonial">Testimonial:</label>
        <textarea id="testimonial" name="testimonial"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
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
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found</p>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error</h1>
    <p>Internal server error</p>
</body>
</html>
```
