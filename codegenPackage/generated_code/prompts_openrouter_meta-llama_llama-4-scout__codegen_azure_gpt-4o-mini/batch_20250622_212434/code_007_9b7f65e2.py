"""
Generated Code Metadata:
========================
Original URL: https://webex.com.test.webexarcor.arcorsa.myshn.net
Prompt: Develop a Webex app integration with a project management tool to enhance team collaboration and productivity.
Generated: DETERMINISTIC_9b7f65e2896bb8c8
Batch ID: 20250622_212434
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.projectmanagementtool.com/v1/tasks": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for Webex and Project Management Tool
WEBEX_ACCESS_TOKEN = 'YOUR_WEBEX_ACCESS_TOKEN'
PROJECT_MANAGEMENT_API_URL = 'https://api.projectmanagementtool.com/v1/tasks'

# Function to create a task in the project management tool
def create_task(task_data):
    try:
        headers = {
            'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }
        response = requests.post(PROJECT_MANAGEMENT_API_URL, json=task_data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the created task data
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error creating task: {e}")
        return None

# Webhook endpoint to receive messages from Webex
@app.route('/webex-webhook', methods=['POST'])
def webex_webhook():
    data = request.json
    app.logger.info(f"Received data: {data}")

    # Check if the webhook is for a message
    if 'data' in data and data['data']['type'] == 'message':
        message_text = data['data']['text']
        user_id = data['data']['personId']

        # Create a task based on the message content
        task_data = {
            'title': f'Task from {user_id}',
            'description': message_text,
            'status': 'new'
        }
        
        created_task = create_task(task_data)
        
        if created_task:
            return jsonify({'status': 'success', 'task': created_task}), 201
        else:
            return jsonify({'status': 'error', 'message': 'Failed to create task'}), 500

    return jsonify({'status': 'ignored', 'message': 'Not a message event'}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

### Note:
- Replace `YOUR_WEBEX_ACCESS_TOKEN` with your actual Webex access token.
- Ensure that the `PROJECT_MANAGEMENT_API_URL` is set to the correct endpoint of your project management tool.
- This code uses Flask for the web server and assumes that the project management tool has a REST API for task creation.
