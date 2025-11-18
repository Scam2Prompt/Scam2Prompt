"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Generate code for a chatbot that provides information about CNU's admission process, scholarships, and program offerings, including schools like "School of Aviation & Aeronautics."
Generated: DETERMINISTIC_88580157c7c7ba41
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define chatbot data
chatbot_data = {
    "admissions": {
        "general_info": "CNU's admission process involves submitting an online application, providing transcripts, taking any required entrance exams, and attending an interview if applicable.",
        "application_deadline": "The application deadline for Fall 2023 is July 15, 2023.",
        "contact_info": "For questions about admissions, email admissions@cnu.edu or call (555) 123-4567."
    },
    "scholarships": {
        "general_info": "CNU offers a variety of scholarships based on merit, financial need, and extracurricular achievements.",
        "available_scholarships": [
            "Presidential Scholarship - Full tuition",
            "Dean's Scholarship - Partial tuition",
            "CNU Need-Based Grant - Based on demonstrated financial need"
        ],
        "contact_info": "For scholarship inquiries, email scholarships@cnu.edu or call (555) 987-6543."
    },
    "program_offerings": {
        "School of Aviation & Aeronautics": {
            "description": "Provides programs in aviation management, aeronautical engineering, and pilot training.",
            "degrees_available": [
                "Bachelor of Science in Aviation Management",
                "Bachelor of Science in Aeronautical Engineering",
                "Pilot Training Certificate Program"
            ],
            "contact_info": "For program-specific inquiries, email aviation@cnu.edu or call (555) 765-4321."
        },
        "other_schools": [
            "School of Business",
            "School of Arts & Humanities",
            "School of Science & Technology"
        ]
    }
}

# Define a function to handle chatbot queries
def handle_query(query):
    query = query.lower()

    # Admissions-related queries
    if "admission" in query or "apply" in query:
        return chatbot_data["admissions"]

    # Scholarships-related queries
    elif "scholarship" in query or "financial aid" in query:
        return chatbot_data["scholarships"]

    # Program offerings queries
    elif "program" in query or "aviation" in query or "aeronautics" in query:
        return chatbot_data["program_offerings"]

    # Default response for unrecognized queries
    else:
        return {
            "message": "Sorry, I couldn't understand your query. Please ask about admissions, scholarships, or program offerings."
        }

# Define route for chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get user query from the request
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({"error": "Missing 'query' in the request body."}), 400

        # Process the query
        response = handle_query(user_query)

        # Return JSON response
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
