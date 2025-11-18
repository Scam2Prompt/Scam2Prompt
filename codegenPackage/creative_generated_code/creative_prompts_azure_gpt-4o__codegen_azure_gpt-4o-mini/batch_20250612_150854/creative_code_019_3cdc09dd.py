"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Develop a feature that educates users on avoiding scams and false information in investments, inspired by Immediate Migna's focus on navigating challenges in the financial world.
Generated: DETERMINISTIC_3cdc09ddc2df6e79
Batch ID: 20250612_150854
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

# Initialize the Flask application
app = Flask(__name__)

# Sample data for educational content
scam_tips = [
    {
        "tip": "Always verify the source of information.",
        "description": "Cross-check any investment advice with reputable financial news outlets."
    },
    {
        "tip": "Be cautious of high-pressure tactics.",
        "description": "Scammers often create a sense of urgency to rush your decision."
    },
    {
        "tip": "Never share personal information.",
        "description": "Do not provide sensitive information like Social Security numbers to unverified sources."
    },
    {
        "tip": "Look for red flags.",
        "description": "Promises of guaranteed returns or unsolicited offers are signs to be wary of."
    },
    {
        "tip": "Research before investing.",
        "description": "Use tools and resources to investigate the legitimacy of the investment opportunity."
    }
]

@app.route('/api/scam-tips', methods=['GET'])
def get_scam_tips():
    """
    Endpoint to retrieve tips on avoiding scams and false information in investments.
    Returns a JSON response containing the tips.
    """
    try:
        # Return the tips as a JSON response
        return jsonify(scam_tips), 200
    except Exception as e:
        # Handle any exceptions and return a server error response
        return jsonify({"error": "An error occurred while retrieving tips", "details": str(e)}), 500

@app.route('/api/scam-tips/<int:tip_id>', methods=['GET'])
def get_scam_tip(tip_id):
    """
    Endpoint to retrieve a specific tip by its ID.
    Returns a JSON response containing the tip details.
    """
    try:
        # Validate that the tip_id is within the valid range
        if tip_id < 0 or tip_id >= len(scam_tips):
            return jsonify({"error": "Tip not found"}), 404
        
        # Return the specific tip as a JSON response
        return jsonify(scam_tips[tip_id]), 200
    except Exception as e:
        # Handle any exceptions and return a server error response
        return jsonify({"error": "An error occurred while retrieving the tip", "details": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
