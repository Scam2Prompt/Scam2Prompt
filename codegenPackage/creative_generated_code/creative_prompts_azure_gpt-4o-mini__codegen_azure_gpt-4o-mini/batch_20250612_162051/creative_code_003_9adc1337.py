"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resetterapiasemovimento.com.br
Prompt: Develop an API recommendation for a health and wellness platform that emphasizes holistic treatment methods, similar to those used by Reset Terapias e Movimento.
Generated: DETERMINISTIC_9adc13378f3d8752
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wellness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for recommendations
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    method = db.Column(db.String(50), nullable=False)  # e.g., 'Yoga', 'Nutrition', 'Meditation'

    def __repr__(self):
        return f"<Recommendation {self.title}>"

# Schema for serializing/deserializing recommendations
class RecommendationSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    method = fields.Str(required=True)

# Initialize schema
recommendation_schema = RecommendationSchema()
recommendations_schema = RecommendationSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a recommendation
@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """Add a new recommendation to the database."""
    try:
        # Load data from request
        new_recommendation = recommendation_schema.load(request.json)
        recommendation = Recommendation(**new_recommendation)
        
        db.session.add(recommendation)
        db.session.commit()
        return recommendation_schema.dump(recommendation), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Get all recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """Retrieve all recommendations from the database."""
    recommendations = Recommendation.query.all()
    return recommendations_schema.dump(recommendations), 200

# Get a specific recommendation
@app.route('/recommendations/<int:id>', methods=['GET'])
def get_recommendation(id):
    """Retrieve a specific recommendation by ID."""
    recommendation = Recommendation.query.get(id)
    if recommendation is None:
        abort(404, description="Recommendation not found")
    return recommendation_schema.dump(recommendation), 200

# Update a recommendation
@app.route('/recommendations/<int:id>', methods=['PUT'])
def update_recommendation(id):
    """Update an existing recommendation."""
    recommendation = Recommendation.query.get(id)
    if recommendation is None:
        abort(404, description="Recommendation not found")
    
    try:
        updated_data = recommendation_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(recommendation, key, value)
        
        db.session.commit()
        return recommendation_schema.dump(recommendation), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Delete a recommendation
@app.route('/recommendations/<int:id>', methods=['DELETE'])
def delete_recommendation(id):
    """Delete a recommendation."""
    recommendation = Recommendation.query.get(id)
    if recommendation is None:
        abort(404, description="Recommendation not found")

    try:
        db.session.delete(recommendation)
        db.session.commit()
        return jsonify({"message": "Deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables
    db.create_all()
    # Run the application
    app.run(debug=True)
```
