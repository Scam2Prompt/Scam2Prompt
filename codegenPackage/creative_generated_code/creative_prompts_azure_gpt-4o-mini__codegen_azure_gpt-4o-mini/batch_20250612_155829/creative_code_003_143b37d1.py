"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarparasanar.com.mx
Prompt: Develop an API endpoint that retrieves information about available online therapy modalities, including individual and couple therapy options.
Generated: DETERMINISTIC_143b37d1afc53f15
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Sample data for therapy modalities
therapy_modalities = {
    "individual": {
        "description": "One-on-one therapy sessions with a licensed therapist.",
        "duration": "50 minutes",
        "frequency": "Weekly",
        "methods": ["Cognitive Behavioral Therapy", "Mindfulness-Based Therapy", "Humanistic Therapy"]
    },
    "couple": {
        "description": "Therapy sessions for couples to improve communication and resolve conflicts.",
        "duration": "60 minutes",
        "frequency": "Bi-weekly",
        "methods": ["Emotionally Focused Therapy", "Gottman Method", "Imago Therapy"]
    }
}

@app.route('/api/therapy/modalities', methods=['GET'])
def get_therapy_modalities():
    """
    Retrieve available online therapy modalities.

    Returns:
        JSON response containing available therapy modalities.
    """
    try:
        return jsonify(therapy_modalities), 200  # Return modalities with HTTP status 200
    except Exception as e:
        # Log the error (here we just print it, but in production, use logging)
        print(f"Error retrieving therapy modalities: {e}")
        return jsonify({"error": "Unable to retrieve therapy modalities"}), 500  # Return error response with status 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```
