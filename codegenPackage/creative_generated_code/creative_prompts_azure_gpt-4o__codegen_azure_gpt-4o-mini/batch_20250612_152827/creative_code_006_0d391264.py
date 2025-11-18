"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Create a chatbot using Python that provides information about Amir International Charity Organization's programs and assists users in making donations.
Generated: DETERMINISTIC_0d391264a28822c5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for Amir International Charity Organization's programs
programs = [
    {
        "id": 1,
        "name": "Education Program",
        "description": "Provides educational resources and support to underprivileged children."
    },
    {
        "id": 2,
        "name": "Healthcare Initiative",
        "description": "Offers medical assistance and healthcare services to communities in need."
    },
    {
        "id": 3,
        "name": "Disaster Relief Fund",
        "description": "Helps communities recover from natural disasters through immediate support and resources."
    }
]

@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    Endpoint to retrieve the list of charity programs.
    Returns a JSON list of programs.
    """
    return jsonify(programs), 200

@app.route('/api/donate', methods=['POST'])
def make_donation():
    """
    Endpoint to handle donations.
    Expects JSON with 'amount' and 'donor_name'.
    Returns a success message or an error message.
    """
    try:
        data = request.json
        
        # Validate input data
        if 'amount' not in data or 'donor_name' not in data:
            return jsonify({"error": "Missing required fields: 'amount' and 'donor_name'."}), 400
        
        amount = float(data['amount'])
        donor_name = data['donor_name']

        # Simulate donation processing
        if amount <= 0:
            return jsonify({"error": "Donation amount must be greater than zero."}), 400

        # Here you would typically process the donation (e.g., save to a database, call payment API)
        # For this example, we'll just log the donation
        print(f"Donation received from {donor_name}: ${amount:.2f}")

        return jsonify({"message": f"Thank you {donor_name} for your donation of ${amount:.2f}!"}), 201

    except ValueError:
        return jsonify({"error": "Invalid input data."}), 400
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error processing donation: {str(e)}")
        return jsonify({"error": "An error occurred while processing your donation."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
