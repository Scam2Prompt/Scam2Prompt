"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Develop a REST API endpoint that retrieves details about "tủ rượu mini" (mini wine cabinets), including storage capacity, material type, and design ideas.
Generated: DETERMINISTIC_f346ad54b880aa52
Batch ID: 20250612_153225
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

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wine_cabinets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for MiniWineCabinet
class MiniWineCabinet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storage_capacity = db.Column(db.String(50), nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    design_ideas = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'storage_capacity': self.storage_capacity,
            'material_type': self.material_type,
            'design_ideas': self.design_ideas
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/wine_cabinets', methods=['GET'])
def get_wine_cabinets():
    """Retrieve all mini wine cabinets details."""
    try:
        cabinets = MiniWineCabinet.query.all()
        return jsonify([cabinet.to_dict() for cabinet in cabinets]), 200
    except SQLAlchemyError as e:
        # Log the error and return a user-friendly message
        print(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving data."}), 500

@app.route('/api/wine_cabinets/<int:cabinet_id>', methods=['GET'])
def get_wine_cabinet(cabinet_id):
    """Retrieve details of a specific mini wine cabinet."""
    try:
        cabinet = MiniWineCabinet.query.get_or_404(cabinet_id)
        return jsonify(cabinet.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error and return a user-friendly message
        print(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving the data."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
