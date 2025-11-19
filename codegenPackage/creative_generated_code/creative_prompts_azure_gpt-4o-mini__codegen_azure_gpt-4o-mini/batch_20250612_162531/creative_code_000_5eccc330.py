"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claiming.website
Prompt: Generate a code snippet for a privacy policy generator API that complies with copyright regulations.
Generated: DETERMINISTIC_5eccc330c1f714dd
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample privacy policy templates
PRIVACY_POLICY_TEMPLATES = {
    "basic": "This privacy policy describes how we handle your personal information.",
    "detailed": (
        "This privacy policy describes how we collect, use, and protect your personal information. "
        "We are committed to safeguarding your privacy and ensuring that your personal information is handled "
        "in a safe and responsible manner."
    ),
}

@app.route('/generate_privacy_policy', methods=['POST'])
def generate_privacy_policy():
    """
    Endpoint to generate a privacy policy based on the selected template.
    
    Request Body:
    {
        "template_type": "basic" or "detailed"
    }
    
    Returns:
    JSON response containing the generated privacy policy.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or 'template_type' not in data:
            raise BadRequest("Request must include 'template_type'.")

        template_type = data['template_type']
        
        # Validate the requested template type
        if template_type not in PRIVACY_POLICY_TEMPLATES:
            return jsonify({"error": "Invalid template type. Available types: basic, detailed."}), 400
        
        # Generate the privacy policy
        privacy_policy = PRIVACY_POLICY_TEMPLATES[template_type]
        
        return jsonify({"privacy_policy": privacy_policy}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)  # Set debug=False for production
```
