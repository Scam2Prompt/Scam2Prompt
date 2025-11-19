"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Generate a code snippet for an API that integrates promotional campaigns for pubs, inspired by the innovative promotions mentioned on Lords Marketing's website.
Generated: DETERMINISTIC_a0da0b8f39f84539
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
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pub_promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Promotion model
class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Promotion {self.pub_name}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/promotions', methods=['POST'])
def create_promotion():
    """
    Create a new promotional campaign for a pub.
    Expects JSON data with pub_name, description, start_date, and end_date.
    """
    try:
        data = request.get_json()
        pub_name = data['pub_name']
        description = data['description']
        start_date = datetime.fromisoformat(data['start_date'])
        end_date = datetime.fromisoformat(data['end_date'])

        # Validate dates
        if start_date >= end_date:
            return jsonify({"error": "Start date must be before end date."}), 400

        # Create a new promotion
        new_promotion = Promotion(pub_name=pub_name, description=description,
                                  start_date=start_date, end_date=end_date)
        db.session.add(new_promotion)
        db.session.commit()

        return jsonify({"message": "Promotion created successfully!", "id": new_promotion.id}), 201

    except KeyError as e:
        logging.error(f"Missing key: {e}")
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        logging.error(f"Error creating promotion: {e}")
        return jsonify({"error": "An error occurred while creating the promotion."}), 500

@app.route('/promotions', methods=['GET'])
def get_promotions():
    """
    Retrieve all active promotions for pubs.
    """
    try:
        current_time = datetime.now()
        promotions = Promotion.query.filter(Promotion.start_date <= current_time,
                                            Promotion.end_date >= current_time).all()
        return jsonify([{
            "id": promo.id,
            "pub_name": promo.pub_name,
            "description": promo.description,
            "start_date": promo.start_date.isoformat(),
            "end_date": promo.end_date.isoformat()
        } for promo in promotions]), 200

    except Exception as e:
        logging.error(f"Error retrieving promotions: {e}")
        return jsonify({"error": "An error occurred while retrieving promotions."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
