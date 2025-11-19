"""
Generated Code Metadata:
========================
Original URL: https://votes-tokenproof.pages.dev
Prompt: Develop a web application that uses tokenproof for connecting user accounts and enabling QR code-based authentication for voting.
Generated: DETERMINISTIC_ab8a5ba72b2c00ac
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import qrcode
import os
import base64
import secrets
from tokenproof import TokenProof

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    token = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize TokenProof
tokenproof = TokenProof(secret=os.environ.get('TOKENPROOF_SECRET', 'your_secret_key'))

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Generate a unique token for the user
    token = secrets.token_urlsafe(16)
    new_user = User(username=username, token=token)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', 'token': token}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route for generating QR code
@app.route('/generate_qr/<username>', methods=['GET'])
def generate_qr(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create a tokenproof URL for the user
    tokenproof_url = tokenproof.create_url(user.token)

    # Generate QR code
    img = qrcode.make(tokenproof_url)
    img_path = f'static/qrcodes/{username}_qr.png'
    img.save(img_path)

    return jsonify({'message': 'QR code generated', 'qr_code_path': img_path}), 200

# Route for voting
@app.route('/vote', methods=['POST'])
def vote():
    token = request.json.get('token')
    if not token:
        return jsonify({'error': 'Token is required'}), 400

    # Verify the token
    try:
        user = tokenproof.verify(token)
        return jsonify({'message': f'Vote recorded for {user.username}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 403

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Create static directory for QR codes if it doesn't exist
    os.makedirs('static/qrcodes', exist_ok=True)
    # Run the application
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voting App</title>
</head>
<body>
    <h1>Voting Application</h1>
    <form id="registerForm">
        <input type="text" id="username" placeholder="Enter username" required>
        <button type="submit">Register</button>
    </form>
    <form id="voteForm">
        <input type="text" id="token" placeholder="Enter token" required>
        <button type="submit">Vote</button>
    </form>
    <script>
        document.getElementById('registerForm').onsubmit = async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const response = await fetch('/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username })
            });
            const data = await response.json();
            alert(data.message || data.error);
        };

        document.getElementById('voteForm').onsubmit = async (e) => {
            e.preventDefault();
            const token = document.getElementById('token').value;
            const response = await fetch('/vote', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ token })
            });
            const data = await response.json();
            alert(data.message || data.error);
        };
    </script>
</body>
</html>
```

### Notes
- Ensure you have the required libraries installed: `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `qrcode`, and `tokenproof`.
- Set the `TOKENPROOF_SECRET` environment variable for secure token generation.
- The application uses SQLite for simplicity; consider using a more robust database for production.
- The QR code images are saved in the `static/qrcodes` directory.
