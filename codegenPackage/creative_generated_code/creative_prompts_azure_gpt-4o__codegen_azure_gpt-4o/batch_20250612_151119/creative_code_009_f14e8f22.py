"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Develop a chatbot that can answer questions about paper quilling techniques, workshop schedules, and registration details, based on the ペーパークイリング カントリーフレンズ website.
Generated: DETERMINISTIC_f14e8f2239309558
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data simulating information from the ペーパークイリング カントリーフレンズ website
mock_data = {
    "quilling_techniques": {
        "basic_shapes": "Learn basic shapes such as coils, teardrops, and scrolls.",
        "advanced_shapes": "Explore advanced designs such as husking and comb techniques.",
        "tips": "Use high-quality paper strips and quilling tools for best results.",
    },
    "workshop_schedule": {
        "workshops": [
            {"date": "2023-11-15", "topic": "Introduction to Paper Quilling", "location": "Tokyo"},
            {"date": "2023-12-05", "topic": "Advanced Quilling Techniques", "location": "Osaka"},
        ]
    },
    "registration_details": {
        "process": "Visit our website and fill out the registration form under the 'Workshops' section.",
        "contact": "For assistance, email us at info@countryfriends.jp."
    },
}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    """
    Endpoint to handle chatbot requests. 
    Expected input format:
    {
        "query": "Your question",
        "context": "Optional context for the question"
    }
    """
    try:
        # Parse request data
        user_data = request.get_json()
        query = user_data.get("query", "").lower()

        # Check for empty query
        if not query:
            return jsonify({"error": "Please provide a query."}), 400

        # Determine response based on query content
        if "technique" in query or "shape" in query:
            response = mock_data["quilling_techniques"]
        elif "workshop" in query or "schedule" in query:
            response = mock_data["workshop_schedule"]
        elif "register" in query or "registration" in query:
            response = mock_data["registration_details"]
        else:
            response = {"message": "Sorry, I couldn't understand your question. Please try rephrasing or ask about quilling techniques, workshop schedules, or registration details."}

        # Respond with the appropriate data
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

Note: Install Flask (`pip install flask`) before running this code, and ensure you're using Python 3.
