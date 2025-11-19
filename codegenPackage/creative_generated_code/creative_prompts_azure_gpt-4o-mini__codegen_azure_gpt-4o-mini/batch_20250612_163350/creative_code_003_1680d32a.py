"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Develop a RESTful API endpoint that responds with a custom message, mimicking the repetitive nature of the haitwik website.
Generated: DETERMINISTIC_1680d32a948f2661
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/custom-message', methods=['GET'])
def custom_message():
    """
    Handles GET requests to the /custom-message endpoint.
    Returns a custom message mimicking the repetitive nature of the haitwik website.
    
    Query Parameters:
        repeat_count (int): Number of times the custom message should be repeated.
                            Defaults to 1 if not provided or invalid.

    Returns:
        JSON response containing the custom message.
    """
    try:
        # Get the repeat_count from the query parameters
        repeat_count = request.args.get('repeat_count', default=1, type=int)
        
        # Validate repeat_count to be a positive integer
        if repeat_count < 1:
            return jsonify({"error": "repeat_count must be a positive integer."}), 400
        
        # Custom message to be repeated
        message = "This is a custom message mimicking the repetitive nature of haitwik."
        
        # Create the response by repeating the message
        response_message = ' '.join([message] * repeat_count)
        
        # Return the response as JSON
        return jsonify({"message": response_message})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

Make sure to install Flask before running the code by executing `pip install Flask`.
