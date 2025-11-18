"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Write a Python function to check if a user is logged in to a website before allowing access to downloadable book formats like RTF and FB2.
Generated: DETERMINISTIC_1c593a55043b8d34
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

def is_logged_in():
    """
    Check if the user is logged in by verifying the session.

    Returns:
        bool: True if logged in, False otherwise.
    """
    return session.get('logged_in', False)

@app.route('/download/<file_format>', methods=['GET'])
def download_file(file_format):
    """
    Route to handle the download of book formats.

    Args:
        file_format (str): The requested file format (e.g., RTF, FB2).

    Returns:
        JSON response indicating success or failure.
    """
    # Ensure the user is logged in
    if not is_logged_in():
        return jsonify({'error': 'Access denied. Please log in first.'}), 403

    # Allow only specific formats
    allowed_formats = {'rtf', 'fb2'}
    if file_format.lower() not in allowed_formats:
        return jsonify({'error': f'Invalid file format. Allowed formats: {", ".join(allowed_formats)}'}), 400

    # Simulate successful download
    return jsonify({'message': f'{file_format.upper()} file download initiated.'}), 200

@app.route('/login', methods=['POST'])
def login():
    """
    Simulate a user login by setting session variables.

    Returns:
        JSON response indicating login success.
    """
    session['logged_in'] = True
    return jsonify({'message': 'Login successful.'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """
    Simulate user logout by clearing session variables.

    Returns:
        JSON response indicating logout success.
    """
    session.pop('logged_in', None)
    return jsonify({'message': 'Logout successful.'}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
