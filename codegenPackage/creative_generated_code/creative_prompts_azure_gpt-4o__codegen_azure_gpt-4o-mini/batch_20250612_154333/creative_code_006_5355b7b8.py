"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Provide an API recommendation for generating adhesive labels with options for text, color, and size customization, suitable for applications like those mentioned on Etiquettetout.com.
Generated: DETERMINISTIC_5355b7b841ea97f9
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
import random

app = Flask(__name__)
api = Api(app)

# List of supported colors and sizes for the labels
SUPPORTED_COLORS = ["red", "blue", "green", "yellow", "black", "white"]
SUPPORTED_SIZES = ["small", "medium", "large"]

class LabelGenerator(Resource):
    def get(self):
        """
        Generate a label based on query parameters.

        Query Parameters:
        - text (str): The text to display on the label.
        - color (str): The color of the label text.
        - size (str): The size of the label.

        Returns:
        - JSON object with label details or error message.
        """
        try:
            # Retrieve query parameters
            text = request.args.get('text')
            color = request.args.get('color')
            size = request.args.get('size')

            # Validate input parameters
            if not text or not isinstance(text, str):
                raise BadRequest("The 'text' parameter is required and must be a string.")
            
            if color and color not in SUPPORTED_COLORS:
                raise BadRequest(f"Invalid color. Supported colors: {', '.join(SUPPORTED_COLORS)}.")
            
            if size and size not in SUPPORTED_SIZES:
                raise BadRequest(f"Invalid size. Supported sizes: {', '.join(SUPPORTED_SIZES)}.")
            
            # Default values if not provided
            color = color if color else random.choice(SUPPORTED_COLORS)
            size = size if size else random.choice(SUPPORTED_SIZES)

            # Create a label object
            label = {
                "text": text,
                "color": color,
                "size": size
            }

            return jsonify(label)

        except BadRequest as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "An unexpected error occurred."}), 500

# Define the API endpoint
api.add_resource(LabelGenerator, '/generate-label')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
