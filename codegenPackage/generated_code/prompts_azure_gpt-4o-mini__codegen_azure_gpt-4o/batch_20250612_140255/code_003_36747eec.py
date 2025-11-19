"""
Generated Code Metadata:
========================
Original URL: https://noble-doodles-genesis-box.testnet.nfts2.me
Prompt: How can I create an API endpoint to handle reports of scam NFT collections similar to NFTs 2 Me?
Generated: DETERMINISTIC_36747eece5f18866
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for reported scam collections (for demonstration purposes)
# In production, use a database for persistent storage
reported_scams = []

@app.route('/report-scam', methods=['POST'])
def report_scam():
    """
    API endpoint to report a scam NFT collection.
    Expects a JSON payload with the following fields:
    - collection_name: Name of the NFT collection (string, required)
    - description: Description of the scam (string, optional)
    - reporter_email: Email of the person reporting the scam (string, optional)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        collection_name = data.get('collection_name')
        if not collection_name:
            return jsonify({"error": "Missing required field: collection_name"}), 400

        # Optional fields
        description = data.get('description', '')
        reporter_email = data.get('reporter_email', '')

        # Create a report object
        report = {
            "collection_name": collection_name,
            "description": description,
            "reporter_email": reporter_email
        }

        # Store the report (in-memory for demonstration purposes)
        reported_scams.append(report)

        # Log the report
        logging.info(f"Scam report received: {report}")

        # Return success response
        return jsonify({"message": "Scam report submitted successfully", "report": report}), 201

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error processing scam report: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/reported-scams', methods=['GET'])
def get_reported_scams():
    """
    API endpoint to retrieve all reported scam NFT collections.
    """
    try:
        return jsonify({"reported_scams": reported_scams}), 200
    except Exception as e:
        logging.error(f"Error retrieving reported scams: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
