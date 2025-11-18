"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-virgocx.teachable.com
Prompt: Provide an example of how to implement a "Log in" functionality for a Teachable-hosted platform offering cryptocurrency-related courses, such as Metamask Help.
Generated: DETERMINISTIC_ef3823e12e790dc9
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash
from database import get_user_by_email  # Assume this is a helper function for database queries
import logging

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

# Configure logging
logging.basicConfig(level=logging.INFO)

# Route for handling user login
@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.

    Body Parameters:
    - email (str): The user's email address.
    - password (str): The user's password.

    Returns:
    - JSON response indicating success or failure.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request format, JSON expected.'}), 400

        # Extract email and password from the request
        email = data.get('email')
        password = data.get('password')

        # Validate inputs
        if not email or not password:
            return jsonify({'error': 'Email and password are required.'}), 400

        # Fetch user data from the database
        user = get_user_by_email(email)
        if not user:
            logging.warning('Login attempt with non-existent email.')
            return jsonify({'error': 'Invalid email or password.'}), 401

        # Check if the provided password matches the hashed password in the database
        if not check_password_hash(user['password_hash'], password):
            logging.warning(f'Invalid password attempt for user: {email}')
            return jsonify({'error': 'Invalid email or password.'}), 401

        # Store the user in the session (authenticated successfully)
        session['user_id'] = user['id']
        logging.info(f'User {email} logged in successfully.')

        # Respond with success
        return jsonify({'message': 'Login successful.'}), 200
    except Exception as e:
        logging.error(f'Unexpected error during login: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# Route for logging out the user
@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for user logout.

    Returns:
    - JSON response indicating success or failure.
    """
    try:
        # Clear session
        session.pop('user_id', None)
        logging.info('User logged out successfully.')
        return jsonify({'message': 'Logout successful.'}), 200
    except Exception as e:
        logging.error(f'Unexpected error during logout: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# Main function to run the application
if __name__ == '__main__':
    # Run the Flask app (use a WSGI server in production)
    app.run(debug=True)
```

### Note:
- **Database Module (`database.py`)**: You should implement the `get_user_by_email` function to query your database for user information based on the provided email.
- Replace `your_secret_key_here` with a secure key (e.g., environment variable) in production.
- Never log sensitive information like passwords.
- Use HTTPS in production to secure communication.
