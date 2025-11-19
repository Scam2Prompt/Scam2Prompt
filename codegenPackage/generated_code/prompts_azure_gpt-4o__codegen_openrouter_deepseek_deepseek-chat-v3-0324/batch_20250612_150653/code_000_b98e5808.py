"""
Generated Code Metadata:
========================
Original URL: https://kgtrading.co.jp
Prompt: The webpage does not contain relevant technical content for generating prompts related to code, APIs, or libraries.
Generated: DETERMINISTIC_b98e58080c5b66c2
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

# Initialize Flask application
app = Flask(__name__)

# Sample data store (in-memory for demonstration)
prompts_db = {
    "code": "Generate a clean, efficient Python function that...",
    "api": "Design a RESTful API endpoint for...",
    "library": "Create a Python library that provides functionality for..."
}

@app.route('/prompts/<prompt_type>', methods=['GET'])
def get_prompt(prompt_type):
    """
    Retrieve a prompt by type.
    
    Args:
        prompt_type (str): Type of prompt to retrieve (code, api, or library)
    
    Returns:
        JSON response containing the prompt text
    
    Raises:
        400: If prompt_type is invalid
        404: If prompt_type is not found
    """
    if not prompt_type or not isinstance(prompt_type, str):
        raise BadRequest("Prompt type must be a non-empty string")
    
    prompt = prompts_db.get(prompt_type.lower())
    if not prompt:
        raise NotFound(f"No prompt found for type: {prompt_type}")
    
    return jsonify({"prompt": prompt})

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_errors(error):
    """
    Handle application errors and return appropriate JSON responses.
    """
    response = jsonify({
        "error": error.description,
        "status_code": error.code
    })
    response.status_code = error.code
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
