"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Develop a REST API endpoint that allows users to query herbal supplement products, specifically those containing Habbatussauda, and return their health benefits and customer reviews.
Generated: DETERMINISTIC_5dc86e64c8a4aa1d
Batch ID: 20250612_164000
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

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///herbal_supplements.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define the HerbalSupplement model
class HerbalSupplement(db.Model):
    __tablename__ = 'herbal_supplements'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    reviews = db.Column(db.Text, nullable=True)

    def serialize(self):
        """Convert the object into a JSON serializable format."""
        return {
            'id': self.id,
            'name': self.name,
            'benefits': self.benefits,
            'reviews': self.reviews.split(';') if self.reviews else []
        }

# Create the database and tables (if they don't exist)
@app.before_first_request
def create_tables():
    db.create_all()

# REST API endpoint to query herbal supplements containing Habbatussauda
@app.route('/api/supplements/habbatussauda', methods=['GET'])
def get_habbatussauda_supplements():
    try:
        # Query the database for supplements containing Habbatussauda
        supplements = HerbalSupplement.query.filter(HerbalSupplement.name.contains('Habbatussauda')).all()

        # Serialize the results
        results = [supplement.serialize() for supplement in supplements]

        # Return the results as JSON
        return jsonify(results), 200
        
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify(error=str(e)), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify(error=str(e)), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
