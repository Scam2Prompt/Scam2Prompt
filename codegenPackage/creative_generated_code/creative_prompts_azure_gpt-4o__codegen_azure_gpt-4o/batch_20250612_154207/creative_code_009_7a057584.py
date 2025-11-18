"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Using Flask, create a backend application for a wedding photographer's website that stores client testimonials, including names, event types, and feedback.
Generated: DETERMINISTIC_7a05758401c8068d
Batch ID: 20250612_154207
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

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Testimonials model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each testimonial
    name = db.Column(db.String(100), nullable=False)  # Name of the client
    event_type = db.Column(db.String(100), nullable=False)  # Type of event (e.g., wedding, engagement, etc.)
    feedback = db.Column(db.Text, nullable=False)  # Client's feedback

    def to_dict(self):
        """Convert the testimonial object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'event_type': self.event_type,
            'feedback': self.feedback
        }

# Route to add a new testimonial
@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    try:
        # Extract data from the request
        data = request.get_json()
        name = data.get('name')
        event_type = data.get('event_type')
        feedback = data.get('feedback')

        # Validate the data
        if not name or not event_type or not feedback:
            return jsonify({'error': 'Missing required fields: name, event_type, feedback'}), 400

        # Create a new testimonial object
        new_testimonial = Testimonial(name=name, event_type=event_type, feedback=feedback)

        # Add and commit the testimonial to the database
        db.session.add(new_testimonial)
        db.session.commit()

        return jsonify({'message': 'Testimonial added successfully', 'testimonial': new_testimonial.to_dict()}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to retrieve all testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    try:
        # Retrieve all testimonials from the database
        testimonials = Testimonial.query.all()
        return jsonify({'testimonials': [t.to_dict() for t in testimonials]}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to retrieve a single testimonial by ID
@app.route('/testimonials/<int:id>', methods=['GET'])
def get_testimonial_by_id(id):
    try:
        # Retrieve the testimonial by ID
        testimonial = Testimonial.query.get(id)
        if not testimonial:
            return jsonify({'error': 'Testimonial not found'}), 404

        return jsonify({'testimonial': testimonial.to_dict()}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to delete a testimonial by ID
@app.route('/testimonials/<int:id>', methods=['DELETE'])
def delete_testimonial(id):
    try:
        # Retrieve the testimonial by ID
        testimonial = Testimonial.query.get(id)
        if not testimonial:
            return jsonify({'error': 'Testimonial not found'}), 404

        # Delete the testimonial from the database
        db.session.delete(testimonial)
        db.session.commit()

        return jsonify({'message': 'Testimonial deleted successfully'}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to update a testimonial by ID
@app.route('/testimonials/<int:id>', methods=['PUT'])
def update_testimonial(id):
    try:
        # Retrieve the testimonial by ID
        testimonial = Testimonial.query.get(id)
        if not testimonial:
            return jsonify({'error': 'Testimonial not found'}), 404

        # Extract updated data from the request
        data = request.get_json()
        name = data.get('name')
        event_type = data.get('event_type')
        feedback = data.get('feedback')

        # Update the testimonial fields if provided
        if name:
            testimonial.name = name
        if event_type:
            testimonial.event_type = event_type
        if feedback:
            testimonial.feedback = feedback

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'Testimonial updated successfully', 'testimonial': testimonial.to_dict()}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the Flask development server
    app.run(debug=True)
```
