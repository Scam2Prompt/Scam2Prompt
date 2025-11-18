"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: Write a Python script to automate the process of collecting mineral rights data from sellers in Oklahoma, including fields for first name, last name, email, and comments, as described on Kraken Energy's website.
Generated: DETERMINISTIC_87564f88d9d27a4b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # Database URI from environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing mineral rights data
class MineralRightsSeller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<MineralRightsSeller {self.first_name} {self.last_name}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/submit', methods=['POST'])
def submit_data():
    """
    Endpoint to collect mineral rights data from sellers.
    Expects a JSON payload with first_name, last_name, email, and comments.
    """
    try:
        data = request.json

        # Validate incoming data
        if not all(key in data for key in ('first_name', 'last_name', 'email', 'comments')):
            return jsonify({'error': 'Missing data'}), 400

        # Create a new seller entry
        new_seller = MineralRightsSeller(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            comments=data['comments']
        )

        # Add the seller to the database
        db.session.add(new_seller)
        db.session.commit()

        return jsonify({'message': 'Data submitted successfully!'}), 201

    except Exception as e:
        # Handle any errors that occur during the process
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development; set to False in production
    app.run(debug=True)
```

### .env file example
```
DATABASE_URI=sqlite:///mineral_rights.db
```

### Requirements
To run this script, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy python-dotenv
```

### Notes
- Make sure to create a `.env` file in the same directory as the script with the appropriate `DATABASE_URI`.
- The database used in this example is SQLite for simplicity; you can replace it with any other supported database URI.
- This script is designed to be run as a standalone Flask application.
