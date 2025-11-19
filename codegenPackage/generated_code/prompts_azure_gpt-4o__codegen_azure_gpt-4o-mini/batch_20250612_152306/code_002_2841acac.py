"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Generate code to create a search functionality for finding training centers by state and district, similar to the "Search Nearest Center" feature on the RSP Bharat website.
Generated: DETERMINISTIC_2841acacd5251a4e
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_centers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TrainingCenter(db.Model):
    """Model representing a training center."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<TrainingCenter {self.name}>'

@app.route('/search_centers', methods=['GET'])
def search_centers():
    """Search for training centers by state and district."""
    state = request.args.get('state')
    district = request.args.get('district')

    if not state or not district:
        return jsonify({"error": "State and district parameters are required."}), 400

    try:
        # Query the database for training centers matching the state and district
        centers = TrainingCenter.query.filter_by(state=state, district=district).all()
        results = [{"id": center.id, "name": center.name} for center in centers]

        if not results:
            return jsonify({"message": "No training centers found."}), 404

        return jsonify(results), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string.
- This code includes basic error handling and checks for required parameters.
