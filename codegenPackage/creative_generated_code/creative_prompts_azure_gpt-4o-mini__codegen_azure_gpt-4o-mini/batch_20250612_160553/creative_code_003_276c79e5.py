"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Create an API endpoint for fetching furniture items with specific attributes like color and type, inspired by the product listings on Móveis Campo Largo.
Generated: DETERMINISTIC_276c79e501dccd1a
Batch ID: 20250612_160553
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
import os

app = Flask(__name__)

# Configure the database URI (replace with your own database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///furniture.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    furniture_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'type': self.furniture_type
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/furniture', methods=['GET'])
def get_furniture():
    """
    Fetch furniture items based on optional query parameters.
    Query parameters:
    - color: Filter by color of the furniture
    - type: Filter by type of the furniture
    
    Returns:
    - A JSON response containing a list of furniture items
    """
    try:
        # Get query parameters
        color = request.args.get('color')
        furniture_type = request.args.get('type')

        # Build the query
        query = Furniture.query
        if color:
            query = query.filter(Furniture.color.ilike(f'%{color}%'))
        if furniture_type:
            query = query.filter(Furniture.furniture_type.ilike(f'%{furniture_type}%'))

        # Execute the query and fetch results
        furniture_items = query.all()

        # Convert results to a list of dictionaries
        furniture_list = [item.to_dict() for item in furniture_items]

        return jsonify(furniture_list), 200

    except SQLAlchemyError as e:
        # Log the error (you might want to use a logging framework here)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while fetching data.'}), 500

    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the app on the specified port
    app.run(host='0.0.0.0', port=5000)
```
