"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Create a chatbot using Python that assists users in navigating SKI Foundation's "E-Course Menjadi Pebisnis Pemula" program, providing course recommendations based on user preferences.
Generated: DETERMINISTIC_db87ef848487fda1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Import necessary libraries
from flask import Flask, request, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Predefined course recommendations for the program
COURSES = {
    "marketing": [
        "Introduction to Digital Marketing",
        "Social Media Marketing for Beginners",
        "Email Marketing Basics"
    ],
    "finance": [
        "Managing Personal Finances",
        "Basics of Business Accounting",
        "Understanding Cash Flow"
    ],
    "operations": [
        "Effective Time Management",
        "Optimizing Business Operations",
        "Building Scalable Processes"
    ],
    "general": [
        "Starting a Business from Scratch",
        "How to Develop a Business Plan",
        "Understanding Your Target Market"
    ]
}

# Function to recommend courses based on user preferences
def recommend_courses(preference):
    """
    Recommend courses based on user preference.
    
    Args:
        preference (str): The user's area of interest.
        
    Returns:
        list: A list of recommended courses.
    """
    # Check if preference is valid
    if preference.lower() in COURSES:
        return COURSES[preference.lower()], None
    else:
        # If preference is not valid, suggest available categories
        error_message = (
            "Invalid preference. Please choose from the following categories: "
            + ", ".join(COURSES.keys())
        )
        return None, error_message


@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint for the chatbot interaction.
    
    Returns:
        JSON: A response containing course recommendations or an error message.
    """
    try:
        # Parse user input from the request
        user_input = request.json.get("preference", "").strip()
        
        if not user_input:
            return jsonify({
                "error": "No preference provided. Please specify your area of interest."
            }), 400
        
        # Get recommendations based on user preference
        recommendations, error_message = recommend_courses(user_input)
        
        if recommendations:
            return jsonify({
                "message": "Here are some course recommendations for you:",
                "recommendations": recommendations
            })
        else:
            return jsonify({
                "error": error_message
            }), 400

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({
            "error": "An unexpected error occurred. Please try again later."
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the chatbot server is running.
    
    Returns:
        JSON: A response confirming the server's health.
    """
    return jsonify({"status": "Chatbot server is running"}), 200


# Run the Flask application
if __name__ == '__main__':
    # Use debug mode in development and disable it in production
    app.run(debug=True)
```
