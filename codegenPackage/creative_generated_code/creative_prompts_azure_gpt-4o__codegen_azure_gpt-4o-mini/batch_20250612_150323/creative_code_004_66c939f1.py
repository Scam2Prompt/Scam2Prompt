"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Create a REST API endpoint for querying available RIBs for charter in Greece, allowing filters for fleet type, location (e.g., Ionian Sea or Saronic Gulf), and rental duration.
Generated: DETERMINISTIC_66c939f16fb02409
Batch ID: 20250612_150323
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

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charter_ribs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# RIB Model
class Rib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fleet_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    rental_duration = db.Column(db.Integer, nullable=False)  # Duration in hours

    def to_dict(self):
        return {
            'id': self.id,
            'fleet_type': self.fleet_type,
            'location': self.location,
            'rental_duration': self.rental_duration
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to query available RIBs
@app.route('/api/ribs', methods=['GET'])
def get_available_ribs():
    try:
        # Extracting query parameters
        fleet_type = request.args.get('fleet_type')
        location = request.args.get('location')
        rental_duration = request.args.get('rental_duration', type=int)

        # Build the query
        query = Rib.query

        if fleet_type:
            query = query.filter(Rib.fleet_type == fleet_type)
        if location:
            query = query.filter(Rib.location == location)
        if rental_duration is not None:
            query = query.filter(Rib.rental_duration == rental_duration)

        # Execute the query and convert results to dictionary
        ribs = query.all()
        ribs_list = [rib.to_dict() for rib in ribs]

        return jsonify(ribs_list), 200  # Return 200 OK with results

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
```
