"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Create an API that provides personalized course recommendations for students based on their admission exam preparation needs, inspired by the offerings at Educar Comitán.
Generated: DETERMINISTIC_f315b4d18a6c27dc
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

# Sample data: Mock course catalog and admission exam needs
COURSE_CATALOG = [
    {"id": 1, "name": "Math Foundations", "topics": ["math", "algebra", "geometry"]},
    {"id": 2, "name": "Critical Reading Skills", "topics": ["reading", "comprehension", "language"]},
    {"id": 3, "name": "Science Essentials", "topics": ["science", "biology", "chemistry"]},
    {"id": 4, "name": "Essay Writing Mastery", "topics": ["writing", "grammar", "essays"]},
    {"id": 5, "name": "Exam Strategy and Time Management", "topics": ["strategy", "time management", "exam prep"]},
]

# API endpoint to get course recommendations
@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint to provide personalized course recommendations for students.

    Request JSON format:
    {
        "student_name": "John Doe",
        "prep_needs": ["math", "geometry", "time management"]
    }

    Response JSON format:
    {
        "student_name": "John Doe",
        "recommended_courses": [
            {"id": 1, "name": "Math Foundations"},
            {"id": 5, "name": "Exam Strategy and Time Management"}
        ]
    }
    """
    try:
        # Parse the request JSON data
        data = request.get_json()
        if not data or 'prep_needs' not in data or 'student_name' not in data:
            return jsonify({"error": "Invalid request format. Provide 'student_name' and 'prep_needs'."}), 400

        student_name = data['student_name']
        prep_needs = data['prep_needs']

        # Validate prep_needs as a list
        if not isinstance(prep_needs, list) or not all(isinstance(item, str) for item in prep_needs):
            return jsonify({"error": "'prep_needs' must be a list of strings."}), 400

        # Match prep needs with relevant courses
        recommended_courses = []
        for course in COURSE_CATALOG:
            if any(topic in course['topics'] for topic in prep_needs):
                recommended_courses.append({"id": course["id"], "name": course["name"]})

        # Return personalized recommendations
        response = {
            "student_name": student_name,
            "recommended_courses": recommended_courses
        }
        logging.info(f"Generated recommendations for {student_name}")
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"An error occurred while processing recommendations: {str(e)}")
        return jsonify({"error": "An internal server error occurred."}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
