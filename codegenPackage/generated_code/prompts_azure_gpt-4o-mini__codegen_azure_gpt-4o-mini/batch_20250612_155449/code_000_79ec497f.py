"""
Generated Code Metadata:
========================
Original URL: https://tsunarloyni-connext.pages.dev
Prompt: Generate code for a web application that allows users to customize car designs based on driver ambitions.
Generated: DETERMINISTIC_79ec497f2f1ea6a6
Batch ID: 20250612_155449
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_designs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CarDesign model
class CarDesign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ambition = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    wheels = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<CarDesign {self.ambition} - {self.color} - {self.wheels}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to customize car design
@app.route('/customize', methods=['POST'])
def customize():
    try:
        # Get data from the request
        ambition = request.json.get('ambition')
        color = request.json.get('color')
        wheels = request.json.get('wheels')

        # Validate input data
        if not ambition or not color or not wheels:
            return jsonify({'error': 'All fields are required!'}), 400

        # Create a new car design
        new_design = CarDesign(ambition=ambition, color=color, wheels=wheels)
        db.session.add(new_design)
        db.session.commit()

        return jsonify({'message': 'Car design created successfully!', 'design': new_design.id}), 201

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all car designs
@app.route('/designs', methods=['GET'])
def get_designs():
    try:
        designs = CarDesign.query.all()
        return jsonify([{'id': d.id, 'ambition': d.ambition, 'color': d.color, 'wheels': d.wheels} for d in designs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Design Customizer</title>
    <script>
        async function customizeCar() {
            const ambition = document.getElementById('ambition').value;
            const color = document.getElementById('color').value;
            const wheels = document.getElementById('wheels').value;

            const response = await fetch('/customize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ambition, color, wheels })
            });

            const result = await response.json();
            alert(result.message || result.error);
        }

        async function fetchDesigns() {
            const response = await fetch('/designs');
            const designs = await response.json();
            console.log(designs);
        }
    </script>
</head>
<body>
    <h1>Customize Your Car Design</h1>
    <input type="text" id="ambition" placeholder="Driver Ambition" required>
    <input type="text" id="color" placeholder="Car Color" required>
    <input type="text" id="wheels" placeholder="Wheel Type" required>
    <button onclick="customizeCar()">Create Design</button>
    <button onclick="fetchDesigns()">View Designs</button>
</body>
</html>
```
