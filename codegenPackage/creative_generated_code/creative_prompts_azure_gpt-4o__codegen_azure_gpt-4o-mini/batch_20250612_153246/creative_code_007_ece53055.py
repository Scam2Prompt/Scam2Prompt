"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Develop a RESTful API for a holistic health clinic to manage client testimonials, allowing users to submit feedback and display it on the website.
Generated: DETERMINISTIC_ece530551547a7b8
Batch ID: 20250612_153246
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
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'feedback': self.feedback
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit a new testimonial
@app.route('/testimonials', methods=['POST'])
def submit_testimonial():
    data = request.get_json()

    # Validate request data
    if not data or 'client_name' not in data or 'feedback' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_testimonial = Testimonial(client_name=data['client_name'], feedback=data['feedback'])

    try:
        db.session.add(new_testimonial)
        db.session.commit()
        return jsonify(new_testimonial.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Route to retrieve all testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    testimonials = Testimonial.query.all()
    return jsonify([testimonial.to_dict() for testimonial in testimonials]), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Run the application
if __name__ == '__main__':
    # Ensure the database file is created
    if not os.path.exists('testimonials.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
```
