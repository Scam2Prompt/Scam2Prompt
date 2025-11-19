"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a REST API endpoint that allows patients to submit testimonials about their experiences with cosmetic surgery, inspired by the testimonials section on Dr. Gareth September's website.
Generated: DETERMINISTIC_7d5f1fb8ab56e649
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each testimonial
    name = db.Column(db.String(100), nullable=False)  # Patient's name
    email = db.Column(db.String(120), nullable=False)  # Patient's email
    message = db.Column(db.Text, nullable=False)  # Testimonial message
    created_at = db.Column(db.DateTime, server_default=db.func.now())  # Timestamp

    def to_dict(self):
        """Convert the Testimonial object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'created_at': self.created_at
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Define the endpoint to submit a testimonial
@app.route('/api/testimonials', methods=['POST'])
def submit_testimonial():
    """
    Endpoint to submit a new testimonial.
    Expects JSON payload with 'name', 'email', and 'message'.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON payload'}), 400

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({'error': 'Name, email, and message are required'}), 400

        # Create a new Testimonial object
        testimonial = Testimonial(name=name, email=email, message=message)

        # Save the testimonial to the database
        db.session.add(testimonial)
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Testimonial submitted successfully', 'testimonial': testimonial.to_dict()}), 201

    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Define the endpoint to retrieve all testimonials
@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint to retrieve all testimonials.
    Returns a list of testimonials in JSON format.
    """
    try:
        # Query all testimonials from the database
        testimonials = Testimonial.query.order_by(Testimonial.created_at.desc()).all()

        # Convert the testimonials to a list of dictionaries
        testimonials_list = [testimonial.to_dict() for testimonial in testimonials]

        # Return the testimonials as JSON
        return jsonify({'testimonials': testimonials_list}), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
