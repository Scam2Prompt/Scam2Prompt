"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Recommend an API for managing compressor rental services, incorporating features like availability checks and pricing, as outlined on the Só Compressores e Bombas site.
Generated: DETERMINISTIC_892c673c72406cf6
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///compressor_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Compressors
class Compressor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Compressor {self.model}>'

# Initialize the database (only for demonstration; use migrations in production)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to check availability of compressors
@app.route('/api/compressors/availability', methods=['GET'])
def check_availability():
    """Check availability of compressors."""
    compressors = Compressor.query.filter_by(available=True).all()
    return jsonify({'available_compressors': [c.model for c in compressors]}), 200

# API endpoint to get pricing of a specific compressor
@app.route('/api/compressors/<int:compressor_id>/price', methods=['GET'])
def get_price(compressor_id):
    """Get price of a specific compressor."""
    compressor = Compressor.query.get(compressor_id)
    if compressor is None:
        return jsonify({'error': 'Compressor not found'}), 404
    return jsonify({'model': compressor.model, 'price_per_day': compressor.price_per_day}), 200

# API endpoint to rent a compressor
@app.route('/api/compressors/rent', methods=['POST'])
def rent_compressor():
    """Rent a compressor."""
    data = request.json
    compressor_id = data.get('compressor_id')
    rental_days = data.get('rental_days', 1)

    # Validate input
    if not compressor_id or not isinstance(rental_days, int):
        return jsonify({'error': 'Invalid input'}), 400

    compressor = Compressor.query.get(compressor_id)
    if compressor is None:
        return jsonify({'error': 'Compressor not found'}), 404
    if not compressor.available:
        return jsonify({'error': 'Compressor not available'}), 400

    # Mark compressor as rented
    compressor.available = False
    db.session.commit()

    total_price = compressor.price_per_day * rental_days
    return jsonify({'message': 'Compressor rented successfully', 'total_price': total_price}), 200

# API endpoint to return a rented compressor (mocking return)
@app.route('/api/compressors/return', methods=['POST'])
def return_compressor():
    """Return a rented compressor."""
    data = request.json
    compressor_id = data.get('compressor_id')

    # Validate input
    if not compressor_id:
        return jsonify({'error': 'Invalid input'}), 400

    compressor = Compressor.query.get(compressor_id)
    if compressor is None:
        return jsonify({'error': 'Compressor not found'}), 404

    # Mark compressor as available
    compressor.available = True
    db.session.commit()

    return jsonify({'message': 'Compressor returned successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to install Flask and Flask-SQLAlchemy before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
