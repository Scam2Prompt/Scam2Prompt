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
# Import required libraries
from flask import Flask, render_template, request, jsonify
import json
import os

# Initialize Flask application
app = Flask(__name__)

# Load SCOUT's technical documentation data (mock data for demonstration)
def load_attachments_data():
    try:
        with open('attachments_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Attachments data file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in attachments data"}

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get compatible attachments based on tractor model and task
@app.route('/api/get_attachments', methods=['POST'])
def get_attachments():
    data = request.get_json()
    
    # Validate input
    if not data or 'tractor_model' not in data or 'task' not in data:
        return jsonify({"error": "Invalid input. Please provide tractor_model and task"}), 400
    
    tractor_model = data['tractor_model']
    task = data['task']
    
    attachments_data = load_attachments_data()
    
    if "error" in attachments_data:
        return jsonify(attachments_data), 500
    
    # Filter attachments based on tractor model and task
    compatible_attachments = []
    for attachment in attachments_data.get('attachments', []):
        if (tractor_model in attachment.get('compatible_tractors', []) and
            task in attachment.get('suitable_tasks', [])):
            compatible_attachments.append(attachment)
    
    if not compatible_attachments:
        return jsonify({"message": "No compatible attachments found for the given criteria"}), 404
    
    return jsonify({"attachments": compatible_attachments})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Create attachments data file if it doesn't exist
    if not os.path.exists('attachments_data.json'):
        sample_data = {
            "attachments": [
                {
                    "id": 1,
                    "name": "Standard Plow",
                    "compatible_tractors": ["SCOUT-100", "SCOUT-200"],
                    "suitable_tasks": ["plowing", "tilling"],
                    "description": "Heavy-duty plow for deep soil penetration"
                },
                {
                    "id": 2,
                    "name": "Rotary Mower",
                    "compatible_tractors": ["SCOUT-200", "SCOUT-300"],
                    "suitable_tasks": ["mowing", "brush clearing"],
                    "description": "High-capacity mower for large areas"
                }
            ]
        }
        with open('attachments_data.json', 'w') as file:
            json.dump(sample_data, file)
    
    # Run the application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCOUT Attachment Selector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        select, button {
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #results {
            margin-top: 20px;
        }
        .attachment {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>SCOUT Attachment Selector</h1>
    <p>Find the right attachments for your SCOUT tractor based on your planned tasks.</p>
    
    <div class="form-group">
        <label for="tractor_model">Select Your Tractor Model:</label>
        <select id="tractor_model">
            <option value="">-- Select Model --</option>
            <option value="SCOUT-100">SCOUT-100</option>
            <option value="SCOUT-200">SCOUT-200</option>
            <option value="SCOUT-300">SCOUT-300</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="task">Select Your Task:</label>
        <select id="task">
            <option value="">-- Select Task --</option>
            <option value="plowing">Plowing</option>
            <option value="tilling">Tilling</option>
            <option value="mowing">Mowing</option>
            <option value="brush clearing">Brush Clearing</option>
        </select>
    </div>
    
    <button id="find_attachments">Find Compatible Attachments</button>
    
    <div id="results"></div>
    
    <script>
        document.getElementById('find_attachments').addEventListener('click', function() {
            const tractorModel = document.getElementById('tractor_model').value;
            const task = document.getElementById('task').value;
            
            if (!tractorModel || !task) {
                document.getElementById('results').innerHTML = 
                    '<p class="error">Please select both tractor model and task</p>';
                return;
            }
            
            fetch('/api/get_attachments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    tractor_model: tractorModel,
                    task: task
                })
            })
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('results');
                
                if (data.error) {
                    resultsDiv.innerHTML = `<p class="error">${data.error}</p>`;
                } else if (data.message) {
                    resultsDiv.innerHTML = `<p>${data.message}</p>`;
                } else {
                    let html = '<h2>Compatible Attachments</h2>';
                    
                    if (data.attachments && data.attachments.length > 0) {
                        data.attachments.forEach(attachment => {
                            html += `
                                <div class="attachment">
                                    <h3>${attachment.name}</h3>
                                    <p><strong>Description:</strong> ${attachment.description}</p>
                                    <p><strong>Compatible with:</strong> ${attachment.compatible_tractors.join(', ')}</p>
                                    <p><strong>Suitable for:</strong> ${attachment.suitable_tasks.join(', ')}</p>
                                </div>
                            `;
                        });
                    } else {
                        html += '<p>No attachments found for your selection.</p>';
                    }
                    
                    resultsDiv.innerHTML = html;
                }
            })
            .catch(error => {
                document.getElementById('results').innerHTML = 
                    '<p class="error">An error occurred while fetching attachments</p>';
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
```
