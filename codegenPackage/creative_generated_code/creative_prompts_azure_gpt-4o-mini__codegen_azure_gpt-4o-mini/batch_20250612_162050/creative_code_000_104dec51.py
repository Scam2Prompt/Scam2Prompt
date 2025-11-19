"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Generate a code snippet that allows users to book a car rental online without a credit card or deposit, similar to the process described on Rental Car Elena's website.
Generated: DETERMINISTIC_104dec511683901e
Batch ID: 20250612_162050
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
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Rental model
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    car_model = db.Column(db.String(100), nullable=False)
    rental_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/book', methods=['POST'])
def book_rental():
    """
    Book a car rental without a credit card or deposit.
    
    Expects JSON payload with the following fields:
    - user_name: str
    - car_model: str
    - rental_date: str (ISO format)
    - return_date: str (ISO format)
    
    Returns a confirmation message or an error message.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not all(key in data for key in ('user_name', 'car_model', 'rental_date', 'return_date')):
            return jsonify({"error": "Missing required fields."}), 400
        
        user_name = data['user_name']
        car_model = data['car_model']
        
        # Parse dates and validate
        rental_date = datetime.fromisoformat(data['rental_date'])
        return_date = datetime.fromisoformat(data['return_date'])
        
        if rental_date >= return_date:
            return jsonify({"error": "Return date must be after rental date."}), 400

        # Create a new rental record
        new_rental = Rental(
            user_name=user_name,
            car_model=car_model,
            rental_date=rental_date,
            return_date=return_date
        )
        
        db.session.add(new_rental)
        db.session.commit()
        
        return jsonify({"message": "Rental booked successfully!"}), 201
        
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
