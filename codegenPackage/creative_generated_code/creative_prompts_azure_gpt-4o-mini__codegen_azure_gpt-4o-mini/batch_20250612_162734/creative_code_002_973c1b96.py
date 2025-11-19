"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create an API endpoint that retrieves details about various "aparelhagem" tools and their specifications for a construction application.
Generated: DETERMINISTIC_973c1b96bb646860
Batch ID: 20250612_162734
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

# Configure the database connection (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aparelhagem.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Aparelho model
class Aparelho(db.Model):
    __tablename__ = 'aparelhos'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specification = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specification': self.specification
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve all aparelhos
@app.route('/api/aparelhagem', methods=['GET'])
def get_aparelhos():
    try:
        # Query all aparelhos and convert them to a list of dictionaries
        aparelhos = Aparelho.query.all()
        return jsonify([aparelho.to_dict() for aparelho in aparelhos]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
