"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Create an API endpoint that provides users with personalized recommendations for corrective lenses based on their vision issues, inspired by the offerings of Optic Alizé.
Generated: DETERMINISTIC_0221031b146c22bd
Batch ID: 20250612_164304
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing user vision issues and recommendations
class VisionRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.String(100), nullable=False)
    recommendation = db.Column(db.String(200), nullable=False)

    def as_dict(self):
        return {'issue': self.issue, 'recommendation': self.recommendation}

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint to provide personalized recommendations for corrective lenses
    based on user-provided vision issues.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'issue' not in data:
        return jsonify({'error': 'No vision issue provided'}), 400

    issue = data['issue']
    
    # Fetch the recommendation from the database
    recommendation = VisionRecommendation.query.filter_by(issue=issue).first()
    
    # If no recommendation exists, return a not found error
    if recommendation is None:
        return jsonify({'error': 'No recommendations found for this issue'}), 404
    
    return jsonify(recommendation.as_dict()), 200

@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """
    Endpoint to add a new vision issue and its corresponding recommendation.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'issue' not in data or 'recommendation' not in data:
        return jsonify({'error': 'Issue and recommendation must be provided'}), 400
    
    new_recommendation = VisionRecommendation(issue=data['issue'], recommendation=data['recommendation'])
    
    try:
        db.session.add(new_recommendation)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Recommendation already exists'}), 409
    
    return jsonify(new_recommendation.as_dict()), 201

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
