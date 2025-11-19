"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donaldjtrumclaim.pages.dev
Prompt: Create a REST API that allows users to submit their ideas for restoring free speech and dismantling censorship, inspired by Donald J. Trump's free speech policy initiative.
Generated: DETERMINISTIC_be7b7a4779a7ab8d
Batch ID: 20250612_163408
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
import os

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ideas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Idea model
class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        # Convert the Idea object to a dictionary
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit a new idea
@app.route('/ideas', methods=['POST'])
def submit_idea():
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({'error': 'Title and description are required.'}), 400
        
        # Create a new Idea instance
        new_idea = Idea(title=data['title'], description=data['description'])
        db.session.add(new_idea)
        db.session.commit()
        
        return jsonify(new_idea.to_dict()), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while saving the idea.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all submitted ideas
@app.route('/ideas', methods=['GET'])
def get_ideas():
    try:
        ideas = Idea.query.all()
        return jsonify([idea.to_dict() for idea in ideas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
