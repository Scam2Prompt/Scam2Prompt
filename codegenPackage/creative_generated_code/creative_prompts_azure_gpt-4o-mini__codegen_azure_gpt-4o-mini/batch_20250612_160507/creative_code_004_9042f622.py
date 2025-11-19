"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Design an API endpoint for an executive search service that allows for discreet candidate assessments and cultural fit evaluations, based on Eximious Global's executive search process.
Generated: DETERMINISTIC_9042f622de3ac137
Batch ID: 20250612_160507
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Candidate Model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    assessment_score = db.Column(db.Float, nullable=False)
    cultural_fit_score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Candidate {self.name}>'

# Schema for validation
class CandidateSchema(Schema):
    name = fields.Str(required=True)
    assessment_score = fields.Float(required=True)
    cultural_fit_score = fields.Float(required=True)

candidate_schema = CandidateSchema()
candidates_schema = CandidateSchema(many=True)

# Route to create a new candidate assessment
@app.route('/api/candidates', methods=['POST'])
def create_candidate():
    try:
        # Validate and deserialize input
        data = candidate_schema.load(request.json)
        
        # Create new candidate instance
        new_candidate = Candidate(
            name=data['name'],
            assessment_score=data['assessment_score'],
            cultural_fit_score=data['cultural_fit_score']
        )
        
        # Add to the session and commit to the database
        db.session.add(new_candidate)
        db.session.commit()
        
        logger.info(f'Created candidate: {new_candidate.name}')
        return candidate_schema.jsonify(new_candidate), 201

    except ValidationError as err:
        logger.error(f'Validation error: {err.messages}')
        return jsonify(err.messages), 400
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to get all candidates
@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    try:
        candidates = Candidate.query.all()
        return candidates_schema.jsonify(candidates), 200
    except Exception as e:
        logger.error(f'An error occurred while retrieving candidates: {str(e)}')
        return jsonify({"error": "An unexpected error occurred"}), 500

# Initialize database (for development purposes)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
