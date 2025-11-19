"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetserfi.pages.dev
Prompt: How can I leverage the PLANET ecosystem to promote gender equality through a web application?
Generated: DETERMINISTIC_a89be62510a7a61b
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for API

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///gender_equality.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the GenderEquality model
class GenderEquality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    initiative_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    impact = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Initiative {self.initiative_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new initiative
@app.route('/initiatives', methods=['POST'])
def create_initiative():
    try:
        data = request.get_json()
        new_initiative = GenderEquality(
            initiative_name=data['initiative_name'],
            description=data['description'],
            impact=data['impact']
        )
        db.session.add(new_initiative)
        db.session.commit()
        return jsonify({'message': 'Initiative created successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 400

# Endpoint to get all initiatives
@app.route('/initiatives', methods=['GET'])
def get_initiatives():
    try:
        initiatives = GenderEquality.query.all()
        return jsonify([{
            'id': initiative.id,
            'initiative_name': initiative.initiative_name,
            'description': initiative.description,
            'impact': initiative.impact
        } for initiative in initiatives]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', False), host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### Instructions to Run the Application
1. Ensure Python and Flask are installed.
2. Set the environment variable `DATABASE_URL` for your database connection (optional, defaults to SQLite).
3. Install required packages: 
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Cors
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Use an API client like Postman to interact with the endpoints for creating and retrieving initiatives promoting gender equality.
