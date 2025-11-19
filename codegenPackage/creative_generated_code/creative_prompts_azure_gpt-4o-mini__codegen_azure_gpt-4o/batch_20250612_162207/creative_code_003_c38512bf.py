"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rodi.co.id
Prompt: Develop an API endpoint that allows users to submit their experiences with local welfare programs, akin to the community engagement highlighted by Rodi on his platform.
Generated: DETERMINISTIC_c38512bf9c204c33
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for submitted experiences (for demo purposes)
experiences = []

# API Endpoint: Submit an experience
@app.route('/submit_experience', methods=['POST'])
def submit_experience():
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'program_name', 'experience']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({"error": f"Missing or empty '{field}' field"}), 400
        
        # Construct experience object
        experience = {
            "id": len(experiences) + 1,  # Generate a unique ID for the experience
            "name": data['name'],
            "email": data['email'],
            "program_name": data['program_name'],
            "experience": data['experience'],
            "timestamp": datetime.utcnow().isoformat()  # Store submission time in UTC
        }
        
        # Store the experience (in-memory list, can be replaced with a database)
        experiences.append(experience)
        
        # Return success response
        return jsonify({"message": "Experience submitted successfully", "experience": experience}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# API Endpoint: Get all submitted experiences (for demo purposes)
@app.route('/experiences', methods=['GET'])
def get_experiences():
    try:
        return jsonify({"experiences": experiences}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Main application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
