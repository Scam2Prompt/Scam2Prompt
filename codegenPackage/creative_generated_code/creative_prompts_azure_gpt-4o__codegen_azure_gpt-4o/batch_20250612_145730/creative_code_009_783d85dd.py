"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dpsg.live
Prompt: Provide a code example for tracking and displaying real-time lottery results on a gambling website, with filtering options by region (e.g., Singapore, Malaysia, Hong Kong).
Generated: DETERMINISTIC_783d85ddb6e929d6
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import threading
import time
import random

app = Flask(__name__)

# Mock data structure to store real-time lottery results
lottery_results = {
    "Singapore": [],
    "Malaysia": [],
    "Hong Kong": []
}

# Lock for thread-safe updates to lottery results
lock = threading.Lock()

def generate_mock_results():
    """
    Function to simulate real-time generation of lottery results.
    Runs in a separate thread to update results periodically.
    """
    regions = ["Singapore", "Malaysia", "Hong Kong"]
    while True:
        with lock:
            for region in regions:
                # Generate mock lottery numbers (e.g., 6 random numbers between 1 and 49)
                results = sorted(random.sample(range(1, 50), 6))
                lottery_results[region] = results
        # Sleep for 10 seconds before generating new results
        time.sleep(10)

@app.route('/lottery-results', methods=['GET'])
def get_lottery_results():
    """
    API endpoint to fetch lottery results.
    Allows filtering by region via query parameter 'region'.
    """
    region = request.args.get('region')  # Get region from query parameters

    with lock:
        if region:
            # Validate if the region exists
            if region not in lottery_results:
                return jsonify({"error": "Region not found"}), 404
            # Return results for the requested region
            return jsonify({region: lottery_results[region]})
        else:
            # Return results for all regions
            return jsonify(lottery_results)

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Start the mock result generation in a separate thread
    result_thread = threading.Thread(target=generate_mock_results, daemon=True)
    result_thread.start()

    # Start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```
