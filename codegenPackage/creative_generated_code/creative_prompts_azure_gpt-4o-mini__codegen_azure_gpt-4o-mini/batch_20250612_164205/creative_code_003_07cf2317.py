"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Develop a RESTful API endpoint that allows users to search for automotive parts, referencing the unique features of Gnosis Rew's product offerings.
Generated: DETERMINISTIC_07cf2317fda46c78
Batch ID: 20250612_164205
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automotive_parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for automotive parts
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    unique_features = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert Part object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "unique_features": self.unique_features
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/parts/search', methods=['GET'])
def search_parts():
    """Search for automotive parts based on query parameters."""
    query = request.args.get('query', '').lower()
    category = request.args.get('category', '').lower()

    try:
        # Query the database for matching parts
        results = Part.query.filter(
            (Part.name.ilike(f'%{query}%')) | 
            (Part.description.ilike(f'%{query}%'))
        )

        if category:
            results = results.filter(Part.category.ilike(f'%{category}%'))

        # Convert results to a list of dictionaries
        parts = [part.to_dict() for part in results.all()]

        return jsonify(parts), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Important Notes:
- Ensure that you have Flask and Flask-SQLAlchemy installed in your environment.
- You can install them via pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- The database is configured to use SQLite for simplicity; modify as necessary for production use.
- This code includes a search endpoint at `/api/parts/search` to query automotive parts.
