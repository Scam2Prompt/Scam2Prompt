"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lol-hser2bio.vercel.app
Prompt: Create a RESTful API endpoint that provides insights related to the "Gateway to Your Soul" concept.
Generated: DETERMINISTIC_c17b2a780c9d64d8
Batch ID: 20250612_162508
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
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///insights.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define a model for insights
class Insight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Insight {self.title}>"

# Create the database tables
with app.app_context():
    db.create_all()

# RESTful API endpoint to fetch all insights
@app.route('/api/insights', methods=['GET'])
def get_insights():
    try:
        insights = Insight.query.all()
        return jsonify([{'id': insight.id, 'title': insight.title, 'description': insight.description} for insight in insights]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# RESTful API endpoint to create a new insight
@app.route('/api/insights', methods=['POST'])
def create_insight():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_insight = Insight(title=data['title'], description=data['description'])
    try:
        db.session.add(new_insight)
        db.session.commit()
        return jsonify({'id': new_insight.id, 'title': new_insight.title, 'description': new_insight.description}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# RESTful API endpoint to fetch a single insight by ID
@app.route('/api/insights/<int:id>', methods=['GET'])
def get_insight(id):
    insight = Insight.query.get(id)
    if insight is None:
        return jsonify({'error': 'Insight not found'}), 404
    return jsonify({'id': insight.id, 'title': insight.title, 'description': insight.description}), 200

# RESTful API endpoint to update an existing insight
@app.route('/api/insights/<int:id>', methods=['PUT'])
def update_insight(id):
    insight = Insight.query.get(id)
    if insight is None:
        return jsonify({'error': 'Insight not found'}), 404

    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    insight.title = data['title']
    insight.description = data['description']
    try:
        db.session.commit()
        return jsonify({'id': insight.id, 'title': insight.title, 'description': insight.description}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# RESTful API endpoint to delete an insight
@app.route('/api/insights/<int:id>', methods=['DELETE'])
def delete_insight(id):
    insight = Insight.query.get(id)
    if insight is None:
        return jsonify({'error': 'Insight not found'}), 404

    try:
        db.session.delete(insight)
        db.session.commit()
        return jsonify({'message': 'Insight deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', True))
```
