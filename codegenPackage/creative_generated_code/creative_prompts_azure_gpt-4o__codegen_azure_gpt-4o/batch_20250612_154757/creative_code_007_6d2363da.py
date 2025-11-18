"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: Write code to report an NFT item for removal from the marketplace, using a message and reason input system like the one described on Artlife.
Generated: DETERMINISTIC_6d2363da445b8e9e
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Set up logging for error tracking and reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database to store reported items (In production, integrate with a real database)
reported_items = []

@app.route('/report_nft', methods=['POST'])
def report_nft():
    """
    Endpoint to report an NFT item for removal from the marketplace.
    Request payload must include:
        - nft_id: ID of the NFT to be reported
        - reason: Reason for reporting the NFT
        - message: Additional message or explanation (optional)
    """
    try:
        # Parse the JSON request payload
        data = request.get_json()

        # Validate required fields
        if not data or 'nft_id' not in data or 'reason' not in data:
            return jsonify({"error": "Missing required fields: 'nft_id' and 'reason'"}), 400
        
        nft_id = data['nft_id']
        reason = data['reason']
        message = data.get('message', '')  # Optional field

        # Validate that 'nft_id' and 'reason' are non-empty
        if not nft_id.strip() or not reason.strip():
            return jsonify({"error": "'nft_id' and 'reason' cannot be empty"}), 400

        # Create a report object
        report = {
            "nft_id": nft_id,
            "reason": reason,
            "message": message,
            "status": "Pending Review"  # Initial status set as pending review
        }

        # Store the report in the mock database
        reported_items.append(report)

        logging.info(f"NFT {nft_id} reported successfully for reason: {reason}.")
        return jsonify({"message": "NFT reported successfully", "report": report}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"Error while reporting NFT: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

@app.route('/reported_items', methods=['GET'])
def get_reported_items():
    """
    Endpoint to fetch all reported NFT items.
    """
    return jsonify({"reported_items": reported_items}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
