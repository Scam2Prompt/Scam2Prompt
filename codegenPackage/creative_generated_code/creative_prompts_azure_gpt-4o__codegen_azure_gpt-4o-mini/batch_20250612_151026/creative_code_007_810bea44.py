"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claynosaurz-nft.web.app
Prompt: Generate a script to track and log user interactions with the "Mint Now" button for the "Claynosaurz" NFT project.
Generated: DETERMINISTIC_810bea448f8428f7
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='user_interactions.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/mint_now', methods=['POST'])
def mint_now():
    """
    Endpoint to track user interactions with the "Mint Now" button.
    Expects a JSON payload containing user ID and any additional data.
    Logs the interaction to a file.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the input data
        if not data or 'user_id' not in data:
            logging.warning("Invalid data received: %s", data)
            return jsonify({"error": "Invalid input data"}), 400

        user_id = data['user_id']
        additional_info = data.get('info', 'No additional info provided')

        # Log user interaction
        logging.info("User %s clicked 'Mint Now': %s", user_id, additional_info)

        return jsonify({"message": "Mint action tracked successfully"}), 200

    except Exception as e:
        # Log unexpected errors
        logging.error("An error occurred: %s", str(e))
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
