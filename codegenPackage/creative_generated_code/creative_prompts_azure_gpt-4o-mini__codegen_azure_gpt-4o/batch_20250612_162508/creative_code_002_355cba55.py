"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiter.lol
Prompt: Develop an API that provides users with daily insights and tips to reclaim their time from social media, reflecting the urgent message from orbiter.lol about breaking free from digital control.
Generated: DETERMINISTIC_355cba55761f4b26
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Sample data: daily insights and tips to reclaim time from social media
INSIGHTS_AND_TIPS = [
    {
        "id": 1,
        "insight": "The average person spends over 2 hours a day on social media. Imagine what you could achieve with that time?",
        "tip": "Set app timers or limits on your social media usage starting today."
    },
    {
        "id": 2,
        "insight": "Social media algorithms are designed to keep you hooked. Recognize this and take back control of your attention.",
        "tip": "Use a focus app to block social media during work hours."
    },
    {
        "id": 3,
        "insight": "Studies show reducing social media usage improves mental health. Your mind deserves better care.",
        "tip": "Schedule 'no-social-media' hours daily and use that time for a hobby or reading."
    },
    {
        "id": 4,
        "insight": "Notifications are constant interruptions. Each break in focus compounds lost productivity.",
        "tip": "Turn off non-essential notifications for apps to regain focus."
    },
    {
        "id": 5,
        "insight": "Social media can distort your perception of reality. Remember, comparison is the thief of joy.",
        "tip": "Unfollow accounts that don't inspire or uplift you."
    }
]

@app.route('/api/insight', methods=['GET'])
def get_daily_insight():
    """
    API endpoint to get a daily insight and tip.
    Returns a random insight and tip from the predefined list.
    """
    try:
        # Select a random insight and tip
        insight = random.choice(INSIGHTS_AND_TIPS)
        response = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "insight": insight["insight"],
            "tip": insight["tip"]
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors and return a meaningful message
        error_response = {
            "error": "An internal error occurred while processing your request.",
            "details": str(e)
        }
        return jsonify(error_response), 500


@app.route('/api/insight/<int:id>', methods=['GET'])
def get_insight_by_id(id):
    """
    API endpoint to get a specific insight and tip by ID.
    If the ID does not exist, a 404 error is returned.
    """
    try:
        # Find the insight by ID
        insight = next((item for item in INSIGHTS_AND_TIPS if item["id"] == id), None)
        if insight:
            response = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "insight": insight["insight"],
                "tip": insight["tip"]
            }
            return jsonify(response), 200
        else:
            # Insight not found
            error_response = {
                "error": "Insight not found.",
                "details": f"No insight with ID {id} exists."
            }
            return jsonify(error_response), 404
    except Exception as e:
        # Handle unexpected errors and return a meaningful message
        error_response = {
            "error": "An internal error occurred while processing your request.",
            "details": str(e)
        }
        return jsonify(error_response), 500


@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    Returns a JSON response when a route or resource is not found.
    """
    response = {
        "error": "Resource not found.",
        "details": "The requested endpoint or resource does not exist."
    }
    return jsonify(response), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Returns a JSON response when an internal server error occurs.
    """
    response = {
        "error": "Internal server error.",
        "details": "An unexpected error occurred while handling your request."
    }
    return jsonify(response), 500


if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run(debug=True)
```
