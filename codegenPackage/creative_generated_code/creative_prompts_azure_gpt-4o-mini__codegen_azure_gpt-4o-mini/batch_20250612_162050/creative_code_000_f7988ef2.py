"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Generate a code snippet for a web application that allows users to reserve a lot in Baranoa with a down payment of $500,000 and flexible payment plans.
Generated: DETERMINISTIC_f7988ef2721a5d5a
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baranoa_reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    """Model representing a lot reservation."""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    down_payment = db.Column(db.Integer, nullable=False)
    payment_plan = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Reservation {self.id} - {self.user_name}>'

@app.route('/reserve', methods=['POST'])
def reserve_lot():
    """Endpoint to allow users to reserve a lot with a down payment."""
    data = request.json

    # Input validation
    if 'user_name' not in data or 'payment_plan' not in data:
        return jsonify({'error': 'Invalid input. Please provide user_name and payment_plan.'}), 400

    user_name = data['user_name']
    payment_plan = data['payment_plan']

    # Down payment constant
    DOWN_PAYMENT = 500000

    # Creating a new reservation
    new_reservation = Reservation(user_name=user_name, down_payment=DOWN_PAYMENT, payment_plan=payment_plan)

    try:
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({'message': 'Reservation successful!', 'reservation_id': new_reservation.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to reserve lot. Please try again later.'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
```
