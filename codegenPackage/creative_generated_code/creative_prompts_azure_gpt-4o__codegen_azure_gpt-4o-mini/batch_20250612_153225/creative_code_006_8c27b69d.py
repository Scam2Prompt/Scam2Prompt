"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Recommend tools or libraries for implementing video consultations for nutritionists, similar to the "Video Reception 'Top 5'" service offered by Olga Stepanova.
Generated: DETERMINISTIC_8c27b69dee2a9413
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nutritionist_id = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.String(50), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/consultation', methods=['POST'])
def schedule_consultation():
    """Schedule a new video consultation"""
    data = request.get_json()

    try:
        # Validate required fields
        nutritionist_id = data['nutritionist_id']
        client_id = data['client_id']
        scheduled_time = datetime.fromisoformat(data['scheduled_time'])
        
        # Create a new consultation entry
        new_consultation = Consultation(nutritionist_id=nutritionist_id, client_id=client_id, scheduled_time=scheduled_time)
        db.session.add(new_consultation)
        db.session.commit()

        return jsonify({'message': 'Consultation scheduled successfully!', 'id': new_consultation.id}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Consultation scheduling failed due to integrity error.'}), 500
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use ISO format.'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/consultation/<int:consultation_id>', methods=['GET'])
def get_consultation(consultation_id):
    """Get details of a scheduled consultation"""
    consultation = Consultation.query.get(consultation_id)

    if consultation:
        return jsonify({
            'id': consultation.id,
            'nutritionist_id': consultation.nutritionist_id,
            'client_id': consultation.client_id,
            'scheduled_time': consultation.scheduled_time.isoformat()
        }), 200
    else:
        return jsonify({'error': 'Consultation not found.'}), 404

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
