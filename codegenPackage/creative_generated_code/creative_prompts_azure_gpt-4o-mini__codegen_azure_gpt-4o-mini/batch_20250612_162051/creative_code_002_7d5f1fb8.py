"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a REST API endpoint that allows patients to submit testimonials about their experiences with cosmetic surgery, inspired by the testimonials section on Dr. Gareth September's website.
Generated: DETERMINISTIC_7d5f1fb8ab56e649
Batch ID: 20250612_162051
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Testimonials model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Testimonial {self.patient_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/testimonials', methods=['POST'])
def submit_testimonial():
    """
    Endpoint to submit a new testimonial.
    Expects JSON with 'patient_name', 'content', and 'rating'.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or not all(key in data for key in ('patient_name', 'content', 'rating')):
            return jsonify({"error": "Missing data"}), 400
        
        if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
            return jsonify({"error": "Rating must be an integer between 1 and 5"}), 400
        
        # Create a new Testimonial instance
        testimonial = Testimonial(
            patient_name=data['patient_name'],
            content=data['content'],
            rating=data['rating']
        )
        
        # Add to the session and commit
        db.session.add(testimonial)
        db.session.commit()
        
        return jsonify({"message": "Testimonial submitted successfully"}), 201

    except IntegrityError:
        db.session.rollback()
        logging.error("Database integrity error occurred")
        return jsonify({"error": "Database integrity error"}), 500
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages with:
```bash
pip install Flask Flask-SQLAlchemy
```
