"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Suggest a library or framework for building a web application that allows users to customize Phantom retractable screens for doors, windows, and patios, including integration with an online store.
Generated: DETERMINISTIC_689f2e96fa599a05
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///screens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for the screen customization
class ScreenCustomization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screen_type = db.Column(db.String(50), nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<ScreenCustomization {self.screen_type}, {self.width}x{self.height}, {self.color}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to render the customization form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle customization data submission
@app.route('/customize', methods=['POST'])
def customize():
    try:
        # Get data from the form
        screen_type = request.json.get('screen_type')
        width = request.json.get('width')
        height = request.json.get('height')
        color = request.json.get('color')

        # Validate input data
        if not screen_type or not width or not height or not color:
            return jsonify({'error': 'All fields are required.'}), 400

        # Create a new ScreenCustomization instance
        new_customization = ScreenCustomization(
            screen_type=screen_type,
            width=width,
            height=height,
            color=color
        )

        # Add to the database
        db.session.add(new_customization)
        db.session.commit()

        return jsonify({'message': 'Customization saved successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to retrieve customizations for display (e.g., for an online store)
@app.route('/customizations', methods=['GET'])
def get_customizations():
    try:
        customizations = ScreenCustomization.query.all()
        return jsonify([{
            'screen_type': c.screen_type,
            'width': c.width,
            'height': c.height,
            'color': c.color
        } for c in customizations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point to run the application
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
    <title>Screen Customization</title>
</head>
<body>
    <h1>Customize Your Phantom Screens</h1>
    <form id="customization-form">
        <label for="screen_type">Screen Type:</label>
        <input type="text" id="screen_type" name="screen_type" required>
        <br>
        <label for="width">Width (inches):</label>
        <input type="number" id="width" name="width" required>
        <br>
        <label for="height">Height (inches):</label>
        <input type="number" id="height" name="height" required>
        <br>
        <label for="color">Color:</label>
        <input type="text" id="color" name="color" required>
        <br>
        <button type="submit">Save Customization</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('customization-form').addEventListener('submit', function(event) {
            event.preventDefault();

            const data = {
                screen_type: this.screen_type.value,
                width: this.width.value,
                height: this.height.value,
                color: this.color.value
            };

            fetch('/customize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = data.message || data.error;
            })
            .catch(error => {
                document.getElementById('result').innerText = 'An error occurred: ' + error;
            });
        });
    </script>
</body>
</html>
```
