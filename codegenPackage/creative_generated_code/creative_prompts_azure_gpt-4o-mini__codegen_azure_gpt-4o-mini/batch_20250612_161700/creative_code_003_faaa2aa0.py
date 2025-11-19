"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geddesign.it
Prompt: Create an API endpoint for retrieving details about high-quality, restored sofas, including their materials and design inspirations.
Generated: DETERMINISTIC_faaa2aa091885ad4
Batch ID: 20250612_161700
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

# Configure the database connection (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sofas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Sofa model representing the sofas table in the database
class Sofa(db.Model):
    __tablename__ = 'sofas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    materials = db.Column(db.String(255), nullable=False)
    design_inspiration = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the Sofa model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'materials': self.materials,
            'design_inspiration': self.design_inspiration
        }

# Route to retrieve all high-quality restored sofas
@app.route('/api/sofas', methods=['GET'])
def get_sofas():
    try:
        sofas = Sofa.query.all()  # Query all sofas from the database
        return jsonify([sofa.to_dict() for sofa in sofas]), 200  # Return the list of sofas in JSON format
    except SQLAlchemyError as e:
        # Handle any database errors during the query
        return jsonify({'error': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point of the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=False)
```
