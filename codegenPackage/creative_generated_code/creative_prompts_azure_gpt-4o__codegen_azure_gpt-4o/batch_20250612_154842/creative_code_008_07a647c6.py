"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totalshopexchange.com
Prompt: Write code to integrate a donation system for a charity organization like the Regional Animal Protection Society, inspired by the projects listed on Total Shop Exchange.
Generated: DETERMINISTIC_07a647c6a85b1d63
Batch ID: 20250612_154842
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

# Mock data structure to store donations
donation_data = {
    "total_donations": 0,
    "donors": []
}

# Endpoint to view donation summary
@app.route('/donation-summary', methods=['GET'])
def get_donation_summary():
    """
    Returns the total amount of donations and a list of donors.
    """
    return jsonify({
        "status": "success",
        "data": donation_data
    })

# Endpoint to process a donation
@app.route('/donate', methods=['POST'])
def donate():
    """
    Accepts donation details and updates the donation summary.
    Input JSON format:
    {
        "name": "Donor Name",
        "amount": 100.0
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        
        if not data or 'name' not in data or 'amount' not in data:
            return jsonify({
                "status": "error",
                "message": "Invalid donation data. Please provide 'name' and 'amount'."
            }), 400

        name = data['name']
        amount = float(data['amount'])
        
        if amount <= 0:
            return jsonify({
                "status": "error",
                "message": "Donation amount must be greater than zero."
            }), 400

        # Update donation data
        donation_data['total_donations'] += amount
        donation_data['donors'].append({
            "name": name,
            "amount": amount
        })

        return jsonify({
            "status": "success",
            "message": f"Thank you for your donation, {name}!",
            "current_total": donation_data['total_donations']
        })
    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid donation amount. Please provide a numeric value."
        }), 400
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }), 500

# Endpoint to reset donation data (admin-only)
@app.route('/reset-donations', methods=['POST'])
def reset_donations():
    """
    Resets the donation data. This should only be accessed by an admin.
    """
    try:
        # For simplicity, we use a hardcoded admin key. This should ideally be replaced by proper authentication.
        admin_key = request.headers.get('Admin-Key')
        
        if admin_key != "secret_admin_key":
            return jsonify({
                "status": "error",
                "message": "Unauthorized access. Admin key required."
            }), 403

        # Reset donation data
        donation_data['total_donations'] = 0
        donation_data['donors'] = []

        return jsonify({
            "status": "success",
            "message": "Donation data successfully reset."
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
