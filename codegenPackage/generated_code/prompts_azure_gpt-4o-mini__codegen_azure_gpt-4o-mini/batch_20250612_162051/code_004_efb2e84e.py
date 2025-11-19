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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import json

# Initialize the Flask application
app = Flask(__name__)

# Load SCOUT's technical documentation (mock data for this example)
# In a real application, this data would be loaded from a database or an API
with open('attachments_data.json') as f:
    attachments_data = json.load(f)

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/get_attachments', methods=['POST'])
def get_attachments():
    """Return a list of attachments based on the user's selected task."""
    try:
        # Get the task from the request
        task = request.json.get('task')
        
        # Validate the input
        if not task:
            return jsonify({'error': 'Task is required'}), 400
        
        # Find attachments that match the task
        matching_attachments = [
            attachment for attachment in attachments_data 
            if task.lower() in attachment['tasks']
        ]
        
        # Return the matching attachments
        return jsonify(matching_attachments), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tractor Attachment Selector</title>
    <script>
        async function fetchAttachments() {
            const task = document.getElementById('task').value;
            const response = await fetch('/get_attachments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task })
            });

            const data = await response.json();
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (response.ok) {
                data.forEach(attachment => {
                    const div = document.createElement('div');
                    div.textContent = attachment.name;
                    resultDiv.appendChild(div);
                });
            } else {
                resultDiv.textContent = data.error;
            }
        }
    </script>
</head>
<body>
    <h1>Tractor Attachment Selector</h1>
    <label for="task">Enter the task you plan to perform:</label>
    <input type="text" id="task" placeholder="e.g., plowing, mowing">
    <button onclick="fetchAttachments()">Get Attachments</button>
    <div id="result"></div>
</body>
</html>
```

**Sample Data (attachments_data.json)**

```json
[
    {
        "name": "Plow",
        "tasks": ["plowing", "tilling"]
    },
    {
        "name": "Mower",
        "tasks": ["mowing", "cutting"]
    },
    {
        "name": "Loader",
        "tasks": ["loading", "lifting"]
    }
]
```

This code provides a simple web application that allows users to input a task and receive a list of suitable tractor attachments based on SCOUT's technical documentation. The application is built using Flask and includes error handling, input validation, and a basic HTML interface.
