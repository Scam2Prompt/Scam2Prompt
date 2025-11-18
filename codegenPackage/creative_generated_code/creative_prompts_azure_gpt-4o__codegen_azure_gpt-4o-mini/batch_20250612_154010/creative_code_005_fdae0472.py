"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: Suggest tools or libraries to set up password-protected links with expiration dates, as described in Fli.so's link security features.
Generated: DETERMINISTIC_fdae0472b3cf1c0c
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime
from flask import Flask, request, jsonify, redirect, abort

app = Flask(__name__)

# In-memory storage for links; in a production environment, this should be replaced with a database
link_storage = {}

class Link:
    def __init__(self, url, expires_in_minutes):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the link
        self.url = url
        self.created_at = datetime.datetime.now()
        self.expires_at = self.created_at + datetime.timedelta(minutes=expires_in_minutes)
        self.is_protected = True  # Indicates the link is password-protected
        self.password = None  # Will hold the password for the link if set

    def set_password(self, password):
        self.password = password

    def is_expired(self):
        """Check if the link has expired."""
        return datetime.datetime.now() > self.expires_at


@app.route('/create_link', methods=['POST'])
def create_link():
    """Endpoint to create a password-protected link with expiration."""
    data = request.json
    url = data.get('url')
    expires_in = data.get('expires_in', 60)  # Default to 60 minutes
    password = data.get('password')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    link = Link(url, expires_in)
    if password:
        link.set_password(password)

    link_storage[link.id] = link
    return jsonify({"id": link.id, "expires_at": link.expires_at.isoformat()}), 201


@app.route('/<link_id>', methods=['GET'])
def access_link(link_id):
    """Endpoint to access a protected link."""
    link = link_storage.get(link_id)

    if not link:
        return abort(404)  # Link not found

    if link.is_expired():
        return jsonify({"error": "Link has expired"}), 403  # Forbidden

    # If the link is protected, check for a password
    if link.is_protected:
        password = request.args.get('password')
        if password != link.password:
            return jsonify({"error": "Invalid password"}), 403

    return redirect(link.url)  # Redirect to the original URL


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "An internal error occurred"}), 500


if __name__ == '__main__':
    app.run(debug=False)  # Set debug=True only in a development environment
```

This code sets up a simple Flask application to create password-protected links with expiration dates. It includes error handling and follows best practices. In a production environment, consider using a database instead of in-memory storage for link management.
