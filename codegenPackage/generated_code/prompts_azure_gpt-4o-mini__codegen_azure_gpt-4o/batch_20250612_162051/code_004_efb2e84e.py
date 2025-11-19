"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Design a simple web application that uses SCOUT's technical documentation to help users select the right attachments for their tractors based on the tasks they plan to perform.
Generated: DETERMINISTIC_efb2e84ec6599c46
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: app.py
# Description: A simple web application to help users select the right tractor attachments based on tasks.
# Framework: Flask (Python)

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load SCOUT's technical documentation (mocked as a JSON file for this example)
try:
    with open('attachments_data.json', 'r') as file:
        attachments_data = json.load(file)
except FileNotFoundError:
    attachments_data = {}
    print("Error: attachments_data.json file not found. Ensure the file exists in the project directory.")
except json.JSONDecodeError:
    attachments_data = {}
    print("Error: Failed to decode attachments_data.json. Ensure the file contains valid JSON.")

@app.route('/')
def home():
    """
    Render the home page where users can input their task requirements.
    """
    return render_template('index.html')

@app.route('/get_attachments', methods=['POST'])
def get_attachments():
    """
    Endpoint to process user input and return recommended attachments.
    """
    try:
        # Get user input from the form
        task = request.form.get('task', '').lower()

        # Validate input
        if not task:
            return jsonify({'error': 'Task is required.'}), 400

        # Find matching attachments
        recommendations = [
            attachment for attachment in attachments_data.get('attachments', [])
            if task in attachment.get('supported_tasks', [])
        ]

        # Return recommendations
        if recommendations:
            return jsonify({'recommendations': recommendations}), 200
        else:
            return jsonify({'message': 'No attachments found for the specified task.'}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

# File: templates/index.html
# Description: HTML template for the home page.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tractor Attachments Selector</title>
</head>
<body>
    <h1>Tractor Attachments Selector</h1>
    <form action="/get_attachments" method="POST">
        <label for="task">Enter the task you plan to perform:</label>
        <input type="text" id="task" name="task" required>
        <button type="submit">Find Attachments</button>
    </form>
</body>
</html>

# File: attachments_data.json
# Description: Mocked SCOUT technical documentation data.

{
    "attachments": [
        {
            "name": "Plow",
            "supported_tasks": ["plowing", "tilling"]
        },
        {
            "name": "Harvester",
            "supported_tasks": ["harvesting", "reaping"]
        },
        {
            "name": "Seeder",
            "supported_tasks": ["seeding", "planting"]
        }
    ]
}
```
