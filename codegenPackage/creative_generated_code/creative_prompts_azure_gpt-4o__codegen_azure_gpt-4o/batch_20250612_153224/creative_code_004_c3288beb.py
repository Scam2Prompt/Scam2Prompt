"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Write code to implement a multi-link page similar to Izikard's "Izilink" feature, allowing users to centralize links accessible via NFC or QR code scans.
Generated: DETERMINISTIC_c3288beb4faf36b9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
import qrcode
import os

app = Flask(__name__)

# In-memory storage for user links (In production, use a database)
user_links = {}

@app.route('/')
def home():
    """
    Home endpoint displaying information about the service.
    """
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_link_page():
    """
    Endpoint for creating a multi-link page for a user.
    Expects a JSON payload with 'username' and 'links' (list of URLs).
    """
    try:
        data = request.json
        username = data.get('username')
        links = data.get('links')

        if not username or not links or not isinstance(links, list):
            return jsonify({"error": "Invalid input. 'username' and 'links' are required."}), 400

        user_links[username] = links

        # Generate QR code for the user's multi-link page
        qr_code_url = url_for('multi_link_page', username=username, _external=True)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_code_url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img_path = f"static/qr_codes/{username}.png"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(qr_img_path), exist_ok=True)
        qr_img.save(qr_img_path)

        return jsonify({
            "message": "Multi-link page created successfully.",
            "username": username,
            "qr_code_url": qr_code_url,
            "qr_code_image": qr_img_path
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/user/<username>')
def multi_link_page(username):
    """
    Endpoint to render the multi-link page for a specific user.
    """
    links = user_links.get(username)
    if not links:
        return jsonify({"error": "User not found or no links available."}), 404
    return render_template('multi_link.html', username=username, links=links)

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

# -------------------------------
# HTML Templates
# Save these templates in a `templates` folder in the same directory as this script.

# index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Izilink</h1>
    <p>Centralize your links and share them using QR codes or NFC.</p>
</body>
</html>
"""

# multi_link.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ username }}'s Links</title>
</head>
<body>
    <h1>{{ username }}'s Links</h1>
    <ul>
        {% for link in links %}
        <li><a href="{{ link }}" target="_blank">{{ link }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""
```
