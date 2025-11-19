"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write a code snippet to create a survey that requires token authentication, inspired by the Moonbirds survey model.
Generated: DETERMINISTIC_9a069ad19c5c03d4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

# Secret key for encoding and decoding JWT tokens
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Sample survey data (in a real application this would likely be stored in a database)
surveys = []

# Function to generate a token
def generate_token(user_id):
    """Generate a JWT token for user authentication."""
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    }, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Decorator to require token authentication
def token_required(f):
    """Decorator to protect routes requiring token authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Check if token is passed in the header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        # If no token is provided, return unauthorized error
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode the token to get the user ID
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/create_survey', methods=['POST'])
@token_required
def create_survey(current_user):
    """Endpoint to create a new survey."""
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'questions' not in data:
            return jsonify({'message': 'Invalid data!'}), 400
        
        # Create a new survey
        new_survey = {
            'id': len(surveys) + 1,
            'title': data['title'],
            'questions': data['questions'],
            'created_by': current_user,
            'created_at': datetime.utcnow()
        }
        surveys.append(new_survey)
        return jsonify({'message': 'Survey created successfully!', 'survey': new_survey}), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/surveys', methods=['GET'])
def get_surveys():
    """Endpoint to get the list of surveys."""
    return jsonify({'surveys': surveys}), 200

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
