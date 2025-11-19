"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Design an API endpoint for retrieving sustainability metrics (e.g., recyclability, baby-friendly features) of furniture materials like Olyna, as described on the Nodo Italia website.
Generated: DETERMINISTIC_a15ae2b2e87d4356
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainability_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SustainabilityMetric model
class SustainabilityMetric(db.Model):
    __tablename__ = 'sustainability_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(100), nullable=False)
    recyclability = db.Column(db.String(50), nullable=False)
    baby_friendly = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'material_name': self.material_name,
            'recyclability': self.recyclability,
            'baby_friendly': self.baby_friendly
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/sustainability_metrics/<string:material_name>', methods=['GET'])
def get_sustainability_metrics(material_name):
    """
    Retrieve sustainability metrics for a specific material.
    
    Args:
        material_name (str): The name of the material to retrieve metrics for.
    
    Returns:
        JSON response containing sustainability metrics or an error message.
    """
    try:
        # Query the database for the specified material
        metric = SustainabilityMetric.query.filter_by(material_name=material_name).first()
        
        if metric is None:
            return jsonify({'error': 'Material not found'}), 404
        
        return jsonify(metric.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
