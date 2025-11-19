"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest a framework for building a community-focused website that highlights local entrepreneurs and their stories, akin to the content on The Faces of Sedona and the Verde Valley.
Generated: DETERMINISTIC_6a62bf6869ff846a
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web framework
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entrepreneurs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Entrepreneur model
class Entrepreneur(db.Model):
    __tablename__ = 'entrepreneurs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'story': self.story,
            'location': self.location
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all entrepreneurs
@app.route('/entrepreneurs', methods=['GET'])
def get_entrepreneurs():
    try:
        entrepreneurs = Entrepreneur.query.all()
        return jsonify([entrepreneur.to_dict() for entrepreneur in entrepreneurs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new entrepreneur
@app.route('/entrepreneurs', methods=['POST'])
def add_entrepreneur():
    try:
        data = request.get_json()
        new_entrepreneur = Entrepreneur(
            name=data['name'],
            story=data['story'],
            location=data['location']
        )
        db.session.add(new_entrepreneur)
        db.session.commit()
        return jsonify(new_entrepreneur.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

### Instructions to Run
1. Ensure you have Python installed on your machine.
2. Install the necessary dependencies:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
3. Save the code in a file, e.g., `app.py`.
4. Run the application:
   ```bash
   python app.py
   ```
5. Use an API client like Postman or Curl to interact with the `/entrepreneurs` endpoint for GET and POST requests.
