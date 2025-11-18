"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Write code to implement a secure payment gateway for an online betting platform, ensuring encryption and data safety as highlighted in the 1Win security measures.
Generated: DETERMINISTIC_05276d7d0f58ef22
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import json
import os
import uuid
from typing import Dict, Any
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables for sensitive information
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Generate or load encryption key
encryption_key = os.getenv("ENCRYPTION_KEY")  # Ensure this key is stored securely, e.g., in an environment variable
if not encryption_key:
    raise RuntimeError("ENCRYPTION_KEY environment variable not set")
fernet = Fernet(encryption_key.encode())

# Secret key for HMAC (for verifying payment authenticity)
hmac_secret_key = os.getenv("HMAC_SECRET_KEY")
if not hmac_secret_key:
    raise RuntimeError("HMAC_SECRET_KEY environment variable not set")


def encrypt_data(data: str) -> str:
    """Encrypt sensitive payment data."""
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data: str) -> str:
    """Decrypt sensitive payment data."""
    return fernet.decrypt(data.encode()).decode()


def generate_transaction_id() -> str:
    """Generate a unique transaction ID."""
    return str(uuid.uuid4())


def verify_hmac_signature(data: Dict[str, Any], received_signature: str) -> bool:
    """
    Verify the HMAC signature of the data to ensure its integrity.
    :param data: The payload to verify
    :param received_signature: The signature sent by the client
    :return: True if the signature is valid, False otherwise
    """
    serialized_data = json.dumps(data, sort_keys=True).encode()
    computed_signature = hmac.new(
        hmac_secret_key.encode(), serialized_data, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, received_signature)


@app.route("/process_payment", methods=["POST"])
def process_payment():
    """
    Endpoint to process payments securely.
    :return: JSON response indicating success or failure.
    """
    try:
        # Parse and validate incoming data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request, JSON payload missing"}), 400

        required_fields = ["amount", "currency", "payment_method", "user_id", "signature"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Verify HMAC signature to ensure data integrity
        signature = data.pop("signature")  # Remove signature for verification
        if not verify_hmac_signature(data, signature):
            return jsonify({"error": "Invalid HMAC signature"}), 400

        # Encrypt sensitive payment data
        encrypted_payment_method = encrypt_data(data["payment_method"])

        # Generate a unique transaction ID
        transaction_id = generate_transaction_id()

        # Simulate payment processing and response
        # (In production, integrate with a payment gateway API here)
        payment_status = "success"  # This is a simulated response

        # Prepare the response
        response = {
            "transaction_id": transaction_id,
            "status": payment_status,
            "amount": data["amount"],
            "currency": data["currency"],
        }

        # Return success response
        return jsonify(response), 200

    except Exception as e:
        # Log the error (in production, use a proper logging framework)
        print(f"Error processing payment: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


if __name__ == "__main__":
    # Run the Flask app securely
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")  # Use HTTPS in production
```

### Notes on Deployment:
- Replace `ssl_context="adhoc"` with a proper SSL/TLS certificate for production.
- Store `ENCRYPTION_KEY` and `HMAC_SECRET_KEY` in a secure environment (e.g., AWS Secrets Manager, environment variables).
- Use a proper logging framework in production to handle errors and logs securely.
