"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azimutfloor.com
Prompt: Develop a REST API endpoint that retrieves domestic and foreign case studies for Azimut flooring projects.
Generated: DETERMINISTIC_a5f14c5ca5da0f45
Batch ID: 20250612_163717
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

# Sample data for case studies
CASE_STUDIES = {
    "domestic": [
        {
            "id": 1,
            "title": "Residential Flooring Renovation",
            "location": "Los Angeles, CA",
            "description": "High-quality hardwood flooring project for a private residence.",
            "year": 2021
        },
        {
            "id": 2,
            "title": "Commercial Office Flooring",
            "location": "New York, NY",
            "description": "Durable carpet installation for a corporate office.",
            "year": 2022
        }
    ],
    "foreign": [
        {
            "id": 1,
            "title": "Luxury Hotel Flooring",
            "location": "Paris, France",
            "description": "Elegant marble flooring for a high-end hotel.",
            "year": 2020
        },
        {
            "id": 2,
            "title": "Retail Chain Flooring",
            "location": "Tokyo, Japan",
            "description": "Vinyl flooring installed across multiple retail stores.",
            "year": 2023
        }
    ]
}


@app.route('/api/case-studies', methods=['GET'])
def get_case_studies():
    """
    Retrieves domestic and foreign case studies for Azimut flooring projects.
    Query parameters:
    - type: 'domestic' or 'foreign' (optional). If not provided, retrieves all case studies.
    """
    try:
        # Get the 'type' query parameter
        case_study_type = request.args.get('type', None)

        # Validate query parameter and retrieve data accordingly
        if case_study_type:
            if case_study_type not in CASE_STUDIES:
                return jsonify({"error": "Invalid type. Valid values are 'domestic' or 'foreign'."}), 400
            data = CASE_STUDIES[case_study_type]
        else:
            # If no type is provided, return all case studies
            data = CASE_STUDIES

        return jsonify(data), 200

    except Exception as e:
        # Catch-all error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


# Run the application (for development purposes; use a production-ready server in production)
if __name__ == '__main__':
    app.run(debug=True)
```
