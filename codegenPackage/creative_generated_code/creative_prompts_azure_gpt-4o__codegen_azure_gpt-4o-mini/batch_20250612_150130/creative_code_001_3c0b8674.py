"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Recommend libraries or APIs for building a web content discovery app that allows users to submit, rate, and share their favorite web finds, as described on the Stumble! ® website.
Generated: DETERMINISTIC_3c0b86740e9ca4f1
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries for a web content discovery app
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create a model for user submissions
class WebFind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Integer, default=0)

# Create a schema for input validation
class WebFindSchema(Schema):
    url = fields.String(required=True)
    description = fields.String(required=False)
    rating = fields.Integer(required=False)

# Initialize schema
webfind_schema = WebFindSchema()
webfinds_schema = WebFindSchema(many=True)

# Endpoint to submit a new web find
@app.route('/api/webfinds', methods=['POST'])
def add_webfind():
    try:
        # Validate and deserialize input
        data = webfind_schema.load(request.json)
        new_find = WebFind(**data)
        db.session.add(new_find)
        db.session.commit()
        return webfind_schema.dump(new_find), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all web finds
@app.route('/api/webfinds', methods=['GET'])
def get_webfinds():
    try:
        webfinds = WebFind.query.all()
        return webfinds_schema.dump(webfinds), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to rate a web find
@app.route('/api/webfinds/<int:id>/rate', methods=['PUT'])
def rate_webfind(id):
    try:
        # Get the rating from request
        rating = request.json.get('rating', 0)
        if not isinstance(rating, int) or not (0 <= rating <= 5):
            return jsonify({"error": "Rating must be an integer between 0 and 5"}), 400

        # Find the web find by ID
        webfind = WebFind.query.get_or_404(id)
        webfind.rating = rating
        db.session.commit()
        return webfind_schema.dump(webfind), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
