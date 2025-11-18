"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write code to integrate Gitcoin Passport for bot protection and reputation building in a grants program, as described on the Gitcoin webpage.
Generated: DETERMINISTIC_ce3dc60a26ffc368
Batch ID: 20250612_154737
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gitcoin.co/passport/v1/": {
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
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Gitcoin Passport configuration
GITCOIN_PASSPORT_API_URL = "https://api.gitcoin.co/passport/v1/"
GITCOIN_API_KEY = "YOUR_GITCOIN_API_KEY"  # Replace with your actual API key

def verify_passport(passport_id):
    """
    Verifies a Gitcoin Passport using the provided passport ID.

    :param passport_id: The Gitcoin Passport ID to verify.
    :return: A dictionary containing verification results or an error message.
    """
    try:
        response = requests.get(
            f"{GITCOIN_PASSPORT_API_URL}verify/{passport_id}",
            headers={"Authorization": f"Bearer {GITCOIN_API_KEY}"}
        )
        
        # Raise an error for bad responses
        response.raise_for_status()
        
        # Return the JSON response if successful
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

@app.route('/api/grant', methods=['POST'])
def create_grant():
    """
    Endpoint to create a grant with Gitcoin Passport verification.

    :return: JSON response with the result of the grant creation.
    """
    data = request.json
    
    # Validate incoming request data
    passport_id = data.get("passport_id")
    if not passport_id:
        return jsonify({"error": "passport_id is required"}), 400

    # Verify the Gitcoin Passport
    verification_result = verify_passport(passport_id)
    
    if "error" in verification_result:
        return jsonify(verification_result), 400

    # Process grant creation logic here (stubbed out)
    # In a real application, you would implement grant creation logic, e.g., saving to a database.
    
    return jsonify({"message": "Grant created successfully", "verification": verification_result}), 201

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Make sure to replace `YOUR_GITCOIN_API_KEY` with your actual Gitcoin API key before running the code. The application is set to run on port 5000, and it provides an endpoint to create grants after verifying the Gitcoin Passport.
