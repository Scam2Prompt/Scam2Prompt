"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workshopgranada.com
Prompt: Develop a REST API endpoint that allows users to fetch information about the different skill levels available for sewing courses at Workshop Granada, including beginner, intermediate, and professional options.
Generated: DETERMINISTIC_86d0b3c20e810dd3
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
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for sewing skill levels
skill_levels = {
    "beginner": {
        "description": "Introduction to sewing techniques and basic projects.",
        "duration": "4 weeks",
        "prerequisites": "None"
    },
    "intermediate": {
        "description": "Enhancing sewing skills with more complex projects.",
        "duration": "6 weeks",
        "prerequisites": "Completion of Beginner course or equivalent."
    },
    "professional": {
        "description": "Advanced techniques and professional sewing practices.",
        "duration": "8 weeks",
        "prerequisites": "Completion of Intermediate course or equivalent."
    }
}

class SkillLevels(Resource):
    """
    Resource to manage sewing skill levels.
    """

    def get(self):
        """
        GET method to fetch the available skill levels for sewing courses.

        Returns:
            Response (dict): JSON object containing skill levels data.
        """
        try:
            return jsonify(skill_levels), 200
        except Exception as e:
            # Log the error (logging not shown here for brevity)
            return {"error": "An error occurred while fetching skill levels."}, 500

# Adding the resource to the API with the appropriate endpoint
api.add_resource(SkillLevels, '/api/skill-levels')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug to False for production
```
