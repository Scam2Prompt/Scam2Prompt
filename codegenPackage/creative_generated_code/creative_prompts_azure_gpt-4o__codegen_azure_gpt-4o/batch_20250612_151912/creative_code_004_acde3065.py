"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Suggest an API for handling secure communication between lawyers and clients in a family law firm, emphasizing confidentiality and client support, as highlighted by Majeli Avocat.
Generated: DETERMINISTIC_acde3065a27db281
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from cryptography.fernet import Fernet

app = Flask(__name__)

# Secret key for JWT generation
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key_here"
jwt = JWTManager(app)

# Generate and store a key for encryption
# In production, store this securely (e.g., environment variable or secret management tool)
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Mock database for users (lawyers and clients)
# In production, replace with a proper database
users_db = {
    "lawyer1": {"password": "lawyer_password", "role": "lawyer"},
    "client1": {"password": "client_password", "role": "client"},
}

# Mock messages database
messages_db = []


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint for user login.
    Requires a username and password.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validate user credentials
    user = users_db.get(username)
    if user and user["password"] == password:
        # Generate JWT token
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/send_message", methods=["POST"])
@jwt_required()
def send_message():
    """
    Endpoint for sending secure messages between lawyers and clients.
    Requires authentication and encryption of the message content.
    """
    data = request.json
    sender = data.get("sender")
    recipient = data.get("recipient")
    message = data.get("message")

    if not all([sender, recipient, message]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Encrypt the message
        encrypted_message = cipher_suite.encrypt(message.encode())
        messages_db.append({"sender": sender, "recipient": recipient, "message": encrypted_message})
        return jsonify({"message": "Message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to send message", "details": str(e)}), 500


@app.route("/get_messages", methods=["GET"])
@jwt_required()
def get_messages():
    """
    Endpoint for retrieving messages for the authenticated user.
    Decrypts and returns messages intended for the user.
    """
    current_user = request.json.get("username")

    if not current_user:
        return jsonify({"error": "Missing username"}), 400

    try:
        user_messages = [
            {
                "sender": msg["sender"],
                "recipient": msg["recipient"],
                "message": cipher_suite.decrypt(msg["message"]).decode(),
            }
            for msg in messages_db
            if msg["recipient"] == current_user
        ]
        return jsonify({"messages": user_messages}), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve messages", "details": str(e)}), 500


@app.errorhandler(404)
def not_found(e):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
