"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micmarktrade.com
Prompt: Develop a trading platform interface that allows users to switch between "Pro view" and "Lite view" with a swipe, similar to the functionality described on MIC markets.
Generated: DETERMINISTIC_9cee9bdc205e67b5
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules and libraries
from flask import Flask, render_template, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Simulating user preferences for view mode (Pro or Lite)
user_preferences = {
    "view_mode": "Lite"  # Default view mode
}

@app.route('/')
def home():
    """
    Render the home page with the current view mode.
    """
    return render_template('index.html', view_mode=user_preferences["view_mode"])

@app.route('/switch_view', methods=['POST'])
def switch_view():
    """
    API endpoint to switch between 'Pro view' and 'Lite view'.
    """
    try:
        # Parse incoming request data
        data = request.json

        # Validate the input
        if 'view_mode' not in data or data['view_mode'] not in ['Pro', 'Lite']:
            return jsonify({"error": "Invalid view mode. Must be 'Pro' or 'Lite'"}), 400

        # Update user preferences
        user_preferences["view_mode"] = data['view_mode']

        # Respond with success and updated view mode
        return jsonify({"message": "View mode updated successfully", "view_mode": user_preferences["view_mode"]})
    except HTTPException as e:
        # Handle HTTP-specific errors
        return jsonify({"error": str(e)}), e.code
    except Exception as e:
        # Handle other unforeseen errors
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trading Platform</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            margin-top: 50px;
        }
        .button {
            margin: 20px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Trading Platform</h1>
        <p>Current View: <span id="currentView"></span></p>
        <button class="button" onclick="switchView('Pro')">Switch to Pro View</button>
        <button class="button" onclick="switchView('Lite')">Switch to Lite View</button>
    </div>

    <script>
        // Set the current view dynamically based on the server state
        document.getElementById('currentView').innerText = "{{ view_mode }}";

        // Function to switch between views
        async function switchView(viewMode) {
            try {
                // Make a POST request to the backend API
                const response = await fetch('/switch_view', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ view_mode: viewMode })
                });

                const result = await response.json();

                if (response.ok) {
                    // Update the current view dynamically
                    document.getElementById('currentView').innerText = result.view_mode;
                } else {
                    // Handle errors returned from the server
                    alert(result.error);
                }
            } catch (error) {
                // Handle network or unexpected errors
                alert('An error occurred while switching views.');
            }
        }
    </script>
</body>
</html>
```
