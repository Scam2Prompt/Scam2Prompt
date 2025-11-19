"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-protocol-seal.nfts2.me
Prompt: Can you provide a code snippet for integrating a reporting feature for scam NFTs in a web application?
Generated: DETERMINISTIC_1dfe6ed0e899dd33
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: report_scam_nft.py

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# A mock database for storing scam NFT reports
scam_reports_db = []

@app.route('/report-scam-nft', methods=['POST'])
def report_scam_nft():
    """
    Endpoint to report a scam NFT.
    Expected JSON format: 
    {
        "nft_id": "string",
        "nft_name": "string",
        "reporter_email": "string",
        "description": "string"
    }
    """
    try:
        # Parse the incoming request data
        data = request.get_json()
        
        # Validate the required fields
        required_fields = ["nft_id", "nft_name", "reporter_email", "description"]
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({"error": f"'{field}' is required."}), 400
        
        # Create a new report entry
        report_entry = {
            "nft_id": data["nft_id"],
            "nft_name": data["nft_name"],
            "reporter_email": data["reporter_email"],
            "description": data["description"],
            "timestamp": request.date
        }

        # Add the report to the mock database
        scam_reports_db.append(report_entry)
        
        # Return a success response
        return jsonify({"message": "Scam NFT report submitted successfully.", "report": report_entry}), 201
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing the request.", "details": str(e)}), 500


@app.route('/scam-reports', methods=['GET'])
def get_scam_reports():
    """
    Endpoint to retrieve all scam NFT reports.
    Returns a list of all reports in the database.
    """
    return jsonify({"scam_reports": scam_reports_db}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
