"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chatnchill.com
Prompt: Develop an API endpoint that retrieves information about the famous Caribbean Pig Roast at Chat 'N' Chill®, including menu items and timings.
Generated: DETERMINISTIC_510dde3235e20589
Batch ID: 20250612_162051
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
from datetime import datetime

# Create a Flask application instance
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatnchill.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model for the Pig Roast event
class PigRoast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    menu_items = db.Column(db.String(500), nullable=False)
    timings = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the PigRoast object to a dictionary."""
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d %H:%M"),
            "menu_items": self.menu_items.split(','),  # Split menu items into a list
            "timings": self.timings
        }

# API endpoint to retrieve Pig Roast information
@app.route('/api/pig_roast', methods=['GET'])
def get_pig_roast_info():
    """Retrieve information about the Caribbean Pig Roast."""
    try:
        # Query the database for the most recent Pig Roast
        pig_roast = PigRoast.query.order_by(PigRoast.date.desc()).first()
        
        if pig_roast is None:
            return jsonify({"error": "No Pig Roast information found."}), 404
        
        return jsonify(pig_roast.to_dict()), 200

    except Exception as e:
        # Log the exception and return a 500 error
        app.logger.error(f"Error retrieving Pig Roast information: {e}")
        return jsonify({"error": "An error occurred while retrieving the information."}), 500

# Route for creating a new Pig Roast event (for demonstration purposes)
@app.route('/api/pig_roast', methods=['POST'])
def create_pig_roast():
    """Create a new Pig Roast event."""
    data = request.json

    # Validate incoming data
    try:
        date = datetime.strptime(data['date'], "%Y-%m-%d %H:%M")
        menu_items = data['menu_items']  # Expecting a comma-separated string
        timings = data['timings']

        # Create a new Pig Roast entry
        new_pig_roast = PigRoast(date=date, menu_items=menu_items, timings=timings)
        db.session.add(new_pig_roast)
        db.session.commit()

        return jsonify(new_pig_roast.to_dict()), 201

    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid date format: {str(e)}"}), 400
    except Exception as e:
        app.logger.error(f"Error creating Pig Roast: {e}")
        return jsonify({"error": "An error occurred while creating the Pig Roast."}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
