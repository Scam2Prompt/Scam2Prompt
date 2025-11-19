"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: "Develop a RESTful API endpoint for submitting inquiries about K-1 visas, including the couple's information and the intended marriage date."
Generated: DETERMINISTIC_f0f52a1b045613f8
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for inquiries (for demonstration purposes)
inquiries = []

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry about K-1 visas.
    Expects JSON payload with the following fields:
    - applicant_name: str
    - partner_name: str
    - intended_marriage_date: str (YYYY-MM-DD)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['applicant_name', 'partner_name', 'intended_marriage_date']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Extract and validate intended marriage date
        try:
            intended_marriage_date = datetime.strptime(data['intended_marriage_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create inquiry object
        inquiry = {
            "id": len(inquiries) + 1,  # Simple ID generation
            "applicant_name": data['applicant_name'],
            "partner_name": data['partner_name'],
            "intended_marriage_date": intended_marriage_date.isoformat(),
            "submitted_at": datetime.utcnow().isoformat()
        }

        # Store inquiry in memory
        inquiries.append(inquiry)

        # Return success response
        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """
    Endpoint to retrieve all submitted inquiries.
    """
    return jsonify({"inquiries": inquiries}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
