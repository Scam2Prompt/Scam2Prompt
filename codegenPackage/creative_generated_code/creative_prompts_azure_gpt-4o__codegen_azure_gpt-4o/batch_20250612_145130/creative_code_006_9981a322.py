"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Create a REST API endpoint to interact with InMotion Central for managing WordPress Playgrounds, including handling expired environments.
Generated: DETERMINISTIC_9981a322c7a61851
Batch ID: 20250612_145130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.inmotioncentral.com/v1/playgrounds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

# Configuration
API_BASE_URL = "https://api.inmotioncentral.com/v1/playgrounds"
API_KEY = "your_api_key_here"  # Replace with your InMotion API Key

# Utility function to make API requests
def inmotion_api_request(endpoint, method="GET", data=None):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{API_BASE_URL}/{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            return None
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX, 5XX)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Endpoint to create a new WordPress Playground
@app.route('/playgrounds', methods=['POST'])
def create_playground():
    payload = request.json
    # Example payload: {"name": "test-playground", "duration": 60}
    if not payload or "name" not in payload or "duration" not in payload:
        return jsonify({"error": "Invalid request payload"}), 400

    response = inmotion_api_request(endpoint="", method="POST", data=payload)
    if "error" in response:
        return jsonify(response), 500
    return jsonify(response), 201

# Endpoint to get the list of Playgrounds
@app.route('/playgrounds', methods=['GET'])
def list_playgrounds():
    response = inmotion_api_request(endpoint="")
    if "error" in response:
        return jsonify(response), 500
    return jsonify(response), 200

# Endpoint to delete expired Playgrounds
@app.route('/playgrounds/cleanup', methods=['DELETE'])
def delete_expired_playgrounds():
    response = inmotion_api_request(endpoint="")
    if "error" in response:
        return jsonify(response), 500

    expired_playgrounds = []
    current_time = datetime.datetime.utcnow()
    for playground in response.get("data", []):
        expiration_time = datetime.datetime.strptime(playground["expiration"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if expiration_time < current_time:
            delete_response = inmotion_api_request(endpoint=f"{playground['id']}", method="DELETE")
            if "error" in delete_response:
                return jsonify(delete_response), 500
            expired_playgrounds.append(playground["id"])

    return jsonify({"deleted": expired_playgrounds}), 200

# Endpoint to delete a specific Playground by ID
@app.route('/playgrounds/<playground_id>', methods=['DELETE'])
def delete_playground(playground_id):
    response = inmotion_api_request(endpoint=playground_id, method="DELETE")
    if "error" in response:
        return jsonify(response), 500
    return jsonify({"message": f"Playground {playground_id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
