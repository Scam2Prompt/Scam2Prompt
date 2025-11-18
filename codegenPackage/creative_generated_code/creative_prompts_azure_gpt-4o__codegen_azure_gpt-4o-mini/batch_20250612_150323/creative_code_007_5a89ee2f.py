"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Provide a step-by-step guide for creating a secure API to transmit encrypted sewing machine data to a centralized analytics platform, as OpenSeam plans to offer in the future.
Generated: DETERMINISTIC_5a89ee2f35e371d9
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import logging
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Generate a key for encryption and decryption
# In a production environment, use a secure method to store and manage your keys
KEY = os.getenv('ENCRYPTION_KEY')
if not KEY:
    KEY = Fernet.generate_key()
    logger.warning("No encryption key found. A new key has been generated. Make sure to save it.")
fernet = Fernet(KEY)

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/sewing-data', methods=['POST'])
def receive_sewing_data():
    """
    Endpoint to receive encrypted sewing machine data.
    
    The data is expected to be encrypted using Fernet.
    """
    try:
        # Get the encrypted data from the request
        encrypted_data = request.json.get('data')
        if not encrypted_data:
            return jsonify({"error": "No data provided."}), 400

        # Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()

        # Process the data (e.g., save to database or forward to another service)
        logger.info("Successfully received and decrypted sewing machine data.")
        logger.debug(f"Decrypted Data: {decrypted_data}")

        # Here you can add the logic to transmit data to the analytics platform

        return jsonify({"message": "Data received successfully."}), 200

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Failed to process request."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### .env file example
```
ENCRYPTION_KEY=your_base64_encoded_key_here
```

### Usage
- Ensure to store the `ENCRYPTION_KEY` securely.
- Use `Fernet` to encrypt data before sending it to the API.
- Adjust logging levels in production as needed.
