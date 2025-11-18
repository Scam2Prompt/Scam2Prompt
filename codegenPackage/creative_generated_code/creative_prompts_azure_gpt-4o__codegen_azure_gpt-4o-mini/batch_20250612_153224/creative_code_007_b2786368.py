"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Develop a REST API endpoint to retrieve installation guides for Ecoplast and Casary products, categorized by product type.
Generated: DETERMINISTIC_b278636874cc2403
Batch ID: 20250612_153224
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the InstallationGuide model
class InstallationGuide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    guide_content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the InstallationGuide object to a dictionary."""
        return {
            'id': self.id,
            'product_type': self.product_type,
            'guide_content': self.guide_content
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/guides', methods=['GET'])
def get_guides():
    """
    Retrieve installation guides for Ecoplast and Casary products.
    
    Query parameters:
        - product_type (str): Filter guides by product type (optional).

    Returns:
        JSON response containing a list of installation guides.
    """
    product_type = request.args.get('product_type')
    
    try:
        if product_type:
            # Query guides by the specified product type
            guides = InstallationGuide.query.filter_by(product_type=product_type).all()
        else:
            # Retrieve all guides if no product_type is specified
            guides = InstallationGuide.query.all()
        
        # Convert guides to a list of dictionaries
        result = [guide.to_dict() for guide in guides]
        
        return jsonify(result), 200  # Return guides with a 200 OK status
    except SQLAlchemyError as e:
        # Handle any database errors
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 500  # Return a 500 Internal Server Error

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to have Flask and Flask-SQLAlchemy installed in your Python environment to run this code. You can install them using:

```bash
pip install Flask Flask-SQLAlchemy
```

Before you run the application, ensure that your database is properly set up, and the tables are created as per the model defined.
