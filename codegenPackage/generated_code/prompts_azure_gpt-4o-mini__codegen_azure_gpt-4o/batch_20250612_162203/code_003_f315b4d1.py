"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Create an API that provides personalized course recommendations for students based on their admission exam preparation needs, inspired by the offerings at Educar Comitán.
Generated: DETERMINISTIC_f315b4d18a6c27dc
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data: Courses offered by Educar Comitán
COURSES = [
    {"id": 1, "name": "Mathematics Fundamentals", "category": "Math", "difficulty": "Beginner"},
    {"id": 2, "name": "Advanced Algebra", "category": "Math", "difficulty": "Advanced"},
    {"id": 3, "name": "Physics Basics", "category": "Science", "difficulty": "Beginner"},
    {"id": 4, "name": "Organic Chemistry", "category": "Science", "difficulty": "Intermediate"},
    {"id": 5, "name": "Critical Reading Skills", "category": "Language", "difficulty": "Beginner"},
    {"id": 6, "name": "Essay Writing Mastery", "category": "Language", "difficulty": "Advanced"},
]

# Error messages
ERROR_MESSAGES = {
    "missing_data": "Missing required data in the request.",
    "invalid_category": "Invalid category provided. Valid categories are: Math, Science, Language.",
    "invalid_difficulty": "Invalid difficulty level provided. Valid levels are: Beginner, Intermediate, Advanced."
}

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint to get personalized course recommendations based on student preferences.
    Expects a JSON payload with 'category' and 'difficulty' fields.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            logging.error("Request payload is empty.")
            return jsonify({"error": ERROR_MESSAGES["missing_data"]}), 400

        category = data.get("category")
        difficulty = data.get("difficulty")

        # Validate input
        valid_categories = {"Math", "Science", "Language"}
        valid_difficulties = {"Beginner", "Intermediate", "Advanced"}

        if category not in valid_categories:
            logging.error(f"Invalid category: {category}")
            return jsonify({"error": ERROR_MESSAGES["invalid_category"]}), 400

        if difficulty not in valid_difficulties:
            logging.error(f"Invalid difficulty: {difficulty}")
            return jsonify({"error": ERROR_MESSAGES["invalid_difficulty"]}), 400

        # Filter courses based on preferences
        recommendations = [
            course for course in COURSES
            if course["category"] == category and course["difficulty"] == difficulty
        ]

        # Return recommendations
        logging.info(f"Recommendations generated for category '{category}' and difficulty '{difficulty}'.")
        return jsonify({"recommendations": recommendations}), 200

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/')
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "API is running"}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
