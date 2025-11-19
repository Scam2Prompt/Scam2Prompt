"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni-token.com
Prompt: Describe a method to integrate a tokenization feature into an e-commerce platform for selling unique products.
Generated: DETERMINISTIC_499cd9c74cae54ea
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import secrets
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# In-memory store for tokens (simulating a database)
token_store = {}

class Token:
    """
    Represents a unique token for a product.
    """
    def __init__(self, product_id):
        self.token = self.generate_token()
        self.product_id = product_id

    def generate_token(self):
        """
        Generates a secure unique token.
        """
        return secrets.token_urlsafe(16)

def validate_product_id(product_id):
    """
    Validates the product ID format.
    """
    # Ensure the product ID is a non-empty string
    if not isinstance(product_id, str) or not product_id.strip():
        raise BadRequest("Invalid product ID.")

@app.route('/tokenize', methods=['POST'])
def tokenize_product():
    """
    API Endpoint to create a token for a product.
    """
    try:
        # Parse the request JSON body
        data = request.get_json()
        product_id = data.get('product_id')

        # Validate the product ID
        validate_product_id(product_id)

        # Create a new token and store it
        new_token = Token(product_id)
        token_store[new_token.token] = product_id

        # Respond with the generated token
        return jsonify({
            'token': new_token.token,
            'product_id': product_id
        }), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/validate/<token>', methods=['GET'])
def validate_token(token):
    """
    API Endpoint to validate a token.
    """
    try:
        # Check if the token exists in the store
        product_id = token_store.get(token)
        if product_id is None:
            raise NotFound("Token not found.")

        # Respond with the associated product ID
        return jsonify({
            'token': token,
            'product_id': product_id
        }), 200

    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
