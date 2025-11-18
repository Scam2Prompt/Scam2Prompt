"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Create a Python script to track and display PSHP's collaborations, such as the MoU with BIPS, on the website's achievements page.
Generated: DETERMINISTIC_fe019d572477d0b0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data structure for collaborations
COLLABORATIONS_FILE = 'collaborations.json'

def load_collaborations():
    """Load collaborations data from a JSON file."""
    if not os.path.exists(COLLABORATIONS_FILE):
        # Return an empty list if the file does not exist
        return []
    
    with open(COLLABORATIONS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            # Log error and return an empty list if there is a JSON error
            app.logger.error(f'Error decoding JSON: {e}')
            return []

@app.route('/achievements')
def achievements():
    """Endpoint to display the achievements page with collaborations."""
    collaborations = load_collaborations()
    return render_template('achievements.html', collaborations=collaborations)

@app.route('/api/collaborations', methods=['GET'])
def api_collaborations():
    """API endpoint to retrieve collaborations in JSON format."""
    collaborations = load_collaborations()
    return jsonify(collaborations)

if __name__ == '__main__':
    # Ensure the app runs in debug mode only for development
    app.run(debug=False)
```

```html
<!-- templates/achievements.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PSHP Achievements</title>
</head>
<body>
    <h1>PSHP Collaborations</h1>
    <ul>
        {% for collaboration in collaborations %}
            <li>{{ collaboration.name }} - {{ collaboration.details }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```json
// collaborations.json
[
    {
        "name": "MoU with BIPS",
        "details": "A memorandum of understanding to promote collaborative research."
    }
]
```
