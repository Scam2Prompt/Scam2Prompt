"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Provide a code example for a web application that allows users to book laptop rentals, based on the digital solutions mentioned in the Azuharu article about Sewa Laptop Surabaya.
Generated: DETERMINISTIC_b60bae6437bce7bf
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Define the Laptop model
class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Laptop {self.brand} {self.model}>'

# Define the Rental model
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    laptop_id = db.Column(db.Integer, db.ForeignKey('laptop.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    laptop = db.relationship('Laptop', backref='rentals')

    def __repr__(self):
        return f'<Rental {self.id} by {self.user_name}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to list available laptops
@app.route('/laptops', methods=['GET'])
def get_laptops():
    try:
        laptops = Laptop.query.filter_by(available=True).all()
        return jsonify([{'id': laptop.id, 'brand': laptop.brand, 'model': laptop.model} for laptop in laptops]), 200
    except Exception as e:
        logging.error(f"Error retrieving laptops: {e}")
        return jsonify({"error": "Could not retrieve laptops"}), 500

# API Endpoint to book a laptop rental
@app.route('/rent', methods=['POST'])
def rent_laptop():
    data = request.json
    laptop_id = data.get('laptop_id')
    user_name = data.get('user_name')
    start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')

    # Error handling for invalid input
    if not laptop_id or not user_name or not start_date or not end_date:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        laptop = Laptop.query.get(laptop_id)

        # Check if the laptop is available for rental
        if not laptop or not laptop.available:
            return jsonify({"error": "Laptop not available"}), 400

        # Create a new rental entry
        rental = Rental(laptop_id=laptop_id, user_name=user_name, start_date=start_date, end_date=end_date)
        laptop.available = False  # Mark the laptop as rented
        db.session.add(rental)
        db.session.commit()

        return jsonify({"message": "Laptop rented successfully", "rental_id": rental.id}), 201
    except Exception as e:
        logging.error(f"Error renting laptop: {e}")
        return jsonify({"error": "Could not rent laptop"}), 500

# API Endpoint to return a laptop rental
@app.route('/return', methods=['POST'])
def return_laptop():
    data = request.json
    rental_id = data.get('rental_id')

    if not rental_id:
        return jsonify({"error": "Missing rental_id"}), 400

    try:
        rental = Rental.query.get(rental_id)

        if not rental:
            return jsonify({"error": "Invalid rental ID"}), 400

        # Mark the laptop as available again
        laptop = Laptop.query.get(rental.laptop_id)
        laptop.available = True
        db.session.delete(rental)
        db.session.commit()

        return jsonify({"message": "Laptop returned successfully"}), 200
    except Exception as e:
        logging.error(f"Error returning laptop: {e}")
        return jsonify({"error": "Could not return laptop"}), 500

# Run the application
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
    <title>Laptop Rental</title>
</head>
<body>
    <h1>Laptop Rental Service</h1>
    <h2>Available Laptops</h2>
    <div id="laptop-list"></div>
    <script>
        // Fetch available laptops and display them
        fetch('/laptops')
            .then(response => response.json())
            .then(data => {
                const laptopList = document.getElementById('laptop-list');
                data.forEach(laptop => {
                    const div = document.createElement('div');
                    div.textContent = `${laptop.brand} ${laptop.model}`;
                    laptopList.appendChild(div);
                });
            })
            .catch(error => console.error('Error fetching laptops:', error));
    </script>
</body>
</html>
```

### Notes:
- This code uses Flask for the web application along with SQLAlchemy for the database part. The database is SQLite for simplicity but can be replaced with other databases as needed.
- Proper error handling has been included for the endpoint functionalities.
- HTML is included for rendering the available laptops. The JavaScript fetches the available laptops and displays them on the page. 
- Make sure to create the necessary database and install Flask and Flask-SQLAlchemy packages to run this application.
