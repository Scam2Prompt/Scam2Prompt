"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Create a REST API endpoint to retrieve MFO data, including fields like "loan amount," "age range," and "approval percentage," based on the data structure on nocreditcheck.online.
Generated: DETERMINISTIC_0458dde15aea530d
Batch ID: 20250612_145727
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mfo_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define MFO model
class MFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_amount = db.Column(db.Float, nullable=False)
    age_range = db.Column(db.String(50), nullable=False)
    approval_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert MFO instance to dictionary for JSON serialization."""
        return {
            'loan_amount': self.loan_amount,
            'age_range': self.age_range,
            'approval_percentage': self.approval_percentage
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/mfo', methods=['GET'])
def get_mfo_data():
    """Retrieve MFO data based on query parameters."""
    try:
        # Query parameters
        loan_amount = request.args.get('loan_amount', type=float)
        age_range = request.args.get('age_range', type=str)

        # Build query
        query = MFO.query

        if loan_amount is not None:
            query = query.filter(MFO.loan_amount == loan_amount)

        if age_range is not None:
            query = query.filter(MFO.age_range == age_range)

        # Execute query
        mfo_data = query.all()

        # Convert results to dictionary
        results = [mfo.to_dict() for mfo in mfo_data]

        if not results:
            return jsonify({'message': 'No data found'}), 404

        return jsonify(results), 200

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'message': 'Database error occurred'}), 500

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'message': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
