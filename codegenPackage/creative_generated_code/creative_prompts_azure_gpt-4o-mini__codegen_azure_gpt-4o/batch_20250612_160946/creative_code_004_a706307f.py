"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Design a web-based tool that generates personalized affirmations for users, drawing on the AI-powered support concepts mentioned in the Action Accelerator Academy.
Generated: DETERMINISTIC_a706307f967c911e
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to generate personalized affirmations using AI

from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import HTTPException
import openai
import logging
import os

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI API (replace "your_openai_api_key" with your actual key)
openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Logging configuration for debugging and error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Error handling for API errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": str(e)}), e.code
    logging.error(f"Unexpected error: {str(e)}")
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route to display the homepage with the form
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle affirmation generation
@app.route("/generate", methods=["POST"])
def generate_affirmation():
    try:
        # Get user-provided data from the form submission
        data = request.form
        name = data.get("name", "").strip()
        goal = data.get("goal", "").strip()

        # Validate input
        if not name or not goal:
            return jsonify({"error": "Name and goal are required fields"}), 400

        # Prompt for GPT-3 or GPT-4
        prompt = f"""
        Create a personalized affirmation for someone named {name} who is working towards the goal of {goal}.
        Use supportive and motivational language inspired by the concepts of Action Accelerator Academy.
        """

        # Generate affirmation using OpenAI's GPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use an appropriate AI model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the affirmation from the AI response
        affirmation = response.choices[0].text.strip()

        # Return the affirmation to the user
        return jsonify({"affirmation": affirmation})
    except Exception as e:
        logging.error(f"Error generating affirmation: {str(e)}")
        return jsonify({"error": "Failed to generate affirmation"}), 500

# Run the application in debug mode (turn off debug in production)
if __name__ == "__main__":
    app.run(debug=True)
```

### `index.html` (place this in a `templates/` folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Affirmation Generator</title>
</head>
<body>
    <h1>Personalized Affirmation Generator</h1>
    <form action="/generate" method="post">
        <label for="name">Your Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="goal">Your Goal:</label><br>
        <input type="text" id="goal" name="goal" required><br><br>
        
        <button type="submit">Generate Affirmation</button>
    </form>
    
    <div id="affirmation">
        <!-- Affirmation will be displayed here -->
    </div>
</body>
</html>
```

### Notes:
- Replace `your_openai_api_key` with a valid OpenAI API key or set the key in your environment variables (`OPENAI_API_KEY`).
- Install required dependencies: `pip install flask openai`.
- This is a basic implementation. Consider adding authentication, rate-limiting, and HTTPS in production for security purposes.
