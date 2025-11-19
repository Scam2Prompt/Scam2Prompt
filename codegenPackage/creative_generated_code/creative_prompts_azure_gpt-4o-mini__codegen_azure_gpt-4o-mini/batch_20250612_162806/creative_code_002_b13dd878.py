"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Generate an API endpoint for submitting customer testimonials for a paving service, inspired by the testimonials section of Bedford Paving's site.
Generated: DETERMINISTIC_b13dd878501d43c3
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Testimonial {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to validate testimonial data
def validate_testimonial(name, message):
    if not name or not message:
        raise ValueError("Both name and message are required.")
    if len(name) > 100:
        raise ValueError("Name must be 100 characters or less.")
    if len(message) > 1000:
        raise ValueError("Message must be 1000 characters or less.")

# API endpoint to submit a testimonial
@app.route('/api/testimonials', methods=['POST'])
def submit_testimonial():
    """
    Submit a customer testimonial to the database.
    Expects a JSON payload with 'name' and 'message'.
    Returns a success message and the new testimonial ID if successful,
    or an error message if unsuccessful.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        name = data.get('name')
        message = data.get('message')

        # Validate input data
        validate_testimonial(name, message)

        # Create a new testimonial instance
        new_testimonial = Testimonial(name=name, message=message)

        # Add the testimonial to the session and commit
        db.session.add(new_testimonial)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Testimonial submitted successfully!", "id": new_testimonial.id}), 201

    except ValueError as ve:
        # Handle validation errors
        return jsonify({"error": str(ve)}), 400
    except IntegrityError:
        # Handle integrity errors, such as duplicate entries
        db.session.rollback()
        return jsonify({"error": "An error occurred while submitting your testimonial."}), 500
    except Exception as e:
        # Handle any other unforeseen errors
        return jsonify({"error": str(e)}), 500

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
```
