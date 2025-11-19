"""
Generated Code Metadata:
========================
Original URL: https://paalai-io.web.app
Prompt: Generate an example of a multi-platform integration for a PAAL AI bot that handles chat sentiment analysis.
Generated: DETERMINISTIC_e7ee2169427c1490
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
import requests
from textblob import TextBlob
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Environment variables for platform API keys
SLACK_API_KEY = os.getenv("SLACK_API_KEY")
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
TEAMS_API_KEY = os.getenv("TEAMS_API_KEY")

# Helper function for sentiment analysis
def analyze_sentiment(message):
    """
    Analyze the sentiment of a given message using TextBlob.
    Returns a dictionary with polarity and subjectivity.
    """
    blob = TextBlob(message)
    return {
        "polarity": blob.sentiment.polarity,  # Range: [-1.0, 1.0]
        "subjectivity": blob.sentiment.subjectivity  # Range: [0.0, 1.0]
    }

# Slack integration
@app.route('/slack', methods=['POST'])
def slack_integration():
    """
    Endpoint to handle Slack messages.
    Expects a JSON payload with a 'message' field.
    """
    try:
        data = request.json
        message = data.get('message', '')
        sentiment = analyze_sentiment(message)
        response = {
            "platform": "Slack",
            "message": message,
            "sentiment": sentiment
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Discord integration
@app.route('/discord', methods=['POST'])
def discord_integration():
    """
    Endpoint to handle Discord messages.
    Expects a JSON payload with a 'message' field.
    """
    try:
        data = request.json
        message = data.get('message', '')
        sentiment = analyze_sentiment(message)
        response = {
            "platform": "Discord",
            "message": message,
            "sentiment": sentiment
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Microsoft Teams integration
@app.route('/teams', methods=['POST'])
def teams_integration():
    """
    Endpoint to handle Microsoft Teams messages.
    Expects a JSON payload with a 'message' field.
    """
    try:
        data = request.json
        message = data.get('message', '')
        sentiment = analyze_sentiment(message)
        response = {
            "platform": "Microsoft Teams",
            "message": message,
            "sentiment": sentiment
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for unsupported routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Main entry point
if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
```

This code provides a multi-platform integration for a PAAL AI bot that handles chat sentiment analysis for Slack, Discord, and Microsoft Teams. It uses Flask to create RESTful endpoints for each platform and TextBlob for sentiment analysis.
