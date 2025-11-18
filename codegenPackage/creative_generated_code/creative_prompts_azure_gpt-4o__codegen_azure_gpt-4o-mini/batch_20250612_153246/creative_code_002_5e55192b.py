"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initialmile.com
Prompt: Generate code to integrate a help center feature for answering user questions about company formation, similar to the Help Center described on Initial Mile.
Generated: DETERMINISTIC_5e55192b36033e64
Batch ID: 20250612_153246
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///help_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for FAQ entries
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def serialize(self):
        """Serialize the FAQ object to a dictionary."""
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/faqs', methods=['GET'])
def get_faqs():
    """Retrieve a list of all FAQs."""
    try:
        faqs = FAQ.query.all()
        return jsonify([faq.serialize() for faq in faqs]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/faqs', methods=['POST'])
def add_faq():
    """Add a new FAQ entry."""
    data = request.get_json()
    if not data or not all(key in data for key in ('question', 'answer')):
        return jsonify({'error': 'Invalid input'}), 400

    new_faq = FAQ(question=data['question'], answer=data['answer'])
    try:
        db.session.add(new_faq)
        db.session.commit()
        return jsonify(new_faq.serialize()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    """Delete an FAQ entry by ID."""
    try:
        faq = FAQ.query.get_or_404(faq_id)
        db.session.delete(faq)
        db.session.commit()
        return jsonify({'message': 'FAQ deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Instructions for Use:
1. Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `app.py`.
3. Run the application using:
   ```bash
   python app.py
   ```
4. Use API endpoints `/faqs` for GET, POST, and `/faqs/<id>` for DELETE requests to manage FAQ entries.
