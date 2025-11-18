"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write code to create a token-gated survey application similar to the Moonbirds Q1 '24 Holder Survey, ensuring secure access for users with valid tokens.
Generated: DETERMINISTIC_0da9e8eaa0a833ff
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, abort
import jwt
from functools import wraps
import os

# Initialize Flask app
app = Flask(__name__)

# Secret key for token verification (use environment variable for security)
JWT_SECRET = os.getenv("JWT_SECRET", "ReplaceThisWithYourSecretKey")

# Token-gated access decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            # Return 401 if no token is provided
            abort(401, description="Missing token")
        try:
            # Verify the token
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.user = decoded_token  # Pass decoded token data to the route
        except jwt.ExpiredSignatureError:
            abort(403, description="Token has expired")
        except jwt.InvalidTokenError:
            abort(403, description="Invalid token")
        return f(*args, **kwargs)
    return decorated

# Survey questions (could be replaced with a database)
SURVEY_QUESTIONS = [
    {"id": 1, "question": "What is your favorite feature of Moonbirds?"},
    {"id": 2, "question": "What new feature would you like to see?"},
    {"id": 3, "question": "How would you rate your overall experience?"},
]

# Route to fetch survey questions (token gated)
@app.route('/survey', methods=['GET'])
@token_required
def get_survey():
    """
    Endpoint to retrieve the survey questions. Requires a valid token.
    """
    return jsonify({"questions": SURVEY_QUESTIONS}), 200

# Route to submit survey answers (token gated)
@app.route('/survey/submit', methods=['POST'])
@token_required
def submit_survey():
    """
    Endpoint to submit survey answers. Requires a valid token.
    """
    try:
        # Ensure JSON body is provided
        if not request.json:
            abort(400, description="Request must be JSON")
        
        answers = request.json.get('answers')
        if not answers:
            abort(400, description="Answers are required")
        
        # Validate answers structure
        if not isinstance(answers, list) or len(answers) != len(SURVEY_QUESTIONS):
            abort(400, description="Answers must match the survey structure")
        
        # Here we would store the results in a database (not implemented in this example)
        # For now, we'll just return a success message
        return jsonify({"message": "Survey submitted successfully"}), 200
    except Exception as e:
        # Catch any unexpected error
        abort(500, description=str(e))

# Error handler for custom error messages
@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(500)
def handle_error(e):
    """
    Handle errors with custom messages and status codes.
    """
    return jsonify({"error": str(e.description)}), e.code

# Start the Flask application
if __name__ == '__main__':
    # Use environment variable for port, defaulting to 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```
