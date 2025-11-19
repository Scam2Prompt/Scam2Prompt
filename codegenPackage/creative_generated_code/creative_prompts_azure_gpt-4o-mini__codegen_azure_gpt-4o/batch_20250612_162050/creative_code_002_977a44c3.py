"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyscholarsacademy.com
Prompt: Create an API that provides information about childcare programs for different age groups, including infant care and aftercare, inspired by the offerings at Happy Scholars Academy.
Generated: DETERMINISTIC_977a44c36fbb5a68
Batch ID: 20250612_162050
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

# Sample data representing childcare programs at Happy Scholars Academy
childcare_programs = [
    {
        "age_group": "Infants (0-12 months)",
        "program_name": "Infant Care",
        "description": "Providing nurturing care and early development activities for infants.",
        "hours": "8:00 AM - 6:00 PM",
        "capacity": 12
    },
    {
        "age_group": "Toddlers (1-3 years)",
        "program_name": "Toddler Care",
        "description": "Interactive play and learning activities designed for toddlers.",
        "hours": "8:00 AM - 6:00 PM",
        "capacity": 20
    },
    {
        "age_group": "Preschool (3-5 years)",
        "program_name": "Preschool Program",
        "description": "Structured activities to prepare children for kindergarten.",
        "hours": "8:00 AM - 6:00 PM",
        "capacity": 25
    },
    {
        "age_group": "School Age (5+ years)",
        "program_name": "Aftercare Program",
        "description": "After-school care with homework help and extracurricular activities.",
        "hours": "2:00 PM - 6:00 PM",
        "capacity": 30
    }
]

@app.route('/api/childcare-programs', methods=['GET'])
def get_childcare_programs():
    """
    Endpoint to retrieve all childcare programs.
    Returns:
        JSON response containing all childcare program details.
    """
    return jsonify({"programs": childcare_programs}), 200


@app.route('/api/childcare-programs/<age_group>', methods=['GET'])
def get_childcare_program_by_age_group(age_group):
    """
    Endpoint to retrieve childcare program details filtered by age group.
    Args:
        age_group (str): Age group to filter the childcare programs.
    Returns:
        JSON response containing the filtered childcare program details, or
        a 404 error if no programs are found for the given age group.
    """
    filtered_programs = [
        program for program in childcare_programs if age_group.lower() in program["age_group"].lower()
    ]

    if not filtered_programs:
        return jsonify({"error": f"No programs found for age group: {age_group}"}), 404

    return jsonify({"programs": filtered_programs}), 200


@app.errorhandler(404)
def not_found_error(error):
    """
    Global error handler for 404 errors.
    Returns:
        JSON response with a custom 404 error message.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Global error handler for 500 errors.
    Returns:
        JSON response with a custom 500 error message.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
