"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Develop an API endpoint for managing membership registrations and inquiries for a running club, similar to the features offered by Thompson Estate Athletics.
Generated: DETERMINISTIC_f91270ead353990f
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database for production)
memberships = {}

# Utility function: Generate a unique membership ID
def generate_membership_id():
    return str(uuid.uuid4())

@app.route('/register', methods=['POST'])
def register_member():
    """
    Endpoint to register a new member to the running club.
    Expects JSON with `name`, `email`, and `age`.
    """
    try:
        # Parse JSON data from request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        # Validate input
        if not name or not email or not age:
            return jsonify({'error': 'Name, email, and age are required'}), 400

        if not isinstance(age, int) or age <= 0:
            return jsonify({'error': 'Age must be a positive integer'}), 400

        # Generate unique ID for the new member
        membership_id = generate_membership_id()

        # Save member information
        memberships[membership_id] = {
            'membership_id': membership_id,
            'name': name,
            'email': email,
            'age': age
        }

        # Return success response
        return jsonify({'message': 'Registration successful', 'membership_id': membership_id}), 201

    except Exception as e:
        # Catch-all error handling (should log actual error in production)
        return jsonify({'error': 'An error occurred during registration', 'details': str(e)}), 500


@app.route('/inquire/<membership_id>', methods=['GET'])
def inquire_member(membership_id):
    """
    Endpoint to inquire about a member's details using their membership ID.
    """
    try:
        # Lookup member by membership ID
        member = memberships.get(membership_id)

        if not member:
            return jsonify({'error': 'Membership ID not found'}), 404

        # Return member details
        return jsonify(member), 200

    except Exception as e:
        # Catch-all error handling (should log actual error in production)
        return jsonify({'error': 'An error occurred during inquiry', 'details': str(e)}), 500


@app.route('/members', methods=['GET'])
def list_members():
    """
    Endpoint to list all members of the running club.
    """
    try:
        # Return all members
        return jsonify({'members': list(memberships.values())}), 200

    except Exception as e:
        # Catch-all error handling (should log actual error in production)
        return jsonify({'error': 'An error occurred while listing members', 'details': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False in production
```
