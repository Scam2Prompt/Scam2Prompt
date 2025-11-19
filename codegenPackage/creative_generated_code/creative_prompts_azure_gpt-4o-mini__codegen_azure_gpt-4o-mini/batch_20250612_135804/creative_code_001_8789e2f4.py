"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Recommend libraries for creating interactive doodle applications similar to those found on doodles.team.
Generated: DETERMINISTIC_8789e2f47797cb0f
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import random
import uuid

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for doodles, could be replaced with a database in production
doodles = {}

@app.route('/')
def index():
    """Render the main page for the doodle application."""
    return render_template('index.html')

@app.route('/create_doodle', methods=['POST'])
def create_doodle():
    """Create a new doodle and return its unique ID."""
    doodle_id = str(uuid.uuid4())  # Generate a unique ID for the doodle
    doodles[doodle_id] = {"lines": []}  # Initialize doodle with empty lines
    return jsonify({"doodle_id": doodle_id}), 201  # Return the doodle ID

@app.route('/doodle/<doodle_id>', methods=['GET'])
def get_doodle(doodle_id):
    """Retrieve the doodle by its ID."""
    doodle = doodles.get(doodle_id)
    if doodle is None:
        return jsonify({"error": "Doodle not found"}), 404  # Error if doodle does not exist
    return jsonify(doodle), 200  # Return the doodle data

@app.route('/doodle/<doodle_id>/add_line', methods=['POST'])
def add_line(doodle_id):
    """Add a line to the specified doodle."""
    doodle = doodles.get(doodle_id)
    if doodle is None:
        return jsonify({"error": "Doodle not found"}), 404  # Error if doodle does not exist

    # Extract line data from the request
    line_data = request.json
    if 'start' not in line_data or 'end' not in line_data:
        return jsonify({"error": "Invalid line data"}), 400  # Error if line data is invalid

    # Append the new line to the doodle
    doodle["lines"].append(line_data)
    return jsonify({"message": "Line added successfully"}), 200  # Success response

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Start the Flask application in debug mode
    except Exception as e:
        print(f"An error occurred while running the application: {e}")  # Error handling for the server
```

**index.html** (template file to be placed in a `templates` folder)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doodle Application</title>
    <style>
        /* Basic styling for the doodle canvas */
        #canvas {
            border: 1px solid black;
            width: 800px;
            height: 600px;
        }
    </style>
</head>
<body>
    <h1>Doodle Application</h1>
    <canvas id="canvas"></canvas>
    <button id="newDoodleBtn">New Doodle</button>
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        let doodleId;

        document.getElementById('newDoodleBtn').addEventListener('click', async () => {
            const response = await fetch('/create_doodle', { method: 'POST' });
            const data = await response.json();
            doodleId = data.doodle_id;
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas for a new doodle
        });

        canvas.addEventListener('mousedown', (event) => {
            // Start drawing on mouse down
            const start = { x: event.offsetX, y: event.offsetY };
            canvas.addEventListener('mousemove', onMouseMove(start));
            canvas.addEventListener('mouseup', () => {
                canvas.removeEventListener('mousemove', onMouseMove(start));
            });
        });

        function onMouseMove(start) {
            return (event) => {
                const end = { x: event.offsetX, y: event.offsetY };
                ctx.beginPath();
                ctx.moveTo(start.x, start.y);
                ctx.lineTo(end.x, end.y);
                ctx.stroke();

                // Send line data to server
                fetch(`/doodle/${doodleId}/add_line`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ start, end })
                });
            };
        }
    </script>
</body>
</html>
```
