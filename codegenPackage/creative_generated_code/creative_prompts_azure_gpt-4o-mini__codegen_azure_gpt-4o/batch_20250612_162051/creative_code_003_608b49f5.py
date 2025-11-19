"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perezbernalte.com
Prompt: Develop an API endpoint for a legal advice service that includes options for users to select areas like family law and administrative law, inspired by the offerings of Pérez Bernalte Abogados.
Generated: DETERMINISTIC_608b49f5eabc6a1e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample legal advice areas - inspired by Pérez Bernalte Abogados
LEGAL_AREAS = {
    "family_law": "Legal advice on family-related matters such as divorce, custody, and inheritance.",
    "administrative_law": "Assistance with administrative issues, including permits and appeals before public bodies.",
    "criminal_law": "Advice regarding criminal defense and legal representation in criminal cases.",
    "corporate_law": "Guidance on business and corporate legal matters, including contracts and compliance."
}

@app.route('/legal-advice', methods=['GET'])
def get_legal_advice():
    """
    API endpoint to fetch legal advice options based on selected areas.
    - Users can specify an area of law to get information.
    - If no area is specified, all available legal advice areas are returned.
    """
    try:
        # Get the query parameter for 'area'
        area = request.args.get('area')

        if area:
            # Check if the requested area exists in the predefined legal areas
            if area in LEGAL_AREAS:
                return jsonify({
                    "status": "success",
                    "area": area,
                    "description": LEGAL_AREAS[area]
                }), 200
            else:
                # Return error if area is not found
                return jsonify({
                    "status": "error",
                    "message": f"Legal area '{area}' not found. Available areas: {list(LEGAL_AREAS.keys())}"
                }), 404
        else:
            # Return all legal areas if no specific area is requested
            return jsonify({
                "status": "success",
                "areas": LEGAL_AREAS
            }), 200
    except Exception as e:
        # Catch unexpected errors
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
