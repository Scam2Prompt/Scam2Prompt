"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neftyartstudio.com
Prompt: Create a REST API endpoint in Flask for retrieving and reporting NFTs from the Neftyartstudio marketplace, including features like "Describe why you think this item should be removed."
Generated: DETERMINISTIC_e18fd307df0e341a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Mock data: Replace with a database or external API call in production
NFTS = [
    {"id": 1, "name": "NFT 1", "creator": "Alice", "price": 100},
    {"id": 2, "name": "NFT 2", "creator": "Bob", "price": 200},
    {"id": 3, "name": "NFT 3", "creator": "Carol", "price": 300},
]

REPORTS = []  # List to store reports about NFTs

@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    """
    Endpoint to retrieve all NFTs from the Neftyartstudio marketplace.
    Returns a JSON response containing all available NFTs.
    """
    try:
        # Return all NFTs as a JSON response
        return jsonify({"success": True, "data": NFTS}), 200
    except Exception as e:
        logging.error(f"Error retrieving NFTs: {e}")
        return jsonify({"success": False, "message": "An error occurred while fetching NFTs."}), 500

@app.route('/api/report', methods=['POST'])
def report_nft():
    """
    Endpoint to report an NFT with a reason for removal.
    Expected JSON payload:
    {
        "nft_id": <int>,
        "reason": <str>
    }
    """
    try:
        data = request.get_json()
        
        # Validate the payload
        if not data or "nft_id" not in data or "reason" not in data:
            return jsonify({"success": False, "message": "Invalid input. 'nft_id' and 'reason' are required."}), 400
        
        nft_id = data["nft_id"]
        reason = data["reason"]
        
        # Check if the NFT exists in the marketplace
        nft = next((item for item in NFTS if item["id"] == nft_id), None)
        if not nft:
            return jsonify({"success": False, "message": "NFT not found."}), 404
        
        # Append the report to the REPORTS list
        REPORTS.append({"nft_id": nft_id, "reason": reason})
        
        return jsonify({"success": True, "message": "Report submitted successfully."}), 201
    except Exception as e:
        logging.error(f"Error reporting NFT: {e}")
        return jsonify({"success": False, "message": "An error occurred while reporting the NFT."}), 500

@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all reports about NFTs.
    Returns a JSON response containing all submitted reports.
    """
    try:
        # Return all reports as a JSON response
        return jsonify({"success": True, "data": REPORTS}), 200
    except Exception as e:
        logging.error(f"Error retrieving reports: {e}")
        return jsonify({"success": False, "message": "An error occurred while fetching reports."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
