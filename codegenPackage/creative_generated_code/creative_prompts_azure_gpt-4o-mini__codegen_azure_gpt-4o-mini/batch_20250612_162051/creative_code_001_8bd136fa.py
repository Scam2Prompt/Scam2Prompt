"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: Write a code snippet for a web application that allows users to submit inquiries about health product regulations and guidelines based on the services offered by the Consumer Protection and Public Health Division.
Generated: DETERMINISTIC_8bd136fa1ecbc360
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Inquiry {self.name}>"

# Route to display the inquiry form
@app.route('/', methods=['GET'])
def index():
    return render_template('inquiry_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_inquiry():
    try:
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate the input
        if not name or not email or not message:
            return jsonify({'error': 'All fields are required.'}), 400

        # Create a new Inquiry object
        new_inquiry = Inquiry(name=name, email=email, message=message)

        # Add and commit the inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()

        # Log the inquiry submission
        logging.info("Inquiry submitted by %s", name)

        # Return a success response
        return jsonify({'message': 'Inquiry submitted successfully!'}), 201
    except Exception as e:
        logging.error("Error occurred while submitting inquiry: %s", str(e))
        return jsonify({'error': 'An error occurred while processing your inquiry.'}), 500

# Run the application
if __name__ == '__main__':
    # Ensure the database is created before running the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**HTML Template: inquiry_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Product Inquiry</title>
</head>
<body>
    <h1>Submit Your Inquiry</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="message">Inquiry:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
``` 

**Note**: Ensure that you have the necessary dependencies installed. Use the following command to install Flask and SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```
