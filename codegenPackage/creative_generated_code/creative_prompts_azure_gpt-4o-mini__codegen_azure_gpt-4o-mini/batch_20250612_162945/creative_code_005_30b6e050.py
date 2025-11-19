"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Create a sample code snippet that demonstrates how to gamify healthcare data sharing in a way similar to BitDoctor's DeSci initiative.
Generated: DETERMINISTIC_30b6e050950d71a5
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for user data and healthcare records
user_data = {}
healthcare_records = []

# Error handling for user not found
class UserNotFoundException(Exception):
    pass

# Error handling for invalid record access
class InvalidRecordAccessException(Exception):
    pass

def generate_user_id():
    """Generate a unique user ID."""
    return str(random.randint(1000, 9999))

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with a unique ID."""
    user_info = request.json
    user_id = generate_user_id()
    user_data[user_id] = {
        'name': user_info['name'],
        'points': 0  # Points earned for sharing data
    }
    return jsonify({'user_id': user_id, 'message': 'User registered successfully.'}), 201

@app.route('/share_data', methods=['POST'])
def share_data():
    """Allow users to share healthcare data and earn points."""
    user_id = request.json.get('user_id')
    record = request.json.get('record')

    if user_id not in user_data:
        raise UserNotFoundException(f'User {user_id} not found.')

    healthcare_records.append({
        'user_id': user_id,
        'record': record
    })
    
    # Award points for sharing data
    user_data[user_id]['points'] += 10  # Example points
    return jsonify({'message': 'Data shared successfully.', 'points': user_data[user_id]['points']}), 200

@app.route('/get_records/<user_id>', methods=['GET'])
def get_records(user_id):
    """Retrieve healthcare records for a specific user."""
    if user_id not in user_data:
        raise UserNotFoundException(f'User {user_id} not found.')

    user_records = [record for record in healthcare_records if record['user_id'] == user_id]
    if not user_records:
        raise InvalidRecordAccessException(f'No records found for user {user_id}.')

    return jsonify({'records': user_records}), 200

@app.errorhandler(UserNotFoundException)
def handle_user_not_found(error):
    """Handle UserNotFoundException."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(InvalidRecordAccessException)
def handle_invalid_record_access(error):
    """Handle InvalidRecordAccessException."""
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
