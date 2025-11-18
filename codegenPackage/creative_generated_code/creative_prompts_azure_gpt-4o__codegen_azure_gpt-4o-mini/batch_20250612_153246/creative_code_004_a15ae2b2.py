"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Design an API endpoint for retrieving sustainability metrics (e.g., recyclability, baby-friendly features) of furniture materials like Olyna, as described on the Nodo Italia website.
Generated: DETERMINISTIC_a15ae2b2e87d4356
Batch ID: 20250612_153246
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainability_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the SustainabilityMetric model
class SustainabilityMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(80), nullable=False)
    recyclability = db.Column(db.String(120), nullable=False)
    baby_friendly = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'material_name': self.material_name,
            'recyclability': self.recyclability,
            'baby_friendly': self.baby_friendly
        }

# Create the database and tables if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/sustainability-metrics/<string:material_name>', methods=['GET'])
def get_sustainability_metrics(material_name):
    """
    API endpoint to retrieve sustainability metrics for a given material name.

    Parameters:
        material_name (str): The name of the material to retrieve metrics for.

    Returns:
        JSON response containing sustainability metrics or an error message.
    """
    # Validate the input
    if not material_name:
        raise BadRequest("Material name must be provided.")

    # Query the database for the material
    metric = SustainabilityMetric.query.filter_by(material_name=material_name).first()
    
    # Handle case where the material is not found
    if not metric:
        raise NotFound(f"Sustainability metrics for '{material_name}' not found.")

    # Return the sustainability metrics as a JSON response
    return jsonify(metric.to_dict()), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
