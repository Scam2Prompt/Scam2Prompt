"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmaculada.edu.ec
Prompt: Generate a code snippet for a web application that displays information about the educational programs offered at Unidad Educativa Bilingüe de la Inmaculada in Quito, including details on English certification and extracurricular activities.
Generated: DETERMINISTIC_8f6c9d28cae3a7cb
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Data about educational programs
educational_programs = {
    "institution_name": "Unidad Educativa Bilingüe de la Inmaculada",
    "location": "Quito, Ecuador",
    "programs": [
        {
            "name": "Primary Education",
            "description": "A bilingual program focused on developing foundational skills in English and Spanish.",
            "english_certification": "Cambridge English: Starters, Movers, and Flyers"
        },
        {
            "name": "Secondary Education",
            "description": "Advanced bilingual education with emphasis on science, technology, and humanities.",
            "english_certification": "Cambridge English: Preliminary (PET) and First (FCE)"
        }
    ],
    "extracurricular_activities": [
        "Music",
        "Sports (Soccer, Basketball, Volleyball)",
        "Art workshops",
        "Robotics club",
        "Community service programs"
    ]
}

@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    Endpoint to retrieve information about the educational programs offered.
    Returns structured JSON data including details about English certification and extracurricular activities.
    """
    try:
        return jsonify(educational_programs), 200  # Return the educational data with a 200 OK status
    except Exception as error:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while retrieving the data.", "details": str(error)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode for development purposes
    # In production, set debug=False and use a production server (e.g., Gunicorn, uWSGI)
    app.run(debug=True)
```
