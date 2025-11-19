"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Design a web-based tool that generates personalized affirmations for users, drawing on the AI-powered support concepts mentioned in the Action Accelerator Academy.
Generated: DETERMINISTIC_a706307f967c911e
Batch ID: 20250612_160946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/generate_affirmation`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import random

# Initialize Flask application
app = Flask(__name__)

# Sample pool of affirmations
affirmations = [
    "You are capable of achieving great things.",
    "Your potential is limitless.",
    "Believe in yourself and all that you are.",
    "You have the power to create change.",
    "Every day brings new opportunities.",
    "You are enough just as you are.",
    "Your strengths are what make you unique.",
    "Embrace the journey of self-discovery."
]

@app.route('/generate_affirmation', methods=['POST'])
def generate_affirmation():
    """
    Generate a personalized affirmation for the user.
    Expects a JSON payload with a user's name.
    Returns a JSON response with the affirmation.
    """
    try:
        # Extract user data from request
        data = request.get_json()
        
        # Validate input
        if 'name' not in data:
            return jsonify({"error": "Missing 'name' in request payload."}), 400
        
        user_name = data['name']
        
        # Randomly select an affirmation
        affirmation = random.choice(affirmations)
        
        # Personalize the affirmation
        personalized_affirmation = f"{user_name}, {affirmation}"
        
        # Return the affirmation as a JSON response
        return jsonify({"affirmation": personalized_affirmation}), 200
    
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while generating the affirmation."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Requirements:
To run this code, you will need:
- Python 3.x installed
- Flask installed (`pip install Flask`)

### Running the Application:
1. Save the code to a file named `app.py`.
2. Open a terminal and navigate to the directory containing `app.py`.
3. Run the application with `python app.py`.
4. Send a POST request to `http://localhost:5000/generate_affirmation` with JSON payload containing the user's name to receive a personalized affirmation.
