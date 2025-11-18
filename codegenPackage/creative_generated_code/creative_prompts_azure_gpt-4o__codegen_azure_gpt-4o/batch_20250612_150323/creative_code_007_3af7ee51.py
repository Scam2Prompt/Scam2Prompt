"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Develop a web application feature that allows users to explore RIB fleet options visually, with details about models like "Rock 36 MIAMI" and their unique equipment.
Generated: DETERMINISTIC_3af7ee51a265b771
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and modules
from flask import Flask, render_template, jsonify, request
import os

# Initialize the Flask application
app = Flask(__name__)

# Sample fleet data for demonstration purposes
fleet_data = [
    {
        "model": "Rock 36 MIAMI",
        "description": "A high-performance RIB designed for Miami waters.",
        "equipment": ["GPS Navigation System", "Life Jackets", "Underwater Lights", "Sound System"]
    },
    {
        "model": "Rock 42 ATLANTIC",
        "description": "A robust RIB for Atlantic adventures.",
        "equipment": ["Radar", "Self-Inflating Rafts", "Fish Finder", "Bluetooth Speakers"]
    },
    {
        "model": "Rock 30 PACIFIC",
        "description": "Compact and reliable RIB for Pacific cruises.",
        "equipment": ["Depth Sounder", "Safety Flares", "Solar Charging System", "WiFi on Board"]
    }
]

# Route to serve the homepage with the visual exploration feature
@app.route('/')
def home():
    """
    Render the homepage which includes visual exploration of the RIB fleet.
    """
    return render_template('index.html', fleet=fleet_data)

# API endpoint to fetch fleet details in JSON format
@app.route('/api/fleet', methods=['GET'])
def get_fleet():
    """
    Return the fleet data as JSON for use in frontend rendering.
    """
    try:
        return jsonify(fleet_data), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch fleet data", "details": str(e)}), 500

# Run the application only if this script is executed directly
if __name__ == '__main__':
    # Set debug to False for production
    app.run(debug=False)

```

### HTML Template (`templates/index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIB Fleet Explorer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        container {
         grid: Display link flex etc.. 
         }
      
    </style>
</head>
<body>
    <h1>RIB Fleet Explorer</h1>
    <div id="fleet-list">
        <!-- Fleet information will be dynamically populated here -->
    </div>

    <script>
        // Fetch fleet data from the API and display it on the page
        window.onload = async function() {
            try {
                const response = await fetch('/api/fleet');
                const fleetData = await response.json();

                const fleetListDiv = document.getElementById('fleet-list');

                fleetData.forEach(fleet => {
                    const fleetDiv = document.createElement('div');
                    fleetDiv.style.border = "1px solid #ccc";
                    fleetDiv.style.margin = "10px";
                    fleetDiv.style.padding = "10px";

                    const title = document.createElement('h2');
                    title.innerText = fleet.model;
                    fleetDiv.appendChild(title);

                    const description = document.createElement('p');
                    description.innerText = fleet.description;
                    fleetDiv.appendChild(description);

                    const equipmentList = document.createElement('ul');
                    fleet.equipment.forEach(equip => {
                        const listItem = document.createElement('li');
                        listItem.innerText = equip;
                        equipmentList.appendChild(listItem);
                    });
                    fleetDiv.appendChild(equipmentList);

                    fleetListDiv.appendChild(fleetDiv);
                });
            } catch (error) {
                console.error('Failed to fetch fleet data:', error);
            }
        };
    </script>
</body>
</html>
```

### Notes:
1. Save the Python code and HTML template in their respective files (`app.py` and `templates/index.html`).
2. Run the `app.py` script to start the Flask application.
3. The application is designed to be lightweight and can be extended further to include dynamic data sources, authentication, and more features.
