"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Develop a script to automate the collection and storage of user registration data (name and phone number) for an online educational program, adhering to the privacy policy principles outlined on КарьераОнлайн.
Generated: DETERMINISTIC_432d4f3d777675a1
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Define the path for storing the registration data
DATA_FILE = 'user_registration_data.json'

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)  # Initialize with an empty list

def save_registration_data(user_data):
    """
    Save user registration data to a JSON file.

    :param user_data: Dictionary containing user registration data
    """
    try:
        with open(DATA_FILE, 'r+') as f:
            # Load existing data
            data = json.load(f)
            # Append the new user data
            data.append(user_data)
            # Move the cursor to the beginning of the file
            f.seek(0)
            # Write updated data back to the file
            json.dump(data, f, indent=4)
            # Truncate the file to remove any leftover old data
            f.truncate()
    except Exception as e:
        # Log the error and raise a BadRequest
        print(f"Error saving registration data: {e}")
        raise BadRequest("Could not save registration data.")

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a user with their name and phone number.

    Expects a JSON body with keys: 'name' and 'phone'.
    """
    try:
        # Parse JSON data from request
        user_data = request.json

        # Validate input data
        if not user_data or 'name' not in user_data or 'phone' not in user_data:
            return jsonify({"error": "Invalid input. 'name' and 'phone' are required."}), 400

        # Collect user data
        name = user_data['name']
        phone = user_data['phone']

        # Simple validation
        if not isinstance(name, str) or not isinstance(phone, str):
            return jsonify({"error": "'name' and 'phone' must be strings."}), 400

        # Save the user registration data
        save_registration_data({"name": name, "phone": phone})

        # Return success response
        return jsonify({"message": "User registered successfully."}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
