"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Develop a RESTful API endpoint that retrieves information about different safari experiences in Tanzania, including mid-range and luxury options, and formats the data for a mobile app.
Generated: DETERMINISTIC_ca102ea597463df8
Batch ID: 20250612_164122
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

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safari_experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing safari experience data
class SafariExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_range = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    accommodation_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price_range': self.price_range,
            'description': self.description,
            'accommodation_type': self.accommodation_type
        }

# Initialize the database and create a sample data
@app.before_first_request
def create_tables():
    db.create_all()
    # Uncomment below to add sample data only once
    # if SafariExperience.query.count() == 0:
    #     sample_data = [
    #         SafariExperience(name='Serengeti Safari', price_range='Mid-range', 
    #                          description='Experience the great migration.', accommodation_type='Tent'),
    #         SafariExperience(name='Ngorongoro Crater Safari', price_range='Luxury', 
    #                          description='Explore the unique wildlife in the crater.', accommodation_type='Lodge'),
    #     ]
    #     db.session.bulk_save_objects(sample_data)
    #     db.session.commit()

@app.route('/api/safari_experiences', methods=['GET'])
def get_safari_experiences():
    """
    Retrieve a list of safari experiences based on price range filter.
    Query parameters:
        - price_range: Filter results by 'mid-range' or 'luxury'.
    Returns a JSON response with safari experiences.
    """
    price_range = request.args.get('price_range')
    try:
        if price_range:
            experiences = SafariExperience.query.filter_by(price_range=price_range.capitalize()).all()
        else:
            experiences = SafariExperience.query.all()
        
        # Convert results to a list of dictionaries
        return jsonify([experience.to_dict() for experience in experiences]), 200

    except SQLAlchemyError as e:
        # Log the error and respond with an appropriate message
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while fetching safari experiences."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
