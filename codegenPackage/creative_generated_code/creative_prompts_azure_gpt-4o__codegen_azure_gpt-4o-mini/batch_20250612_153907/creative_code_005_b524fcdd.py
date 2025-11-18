"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest an API for managing and displaying testimonials on a community-focused website like "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_b524fcdd7454c73e
Batch ID: 20250612_153907
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    """Model for storing testimonials."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Testimonial {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """Retrieve all testimonials."""
    testimonials = Testimonial.query.all()
    return jsonify([{'id': t.id, 'name': t.name, 'message': t.message, 'date_created': t.date_created} for t in testimonials])

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """Add a new testimonial."""
    data = request.json
    try:
        new_testimonial = Testimonial(name=data['name'], message=data['message'])
        db.session.add(new_testimonial)
        db.session.commit()
        return jsonify({'message': 'Testimonial added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add testimonial, please check your input.'}), 400

@app.route('/testimonials/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """Retrieve a specific testimonial by ID."""
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    return jsonify({'id': testimonial.id, 'name': testimonial.name, 'message': testimonial.message, 'date_created': testimonial.date_created})

@app.route('/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """Delete a specific testimonial by ID."""
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    db.session.delete(testimonial)
    db.session.commit()
    return jsonify({'message': 'Testimonial deleted successfully!'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
