"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Generate a Python script for automating the creation of a knowledge base system for website support, as highlighted in Ansh Soft Tech's quick support features.
Generated: DETERMINISTIC_1dbab245012dda51
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knowledge_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Knowledge Base entries
class KnowledgeBaseEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Schema for serializing Knowledge Base entries
class KnowledgeBaseEntrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KnowledgeBaseEntry

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new knowledge base entry
@app.route('/api/entries', methods=['POST'])
def add_entry():
    """Add a new knowledge base entry."""
    try:
        data = request.json
        if not data or 'question' not in data or 'answer' not in data:
            return jsonify({"error": "Invalid input. Please provide question and answer."}), 400
        
        new_entry = KnowledgeBaseEntry(question=data['question'], answer=data['answer'])
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(KnowledgeBaseEntrySchema().dump(new_entry)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all knowledge base entries
@app.route('/api/entries', methods=['GET'])
def get_entries():
    """Retrieve all knowledge base entries."""
    try:
        entries = KnowledgeBaseEntry.query.all()
        return jsonify(KnowledgeBaseEntrySchema(many=True).dump(entries)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to search for an entry by question
@app.route('/api/entries/search', methods=['GET'])
def search_entry():
    """Search for a knowledge base entry by question."""
    try:
        question = request.args.get('question')
        if not question:
            return jsonify({"error": "Question parameter is required."}), 400
        
        entry = KnowledgeBaseEntry.query.filter(KnowledgeBaseEntry.question.ilike(f'%{question}%')).all()
        return jsonify(KnowledgeBaseEntrySchema(many=True).dump(entry)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start the server: {str(e)}")
```
