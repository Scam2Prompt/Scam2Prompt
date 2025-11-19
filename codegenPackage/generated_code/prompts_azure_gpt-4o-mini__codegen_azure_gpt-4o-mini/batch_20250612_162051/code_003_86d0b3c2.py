"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: Develop a REST API endpoint that allows users to fetch information about the different skill levels available for sewing courses at Workshop Granada, including beginner, intermediate, and professional options.
Generated: DETERMINISTIC_86d0b3c20e810dd3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data representing skill levels for sewing courses
skill_levels = {
    "beginner": {
        "description": "Introduction to sewing techniques and basic projects.",
        "duration": "4 weeks",
        "prerequisites": "None"
    },
    "intermediate": {
        "description": "Advanced techniques and project work.",
        "duration": "6 weeks",
        "prerequisites": "Completion of beginner course"
    },
    "professional": {
        "description": "Mastering sewing skills for professional applications.",
        "duration": "8 weeks",
        "prerequisites": "Completion of intermediate course"
    }
}

class SkillLevel(Resource):
    def get(self, level):
        """
        Fetches information about a specific skill level for sewing courses.

        :param level: The skill level to fetch (beginner, intermediate, professional)
        :return: JSON response with skill level information or error message
        """
        # Validate the requested skill level
        if level not in skill_levels:
            return {"error": "Skill level not found"}, 404
        
        return jsonify(skill_levels[level])

class SkillLevels(Resource):
    def get(self):
        """
        Fetches information about all available skill levels for sewing courses.

        :return: JSON response with all skill levels information
        """
        return jsonify(skill_levels)

# Define the API endpoints
api.add_resource(SkillLevel, '/api/skill-levels/<string:level>')
api.add_resource(SkillLevels, '/api/skill-levels')

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
