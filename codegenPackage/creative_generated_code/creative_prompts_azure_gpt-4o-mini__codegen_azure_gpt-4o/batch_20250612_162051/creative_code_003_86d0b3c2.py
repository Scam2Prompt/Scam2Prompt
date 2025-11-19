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
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing sewing course skill levels
skill_levels = [
    {
        "id": 1,
        "name": "Beginner",
        "description": "Perfect for those starting out with sewing, covering basic techniques and tools."
    },
    {
        "id": 2,
        "name": "Intermediate",
        "description": "Designed for those with some experience, introducing advanced techniques and projects."
    },
    {
        "id": 3,
        "name": "Professional",
        "description": "Tailored for experienced individuals, focusing on mastery and professional-level skills."
    }
]

@app.route('/api/sewing-courses/skill-levels', methods=['GET'])
def get_skill_levels():
    """
    REST API endpoint to fetch all skill levels for sewing courses.
    :return: JSON response containing a list of skill levels.
    """
    try:
        # Return the list of skill levels as a JSON response
        return jsonify({"skill_levels": skill_levels}), 200
    except Exception as e:
        # Handle unexpected errors and respond with a message
        return jsonify({"error": "An error occurred while fetching skill levels", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
