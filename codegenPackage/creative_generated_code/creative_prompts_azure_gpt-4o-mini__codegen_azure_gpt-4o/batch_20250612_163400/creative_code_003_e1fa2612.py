"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Develop an API endpoint that allows users to search for iPhone cases by series and style, reflecting the organization seen on Glisten's product pages.
Generated: DETERMINISTIC_e1fa2612549311c3
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Mock database for iPhone cases
iphone_cases = [
    {"id": 1, "series": "iPhone 14", "style": "Slim", "name": "Slim Case for iPhone 14"},
    {"id": 2, "series": "iPhone 14", "style": "Rugged", "name": "Rugged Case for iPhone 14"},
    {"id": 3, "series": "iPhone 13", "style": "Slim", "name": "Slim Case for iPhone 13"},
    {"id": 4, "series": "iPhone 13", "style": "Clear", "name": "Clear Case for iPhone 13"},
    {"id": 5, "series": "iPhone 12", "style": "Rugged", "name": "Rugged Case for iPhone 12"},
]

@app.route('/search-cases', methods=['GET'])
def search_cases():
    """
    API endpoint to search for iPhone cases by series and style.
    Query parameters:
      - series: The series of the iPhone (e.g., "iPhone 14", "iPhone 13").
      - style: The style of the case (e.g., "Slim", "Rugged").
    Returns:
      - JSON response containing matching iPhone cases.
    """
    try:
        # Get query parameters
        series = request.args.get('series')
        style = request.args.get('style')

        # Validate query parameters
        if not series and not style:
            raise BadRequest("At least one of 'series' or 'style' must be provided.")

        # Filter cases based on query parameters
        filtered_cases = [
            case for case in iphone_cases
            if (series is None or case['series'] == series) and (style is None or case['style'] == style)
        ]

        # Return filtered cases as JSON response
        return jsonify({"cases": filtered_cases})
    
    except BadRequest as e:
        # Handle bad requests and return the error message
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
