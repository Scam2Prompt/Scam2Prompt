"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frontiersistem.ro
Prompt: Develop a RESTful API endpoint for handling import requests, based on the business model of FRONTIER SISTEM.
Generated: DETERMINISTIC_1db8ba4988ad8c7a
Batch ID: 20250612_162710
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
import logging

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frontier_sistem.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the ImportRequest model
class ImportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ImportRequest {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/import', methods=['POST'])
def import_data():
    """
    Endpoint to handle import requests.

    Expects a JSON payload with the following structure:
    {
        "data": "string"
    }

    Returns:
        - 201 Created on successful import
        - 400 Bad Request if data is not provided
        - 500 Internal Server Error for unexpected errors
    """
    try:
        # Get JSON payload
        request_data = request.get_json()
        
        # Validate request data
        if not request_data or 'data' not in request_data:
            logging.warning("Invalid request data: %s", request_data)
            return jsonify({"error": "Invalid input, 'data' field is required."}), 400

        # Create a new ImportRequest instance
        new_import_request = ImportRequest(data=request_data['data'])

        # Add the import request to the session and commit to the database
        db.session.add(new_import_request)
        db.session.commit()

        logging.info("Import request created with ID: %d", new_import_request.id)
        return jsonify({"message": "Import request created successfully.", "id": new_import_request.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of a database error
        logging.error("Database error occurred: %s", str(e))
        return jsonify({"error": "Database error occurred."}), 500

    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
