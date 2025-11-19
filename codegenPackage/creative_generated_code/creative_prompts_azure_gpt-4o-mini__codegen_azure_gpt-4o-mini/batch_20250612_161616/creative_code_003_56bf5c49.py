"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Develop a REST API endpoint that allows users to retrieve information about different Bentô Cake options, including pricing and customization features.
Generated: DETERMINISTIC_56bf5c499e2f041e
Batch ID: 20250612_161616
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLAlchemy (e.g., SQLite for development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bento_cakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Bentô Cake model
class BentoCake(db.Model):
    __tablename__ = 'bento_cakes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    customization_options = db.Column(db.String(500), nullable=True)

    def serialize(self):
        """Serialize the Bento Cake object for JSON output."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'customization_options': self.customization_options.split(',') if self.customization_options else []
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/bento-cakes', methods=['GET'])
def get_bento_cakes():
    """Retrieve all Bentô Cake options."""
    try:
        cakes = BentoCake.query.all()
        return jsonify([cake.serialize() for cake in cakes]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/bento-cakes/<int:cake_id>', methods=['GET'])
def get_bento_cake(cake_id):
    """Retrieve a specific Bentô Cake by ID."""
    try:
        cake = BentoCake.query.get(cake_id)
        if cake is None:
            return jsonify({'error': 'Bento Cake not found'}), 404
        return jsonify(cake.serialize()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
