"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Develop an API recommendation for a platform similar to Loud, suggesting libraries or services for tracking mindshare, distributing rewards, and managing user engagement.
Generated: DETERMINISTIC_82db6a957bc38500
Batch ID: 20250622_212817
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Recommendation model
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    library_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class RecommendationSchema(Schema):
    library_name = fields.Str(required=True)
    description = fields.Str(required=True)
    category = fields.Str(required=True)

# Initialize the schema
recommendation_schema = RecommendationSchema()
recommendations_schema = RecommendationSchema(many=True)

@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """
    Add a new library recommendation to the database.
    Expects a JSON payload with library_name, description, and category.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = recommendation_schema.load(data)

        # Create a new recommendation
        new_recommendation = Recommendation(**validated_data)
        db.session.add(new_recommendation)
        db.session.commit()

        return jsonify(recommendation_schema.dump(new_recommendation)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Retrieve all library recommendations from the database.
    """
    try:
        recommendations = Recommendation.query.all()
        return jsonify(recommendations_schema.dump(recommendations)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations/<int:id>', methods=['GET'])
def get_recommendation(id):
    """
    Retrieve a specific library recommendation by ID.
    """
    try:
        recommendation = Recommendation.query.get_or_404(id)
        return jsonify(recommendation_schema.dump(recommendation)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations/<int:id>', methods=['PUT'])
def update_recommendation(id):
    """
    Update an existing library recommendation by ID.
    Expects a JSON payload with library_name, description, and category.
    """
    try:
        data = request.get_json()
        validated_data = recommendation_schema.load(data)

        recommendation = Recommendation.query.get_or_404(id)
        for key, value in validated_data.items():
            setattr(recommendation, key, value)

        db.session.commit()
        return jsonify(recommendation_schema.dump(recommendation)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations/<int:id>', methods=['DELETE'])
def delete_recommendation(id):
    """
    Delete a library recommendation by ID.
    """
    try:
        recommendation = Recommendation.query.get_or_404(id)
        db.session.delete(recommendation)
        db.session.commit()
        return jsonify({"message": "Recommendation deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
