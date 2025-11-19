"""
Generated Code Metadata:
========================
Original URL: https://votex.sbs
Prompt: Design an AI-powered animation production tool, similar to Cheehoo's platform, and describe its architecture and potential applications.
Generated: DETERMINISTIC_e3c7fb651415aae0
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a configuration for the AI model
class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "path/to/your/model")
    MAX_ANIMATION_LENGTH = 60  # Maximum length of animation in seconds

# Load the AI model (placeholder for actual model loading logic)
def load_model(model_path):
    # Placeholder for model loading logic
    logging.info(f"Loading model from {model_path}")
    # Simulate model loading
    return "Loaded AI Model"

# Initialize the AI model
ai_model = load_model(Config.MODEL_PATH)

# Define a route for generating animations
@app.route('/generate-animation', methods=['POST'])
def generate_animation():
    """
    Generate an animation based on user input.
    Expects a JSON payload with 'script' and 'length' fields.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            raise BadRequest("No input data provided")

        script = data.get('script')
        length = data.get('length', Config.MAX_ANIMATION_LENGTH)

        # Validate input data
        if not script or not isinstance(length, int) or length <= 0:
            raise BadRequest("Invalid input data: 'script' must be a non-empty string and 'length' must be a positive integer")

        # Simulate animation generation (placeholder for actual AI processing)
        animation_output = f"Animation based on script: '{script}' with length: {length} seconds"
        logging.info("Animation generated successfully")

        # Return the generated animation as a JSON response
        return jsonify({"status": "success", "animation": animation_output}), 200

    except BadRequest as e:
        logging.error(f"Bad request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

# Define a route for health check
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return jsonify({"status": "healthy"}), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- This code sets up a basic Flask application that simulates an AI-powered animation generation tool.
- It includes error handling for invalid input and unexpected errors.
- The AI model loading is simulated; in a production scenario, you would replace this with actual model loading logic.
- The application includes a health check endpoint to verify that the service is running.
