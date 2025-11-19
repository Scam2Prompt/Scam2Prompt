"""
Generated Code Metadata:
========================
Original URL: https://muutum.info
Prompt: Design a code snippet for integrating a full-service cafe and shared kitchen features into a luxury apartment complex's website, inspired by Mutuum Apartments.
Generated: DETERMINISTIC_fe1232f188dd8801
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe_kitchen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Cafe and Kitchen models
class Cafe(db.Model):
    """Model representing the cafe."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    opening_hours = db.Column(db.String(50), nullable=False)

class SharedKitchen(db.Model):
    """Model representing the shared kitchen."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page with cafe and kitchen information."""
    cafes = Cafe.query.all()
    kitchens = SharedKitchen.query.all()
    return render_template('index.html', cafes=cafes, kitchens=kitchens)

@app.route('/api/cafes', methods=['GET'])
def get_cafes():
    """API endpoint to retrieve all cafes."""
    try:
        cafes = Cafe.query.all()
        return jsonify([{'id': cafe.id, 'name': cafe.name, 'description': cafe.description, 'opening_hours': cafe.opening_hours} for cafe in cafes]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/kitchens', methods=['GET'])
def get_kitchens():
    """API endpoint to retrieve all shared kitchens."""
    try:
        kitchens = SharedKitchen.query.all()
        return jsonify([{'id': kitchen.id, 'name': kitchen.name, 'capacity': kitchen.capacity, 'availability': kitchen.availability} for kitchen in kitchens]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/cafes', methods=['POST'])
def add_cafe():
    """API endpoint to add a new cafe."""
    try:
        data = request.json
        new_cafe = Cafe(name=data['name'], description=data['description'], opening_hours=data['opening_hours'])
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({'message': 'Cafe added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/kitchens', methods=['POST'])
def add_kitchen():
    """API endpoint to add a new shared kitchen."""
    try:
        data = request.json
        new_kitchen = SharedKitchen(name=data['name'], capacity=data['capacity'], availability=data['availability'])
        db.session.add(new_kitchen)
        db.session.commit()
        return jsonify({'message': 'Shared kitchen added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cafe and Shared Kitchen</title>
</head>
<body>
    <h1>Welcome to the Luxury Apartment Complex</h1>
    <h2>Cafes</h2>
    <ul>
        {% for cafe in cafes %}
            <li>{{ cafe.name }}: {{ cafe.description }} ({{ cafe.opening_hours }})</li>
        {% endfor %}
    </ul>
    <h2>Shared Kitchens</h2>
    <ul>
        {% for kitchen in kitchens %}
            <li>{{ kitchen.name }}: Capacity {{ kitchen.capacity }} ({{ kitchen.availability }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; adjust the URI for production use.
- The HTML template should be placed in a `templates` directory within the project structure.
