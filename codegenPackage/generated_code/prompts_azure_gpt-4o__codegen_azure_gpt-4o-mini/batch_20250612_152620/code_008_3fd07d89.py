"""
Generated Code Metadata:
========================
Original URL: https://mercurio.com.pe
Prompt: Suggest best practices for implementing a secure data center infrastructure for electronic invoicing, referencing Mercurio's TIER III-certified data center.
Generated: DETERMINISTIC_3fd07d89a892f3ed
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption
def generate_key():
    """Generate a secure key for encryption."""
    return Fernet.generate_key()

# Load the encryption key from an environment variable
def load_key():
    """Load the encryption key from an environment variable."""
    key = os.getenv("ENCRYPTION_KEY")
    if key is None:
        logging.error("Encryption key not found in environment variables.")
        raise ValueError("Encryption key not found.")
    return key.encode()

# Encrypt data using the provided key
def encrypt_data(data, key):
    """Encrypt the provided data using the given key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data using the provided key
def decrypt_data(encrypted_data, key):
    """Decrypt the provided data using the given key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Initialize Flask application
app = Flask(__name__)

@app.route('/invoice', methods=['POST'])
def create_invoice():
    """Endpoint to create a new invoice."""
    try:
        # Get the invoice data from the request
        invoice_data = request.json.get('data')
        if not invoice_data:
            logging.error("No invoice data provided.")
            return jsonify({"error": "No invoice data provided."}), 400
        
        # Load the encryption key
        key = load_key()
        
        # Encrypt the invoice data
        encrypted_invoice = encrypt_data(invoice_data, key)
        
        # Here you would typically save the encrypted invoice to a database
        # For demonstration, we just log it
        logging.info(f"Encrypted invoice data: {encrypted_invoice}")
        
        return jsonify({"message": "Invoice created successfully.", "encrypted_data": encrypted_invoice.decode()}), 201

    except Exception as e:
        logging.error(f"Error creating invoice: {str(e)}")
        return jsonify({"error": "Failed to create invoice."}), 500

@app.route('/invoice', methods=['GET'])
def get_invoice():
    """Endpoint to retrieve an invoice."""
    try:
        # Simulate retrieving encrypted invoice data (in a real scenario, this would come from a database)
        encrypted_invoice = request.args.get('encrypted_data')
        if not encrypted_invoice:
            logging.error("No encrypted invoice data provided.")
            return jsonify({"error": "No encrypted invoice data provided."}), 400
        
        # Load the encryption key
        key = load_key()
        
        # Decrypt the invoice data
        decrypted_invoice = decrypt_data(encrypted_invoice.encode(), key)
        
        return jsonify({"message": "Invoice retrieved successfully.", "data": decrypted_invoice}), 200

    except Exception as e:
        logging.error(f"Error retrieving invoice: {str(e)}")
        return jsonify({"error": "Failed to retrieve invoice."}), 500

if __name__ == '__main__':
    # Set the environment variable for the encryption key
    os.environ["ENCRYPTION_KEY"] = generate_key().decode()
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
