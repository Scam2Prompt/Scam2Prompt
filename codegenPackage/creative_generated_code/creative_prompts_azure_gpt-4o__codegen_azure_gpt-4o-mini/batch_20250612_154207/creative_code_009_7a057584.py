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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Testimonial {self.name} - {self.event_type}>'

# Create the database and the table
with app.app_context():
    db.create_all()

# Route to submit a new testimonial
@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'event_type' not in data or 'feedback' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_testimonial = Testimonial(
        name=data['name'],
        event_type=data['event_type'],
        feedback=data['feedback']
    )

    try:
        db.session.add(new_testimonial)
        db.session.commit()
        return jsonify({'message': 'Testimonial added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Testimonial could not be added. Please try again.'}), 500

# Route to retrieve all testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    testimonials = Testimonial.query.all()
    return jsonify([{
        'id': t.id,
        'name': t.name,
        'event_type': t.event_type,
        'feedback': t.feedback
    } for t in testimonials]), 200

# Route to retrieve a single testimonial by ID
@app.route('/testimonials/<int:id>', methods=['GET'])
def get_testimonial(id):
    testimonial = Testimonial.query.get(id)
    if testimonial is None:
        return jsonify({'error': 'Testimonial not found'}), 404
    return jsonify({
        'id': testimonial.id,
        'name': testimonial.name,
        'event_type': testimonial.event_type,
        'feedback': testimonial.feedback
    }), 200

# Route to delete a testimonial
@app.route('/testimonials/<int:id>', methods=['DELETE'])
def delete_testimonial(id):
    testimonial = Testimonial.query.get(id)
    if testimonial is None:
        return jsonify({'error': 'Testimonial not found'}), 404

    db.session.delete(testimonial)
    db.session.commit()
    return jsonify({'message': 'Testimonial deleted successfully!'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
