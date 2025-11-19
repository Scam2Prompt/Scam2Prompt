"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Create a REST API that provides resources and FAQs for young leaders, inspired by the content structure of the UngLeder site.
Generated: DETERMINISTIC_cbb339360451eeba
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///young_leaders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'link': self.link}

# Define the FAQ model
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'question': self.question, 'answer': self.answer}

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """Get a list of all resources."""
    resources = Resource.query.all()
    return jsonify([resource.to_dict() for resource in resources]), 200

# Route to create a new resource
@app.route('/api/resources', methods=['POST'])
def create_resource():
    """Create a new resource."""
    data = request.get_json()
    new_resource = Resource(title=data['title'], link=data['link'])
    
    try:
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(new_resource.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Resource creation failed due to integrity error."}), 400

# Route to get all FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    """Get a list of all FAQs."""
    faqs = FAQ.query.all()
    return jsonify([faq.to_dict() for faq in faqs]), 200

# Route to create a new FAQ
@app.route('/api/faqs', methods=['POST'])
def create_faq():
    """Create a new FAQ."""
    data = request.get_json()
    new_faq = FAQ(question=data['question'], answer=data['answer'])

    try:
        db.session.add(new_faq)
        db.session.commit()
        return jsonify(new_faq.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "FAQ creation failed due to integrity error."}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
