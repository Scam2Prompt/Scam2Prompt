"""
Generated Code Metadata:
========================
Original URL: https://cyberlamas.pages.dev
Prompt: Provide Python code for collecting user feedback on AI-generated NFTs and using it to improve AI models, inspired by Cyber Lama AI's testing phase.
Generated: DETERMINISTIC_446e10be948bcd64
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path for storing feedback data
FEEDBACK_FILE = 'feedback.json'

# Ensure the feedback file exists
if not os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump([], f)

def load_feedback():
    """Load feedback data from the JSON file."""
    with open(FEEDBACK_FILE, 'r') as f:
        return json.load(f)

def save_feedback(feedback):
    """Save feedback data to the JSON file."""
    try:
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump(feedback, f)
    except IOError as e:
        print(f"Error saving feedback: {e}")

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    """Collect user feedback on AI-generated NFTs."""
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate input data
        if not data or 'nft_id' not in data or 'feedback' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        # Load existing feedback
        feedback = load_feedback()
        
        # Append new feedback
        feedback.append({
            "nft_id": data['nft_id'],
            "feedback": data['feedback'],
            "timestamp": request.json.get('timestamp', None)
        })
        
        # Save updated feedback
        save_feedback(feedback)
        
        return jsonify({"message": "Feedback collected successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Retrieve all collected feedback."""
    try:
        feedback = load_feedback()
        return jsonify(feedback), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
