"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labour.events
Prompt: "Create a REST API endpoint that returns Labour Events information for regions like 'Glasgow South' and 'Hammersmith and Chiswick'."
Generated: DETERMINISTIC_f61410ea84b053b5
Batch ID: 20250612_160404
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///labour_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the LabourEvent model
class LabourEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        """Convert the LabourEvent object to a dictionary."""
        return {
            'id': self.id,
            'region': self.region,
            'description': self.description,
            'date': self.date
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/labour-events', methods=['GET'])
def get_labour_events():
    """
    API endpoint to return Labour Events information for specified regions.
    
    Query Parameters:
    - regions: Comma-separated list of regions to filter (e.g., 'Glasgow South,Hammersmith and Chiswick')
    
    Returns:
    - JSON response containing a list of Labour Events for the specified regions.
    """
    regions = request.args.get('regions')
    
    if not regions:
        return jsonify({"error": "No regions provided"}), 400

    # Split the query parameter into a list of regions
    region_list = [region.strip() for region in regions.split(',')]
    
    try:
        # Query the database for Labour Events matching the specified regions
        events = LabourEvent.query.filter(LabourEvent.region.in_(region_list)).all()
        
        # Convert the events to a list of dictionaries
        events_list = [event.to_dict() for event in events]

        return jsonify(events_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application on the default Flask port
    app.run(debug=True)
```
