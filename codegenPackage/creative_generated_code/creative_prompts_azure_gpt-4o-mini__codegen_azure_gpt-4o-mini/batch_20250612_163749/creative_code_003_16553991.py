"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Develop an API that provides real-time betting options for various games on 메이저사이트, including sports and e-sports, with an emphasis on user safety.
Generated: DETERMINISTIC_16553991b9ce9eff
Batch ID: 20250612_163749
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
from marshmallow import Schema, fields, validate, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for demonstration; use a more robust DB in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///betting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database model for Betting Options
class BettingOption(db.Model):
    __tablename__ = 'betting_options'
    
    id = db.Column(db.Integer, primary_key=True)
    game_type = db.Column(db.String(50), nullable=False)
    option_name = db.Column(db.String(100), nullable=False)
    odds = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<BettingOption {self.option_name} for {self.game_type}>"

# Schema for validating input data
class BettingOptionSchema(Schema):
    game_type = fields.String(required=True, validate=validate.Length(max=50))
    option_name = fields.String(required=True, validate=validate.Length(max=100))
    odds = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all betting options
@app.route('/api/betting-options', methods=['GET'])
def get_betting_options():
    """Retrieve all available betting options."""
    try:
        options = BettingOption.query.all()
        return jsonify([{'id': option.id, 'game_type': option.game_type, 'option_name': option.option_name, 'odds': option.odds} for option in options]), 200
    except Exception as e:
        logging.error(f"Error retrieving betting options: {e}")
        return jsonify({'error': 'Could not retrieve betting options.'}), 500

# Endpoint to add a new betting option
@app.route('/api/betting-options', methods=['POST'])
def add_betting_option():
    """Add a new betting option."""
    try:
        data = request.json
        BettingOptionSchema().load(data)  # Validate input data
        new_option = BettingOption(**data)
        db.session.add(new_option)
        db.session.commit()
        return jsonify({'message': 'Betting option created successfully.', 'id': new_option.id}), 201
    except ValidationError as ve:
        logging.warning(f"Validation error: {ve.messages}")
        return jsonify({'error': 'Invalid input.', 'messages': ve.messages}), 400
    except Exception as e:
        logging.error(f"Error adding betting option: {e}")
        return jsonify({'error': 'Could not add betting option.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

This code defines a simple Flask API for managing real-time betting options with error handling and logging. Please ensure you have the necessary packages installed in your Python environment (`Flask`, `Flask-SQLAlchemy`, `marshmallow`) before running this code.
