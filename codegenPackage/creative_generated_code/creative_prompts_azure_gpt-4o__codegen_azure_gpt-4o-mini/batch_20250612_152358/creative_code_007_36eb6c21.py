"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintgenesis.pages.dev
Prompt: Write a script to display the total number of tokens minted out of a maximum limit (e.g., 5532/18000) and update the count dynamically after each minting operation.
Generated: DETERMINISTIC_36eb6c21a7ebc3fc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from threading import Lock

# Initialize the Flask application
app = Flask(__name__)

# Maximum number of tokens that can be minted
MAX_TOKENS = 18000
# Current count of minted tokens
current_tokens = 5532
# Lock for thread-safe operations
lock = Lock()

@app.route('/mint', methods=['POST'])
def mint_token():
    """
    Endpoint to mint a new token. Increments the current token count
    and returns the updated count if the maximum limit is not reached.

    Returns:
        JSON response with the updated token count or an error message.
    """
    global current_tokens

    with lock:
        if current_tokens >= MAX_TOKENS:
            # Return error if maximum limit is reached
            return jsonify({"error": "Maximum token limit reached."}), 400
        
        # Increment the token count
        current_tokens += 1

    # Return the current token count
    return jsonify({"message": "Token minted successfully.", "total_tokens": current_tokens, "max_tokens": MAX_TOKENS})

@app.route('/tokens', methods=['GET'])
def get_token_count():
    """
    Endpoint to retrieve the current count of minted tokens.

    Returns:
        JSON response with the current token count and maximum limit.
    """
    return jsonify({"total_tokens": current_tokens, "max_tokens": MAX_TOKENS})

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

Make sure to have Flask installed in your environment. You can install it using pip:
```bash
pip install Flask
``` 

You can run this script, and it will create a simple web server with endpoints to mint tokens and check the current token count.
