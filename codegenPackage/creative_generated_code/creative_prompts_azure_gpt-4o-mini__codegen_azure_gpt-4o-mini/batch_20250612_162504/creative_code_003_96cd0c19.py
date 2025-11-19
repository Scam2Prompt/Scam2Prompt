"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Develop a RESTful API endpoint that allows users to search for modern homes in Estepona, including parameters for budget and desired features like underground parking.
Generated: DETERMINISTIC_96cd0c19bbfefeca
Batch ID: 20250612_162504
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for the modern homes
class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    features = db.Column(db.String(200), nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'price': self.price,
            'features': self.features.split(',') if self.features else []
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/homes', methods=['GET'])
def search_homes():
    """
    Search for modern homes in Estepona based on budget and desired features.
    Query Parameters:
    - max_price: Maximum budget for the home (float).
    - features: Comma-separated list of desired features (string).
    
    Returns:
    - A JSON array of homes that match the criteria.
    """
    max_price = request.args.get('max_price', default=float('inf'), type=float)
    features = request.args.get('features', type=str)

    # Build the query to fetch homes
    query = Home.query.filter(Home.location == 'Estepona', Home.price <= max_price)

    if features:
        feature_list = [feature.strip() for feature in features.split(',')]
        query = query.filter(Home.features.ilike('%' + '%'.join(feature_list) + '%'))

    try:
        homes = query.all()
        return jsonify([home.as_dict() for home in homes]), 200
    except SQLAlchemyError as e:
        # Log the error message for debugging purposes (logging not implemented here)
        return jsonify({'error': 'Database query failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
