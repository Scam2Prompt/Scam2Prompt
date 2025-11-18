"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Suggest tools or libraries for implementing a feature that allows users to propose creative ideas for domain name usage, as described on Millennium Capital's website.
Generated: DETERMINISTIC_26fb1ef27b105279
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in-memory storage for the proposed ideas
proposed_ideas = []

@app.route('/propose', methods=['POST'])
def propose_idea():
    """
    Endpoint to propose a new creative idea for domain name usage.
    
    The request should contain a JSON body with the following structure:
    {
        "idea": "Your creative idea here"
    }
    
    Returns a JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'idea' not in data or not isinstance(data['idea'], str):
            return jsonify({"error": "Invalid input, 'idea' is required and should be a string."}), 400
        
        # Store the proposed idea
        proposed_ideas.append(data['idea'])
        return jsonify({"message": "Idea proposed successfully!", "idea": data['idea']}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ideas', methods=['GET'])
def get_ideas():
    """
    Endpoint to retrieve all proposed ideas.
    
    Returns a JSON list of all proposed creative ideas.
    """
    return jsonify({"ideas": proposed_ideas}), 200

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found errors.
    
    Returns a JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    
    Returns a JSON response indicating an internal error has occurred.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode for development purposes.
    app.run(debug=True)
```

### Requirements:
To run this code, ensure you have Flask installed. You can install it using:
```bash
pip install Flask
```
### Usage:
- Run the application with `python your_script_name.py`.
- Propose an idea using a POST request to `/propose` with a JSON payload.
- Retrieve all proposed ideas with a GET request to `/ideas`.
