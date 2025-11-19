"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Suggest an API that could help automate the management of training sessions related to Coordination SPS, as mentioned in the AFCO's training initiatives.
Generated: DETERMINISTIC_6c5d8e0234d475e4
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import datetime

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for storing training sessions
training_db = []

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# API: Get all training sessions
@app.route('/api/training_sessions', methods=['GET'])
def get_training_sessions():
    """
    Endpoint to retrieve all training sessions stored in the system.
    """
    return jsonify(training_db), 200

# API: Create a new training session
@app.route('/api/training_sessions', methods=['POST'])
def create_training_session():
    """
    Endpoint to create a new training session.
    Expected JSON Payload:
        {
            "title": "String - Training Session Title",
            "description": "String - Training Session Details",
            "date": "String - Date in YYYY-MM-DD Format",
            "location": "String - Location of the Training"
        }
    """
    try:
        # Parse input data
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        location = data.get('location')

        # Validate input
        if not title or not description or not date or not location:
            return error_response("All fields (title, description, date, location) are required.", 400)

        # Validate date format
        try:
            training_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return error_response("Date format must be YYYY-MM-DD.", 400)

        # Create a new training session
        new_session = {
            'id': len(training_db) + 1,
            'title': title,
            'description': description,
            'date': str(training_date),
            'location': location
        }
        training_db.append(new_session)
        return jsonify({'message': 'Training session created successfully.', 'session': new_session}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# API: Delete a training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['DELETE'])
def delete_training_session(session_id):
    """
    Endpoint to delete a training session by its ID.
    """
    try:
        # Find the session by ID
        session = next((s for s in training_db if s['id'] == session_id), None)

        # Validate existence
        if not session:
            return error_response("Training session not found.", 404)

        # Remove the session
        training_db.remove(session)
        return jsonify({'message': 'Training session deleted successfully.', 'session': session}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# API: Update a training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['PUT'])
def update_training_session(session_id):
    """
    Endpoint to update an existing training session by its ID.
    Expected JSON Payload:
        {
            "title": "String - Training Session Title (optional)",
            "description": "String - Training Session Details (optional)",
            "date": "String - Date in YYYY-MM-DD Format (optional)",
            "location": "String - Location of the Training (optional)"
        }
    """
    try:
        # Find the session by ID
        session = next((s for s in training_db if s['id'] == session_id), None)

        # Validate existence
        if not session:
            return error_response("Training session not found.", 404)

        # Parse input data
        data = request.get_json()

        # Update fields if provided
        if 'title' in data and data['title']:
            session['title'] = data['title']
        if 'description' in data and data['description']:
            session['description'] = data['description']
        if 'date' in data and data['date']:
            try:
                session['date'] = str(datetime.datetime.strptime(data['date'], '%Y-%m-%d').date())
            except ValueError:
                return error_response("Date format must be YYYY-MM-DD.", 400)
        if 'location' in data and data['location']:
            session['location'] = data['location']

        return jsonify({'message': 'Training session updated successfully.', 'session': session}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
