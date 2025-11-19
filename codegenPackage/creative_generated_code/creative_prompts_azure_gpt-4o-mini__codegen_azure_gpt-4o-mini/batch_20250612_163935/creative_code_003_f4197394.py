"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dridmachine.com
Prompt: Develop a RESTful API endpoint that allows users to submit design requests for custom posters and record covers.
Generated: DETERMINISTIC_f4197394b7ba68e1
Batch ID: 20250612_163935
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the DesignRequest model
class DesignRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    request_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the database model to a dictionary."""
        return {
            'id': self.id,
            'user_name': self.user_name,
            'request_type': self.request_type,
            'description': self.description
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/design-request', methods=['POST'])
def create_design_request():
    """
    Endpoint to submit a new design request.
    Expects a JSON payload containing 'user_name', 'request_type', and 'description'.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'user_name' not in data or 'request_type' not in data or 'description' not in data:
            raise BadRequest("Missing required fields: user_name, request_type, or description.")

        # Create a new DesignRequest object
        new_request = DesignRequest(
            user_name=data['user_name'],
            request_type=data['request_type'],
            description=data['description']
        )

        # Add the new request to the session and commit it to the database
        db.session.add(new_request)
        db.session.commit()

        # Return the created design request with a success status
        return jsonify(new_request.to_dict()), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

@app.route('/design-request/<int:request_id>', methods=['GET'])
def get_design_request(request_id):
    """
    Endpoint to retrieve a design request by its ID.
    """
    try:
        # Fetch the design request from the database
        request_record = DesignRequest.query.get(request_id)
        if request_record is None:
            raise NotFound("Design request not found.")

        # Return the found design request
        return jsonify(request_record.to_dict()), 200

    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
