"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Create an API endpoint for a consultancy service that allows users to submit project ideas and request tailored solutions, reflecting the custom consultancy approach of Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_1ed052b79a7aa1af
Batch ID: 20250612_162945
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
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (Change this URI to your database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultancy_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the ProjectIdea model
class ProjectIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    idea_description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'idea_description': self.idea_description,
            'created_at': self.created_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

# API endpoint to submit project ideas
@app.route('/api/project-ideas', methods=['POST'])
def submit_project_idea():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input
        if 'user_name' not in data or 'idea_description' not in data:
            return jsonify({'error': 'Missing user_name or idea_description'}), 400

        # Create a new project idea
        new_idea = ProjectIdea(
            user_name=data['user_name'],
            idea_description=data['idea_description']
        )
        db.session.add(new_idea)
        db.session.commit()

        logger.info(f"New project idea submitted by {new_idea.user_name}")

        # Respond with the created idea
        return jsonify(new_idea.to_dict()), 201

    except Exception as e:
        logger.error(f"Error submitting project idea: {e}")
        return jsonify({'error': 'An error occurred while submitting the project idea'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
