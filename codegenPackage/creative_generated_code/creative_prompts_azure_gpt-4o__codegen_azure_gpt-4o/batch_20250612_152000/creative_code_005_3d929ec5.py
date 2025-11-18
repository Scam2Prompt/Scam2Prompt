"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minting-genesisrunes.pages.dev
Prompt: Develop a script to track the total number of "Genesis Runes" minted out of a maximum supply of 18,000 and display the remaining count dynamically.
Generated: DETERMINISTIC_3d929ec568d07d02
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify

# Flask app setup
app = Flask(__name__)

# Constants: Maximum supply of Genesis Runes
MAX_SUPPLY = 18000

# Variable to track the total minted Genesis Runes
total_minted = 0


@app.route('/mint', methods=['POST'])
def mint_rune():
    """
    Endpoint to mint a Genesis Rune.
    Increases the minted count by 1, if maximum supply is not exceeded.
    """
    global total_minted

    # Check if maximum supply has been reached
    if total_minted >= MAX_SUPPLY:
        return jsonify({"error": "Maximum supply reached. No more Genesis Runes can be minted."}), 400

    # Mint a Genesis Rune
    total_minted += 1
    remaining = MAX_SUPPLY - total_minted

    return jsonify({
        "message": "Genesis Rune minted successfully!",
        "total_minted": total_minted,
        "remaining_supply": remaining
    }), 200


@app.route('/status', methods=['GET'])
def check_status():
    """
    Endpoint to check the current status of the minted Genesis Runes.
    """
    remaining = MAX_SUPPLY - total_minted

    return jsonify({
        "total_minted": total_minted,
        "remaining_supply": remaining
    }), 200


# Error Handling: Catch-all route for undefined endpoints
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle undefined routes gracefully.
    """
    return jsonify({"error": "Endpoint not found. Please check the URL and HTTP method."}), 404


# Start the Flask server
if __name__ == '__main__':
    # Run the server on localhost and port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
```
