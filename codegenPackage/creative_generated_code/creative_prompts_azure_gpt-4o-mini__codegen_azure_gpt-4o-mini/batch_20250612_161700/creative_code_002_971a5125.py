"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Create an API endpoint that allows users to filter Pakistani ethnic wear by occasion, such as weddings or casual outings, similar to the categorization on Multan Designs.
Generated: DETERMINISTIC_971a51256da5a06b
Batch ID: 20250612_161700
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ethnic_wear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Ethnic Wear
class EthnicWear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occasion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the EthnicWear object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'occasion': self.occasion
        }

# Endpoint to filter ethnic wear by occasion
@app.route('/api/ethnicwear', methods=['GET'])
def get_ethnic_wear_by_occasion():
    """Fetch ethnic wear items filtered by occasion."""
    # Get the occasion parameter from query string
    occasion = request.args.get('occasion')
    
    if not occasion:
        return jsonify({"error": "Occasion query parameter is required."}), 400

    try:
        # Query the database for ethnic wear items that match the requested occasion
        results = EthnicWear.query.filter_by(occasion=occasion).all()
        
        # Convert results to a list of dictionaries
        items = [item.to_dict() for item in results]
        
        # Return the filtered list as JSON
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database and create sample data for testing
@app.before_first_request
def create_tables():
    """Create database tables and add sample data if they don't exist."""
    db.create_all()
    
    if EthnicWear.query.count() == 0:  # Check if data already exists
        sample_data = [
            EthnicWear(name='Traditional Sherwani', occasion='wedding'),
            EthnicWear(name='Casual Kurta', occasion='casual'),
            EthnicWear(name='Fancy Lehenga', occasion='wedding'),
            EthnicWear(name='Simple Shalwar Kameez', occasion='casual')
        ]
        db.session.bulk_save_objects(sample_data)
        db.session.commit()

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
