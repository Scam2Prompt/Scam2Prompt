"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theneuraluniverse.com
Prompt: Create an API endpoint that allows users to submit their experiences related to neurosurgery, inspired by the content on The Neural Universe.
Generated: DETERMINISTIC_a2755fd275f1657e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for submitted experiences (simulating a database)
experiences = []

@app.route('/submit_experience', methods=['POST'])
def submit_experience():
    """
    API endpoint to submit a neurosurgery-related experience.
    Expects JSON payload with 'name', 'email', and 'experience'.
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'experience' not in data:
            return jsonify({'error': 'Invalid input. Please provide name, email, and experience.'}), 400
        
        # Ensure all fields are non-empty
        name = data['name'].strip()
        email = data['email'].strip()
        experience = data['experience'].strip()
        if not name or not email or not experience:
            return jsonify({'error': 'All fields (name, email, experience) must be non-empty.'}), 400
        
        # Create a record for the experience
        experience_record = {
            'id': len(experiences) + 1,  # Simple ID generation
            'name': name,
            'email': email,
            'experience': experience,
            'submitted_at': datetime.utcnow().isoformat()  # Timestamp for submission
        }
        
        # Add the record to storage
        experiences.append(experience_record)
        
        # Return success response
        return jsonify({'message': 'Experience submitted successfully!', 'data': experience_record}), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

@app.route('/experiences', methods=['GET'])
def get_experiences():
    """
    API endpoint to retrieve all submitted experiences.
    """
    try:
        return jsonify({'experiences': experiences}), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
