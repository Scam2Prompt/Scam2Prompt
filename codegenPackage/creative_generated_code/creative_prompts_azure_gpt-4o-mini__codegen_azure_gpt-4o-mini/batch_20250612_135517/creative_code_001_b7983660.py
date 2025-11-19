"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnifi.co
Prompt: Write a code snippet for an API that allows users to access their wages instantly, like Earnifi's instant earnings feature.
Generated: DETERMINISTIC_b79836605b0438c7
Batch ID: 20250612_135517
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
from werkzeug.exceptions import BadRequest, NotFound
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Wage model
class Wage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create the database table
with app.app_context():
    db.create_all()

@app.route('/api/wages/<string:user_id>', methods=['GET'])
def get_instant_wages(user_id):
    """
    Endpoint to retrieve the user's instant wages.

    Parameters:
        user_id (str): The ID of the user whose wages are being requested.

    Returns:
        JSON response containing the user's wage information or an error message.
    """
    try:
        # Query the database for the user's wage
        wage = Wage.query.filter_by(user_id=user_id).first()
        
        # If no wage record is found, return a 404 error
        if wage is None:
            logging.warning(f"Wage record not found for user_id: {user_id}")
            raise NotFound("Wage record not found.")
        
        # Return the wage information
        return jsonify({"user_id": user_id, "wage": wage.amount}), 200

    except BadRequest as e:
        logging.error(f"Bad request: {str(e)}")
        return jsonify({"error": "Bad request."}), 400

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
