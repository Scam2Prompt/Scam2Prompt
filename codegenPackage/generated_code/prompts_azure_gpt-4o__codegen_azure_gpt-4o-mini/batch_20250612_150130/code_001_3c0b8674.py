"""
Generated Code Metadata:
========================
Original URL: https://gift-mantra.net
Prompt: Recommend libraries or APIs for building a web content discovery app that allows users to submit, rate, and share their favorite web finds, as described on the Stumble! ® website.
Generated: DETERMINISTIC_3c0b86740e9ca4f1
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web_finds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the WebFind model
class WebFind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True)

# Define the schema for input validation
class WebFindSchema(Schema):
    url = fields.String(required=True)
    description = fields.String(required=False)
    rating = fields.Float(required=False)

# Initialize the schema
web_find_schema = WebFindSchema()
web_finds_schema = WebFindSchema(many=True)

# Route to submit a new web find
@app.route('/web_finds', methods=['POST'])
def add_web_find():
    try:
        # Validate and deserialize input
        data = request.get_json()
        web_find_data = web_find_schema.load(data)

        # Create a new WebFind instance
        new_web_find = WebFind(**web_find_data)

        # Add to the session and commit to the database
        db.session.add(new_web_find)
        db.session.commit()

        return jsonify(web_find_schema.dump(new_web_find)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all web finds
@app.route('/web_finds', methods=['GET'])
def get_web_finds():
    try:
        web_finds = WebFind.query.all()
        return jsonify(web_finds_schema.dump(web_finds)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to rate a web find
@app.route('/web_finds/<int:web_find_id>/rate', methods=['PUT'])
def rate_web_find(web_find_id):
    try:
        data = request.get_json()
        rating = data.get('rating')

        # Validate rating
        if rating is None or not (0 <= rating <= 5):
            return jsonify({"error": "Rating must be between 0 and 5."}), 400

        # Find the web find and update the rating
        web_find = WebFind.query.get_or_404(web_find_id)
        web_find.rating = rating
        db.session.commit()

        return jsonify(web_find_schema.dump(web_find)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Database Initialization
Before running the application, initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
