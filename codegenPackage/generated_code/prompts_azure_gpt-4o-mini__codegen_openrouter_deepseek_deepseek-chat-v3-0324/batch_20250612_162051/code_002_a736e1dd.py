"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Generate a code snippet for a web application that allows users to input their energy consumption data and receive recommendations for improving energy efficiency, inspired by Digar Green's consulting services.
Generated: DETERMINISTIC_a736e1ddd17f3ab2
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
import os
from typing import Dict, List, Optional

# Initialize Flask application
app = Flask(__name__)

# File to store user data (in a real app, use a proper database)
DATA_FILE = "user_data.json"

# Energy efficiency recommendations based on consumption ranges
EFFICIENCY_RECOMMENDATIONS = {
    "low": [
        "Your energy consumption is already efficient!",
        "Consider maintaining your current habits.",
        "You might explore renewable energy options for further savings."
    ],
    "medium": [
        "Upgrade to energy-efficient appliances (LED bulbs, Energy Star rated devices).",
        "Implement smart thermostats to optimize heating/cooling.",
        "Consider solar panel installation for long-term savings."
    ],
    "high": [
        "Conduct a professional energy audit to identify major inefficiencies.",
        "Replace outdated HVAC systems with modern, efficient models.",
        "Improve home insulation to reduce heating/cooling losses.",
        "Consider switching to renewable energy sources immediately."
    ]
}

def load_user_data() -> Dict:
    """Load user data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_user_data(data: Dict) -> None:
    """Save user data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def calculate_efficiency_level(kwh: float) -> str:
    """Determine efficiency level based on kWh consumption."""
    if kwh < 500:
        return "low"
    elif 500 <= kwh < 1000:
        return "medium"
    else:
        return "high"

@app.route("/")
def home():
    """Render the home page with the energy input form."""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_consumption():
    """Handle form submission and provide recommendations."""
    try:
        # Get form data
        user_id = request.form.get("user_id")
        monthly_kwh = float(request.form.get("monthly_kwh"))
        building_type = request.form.get("building_type", "residential")

        # Validate input
        if not user_id or monthly_kwh <= 0:
            return jsonify({"error": "Invalid input data"}), 400

        # Calculate efficiency level
        efficiency_level = calculate_efficiency_level(monthly_kwh)
        recommendations = EFFICIENCY_RECOMMENDATIONS.get(efficiency_level, [])

        # Prepare response data
        response_data = {
            "user_id": user_id,
            "monthly_kwh": monthly_kwh,
            "building_type": building_type,
            "efficiency_level": efficiency_level,
            "recommendations": recommendations
        }

        # Save user data
        user_data = load_user_data()
        user_data[user_id] = response_data
        save_user_data(user_data)

        return jsonify(response_data)

    except ValueError:
        return jsonify({"error": "Invalid numerical input"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/user/<user_id>", methods=["GET"])
def get_user_data(user_id: str):
    """Retrieve stored user data."""
    try:
        user_data = load_user_data()
        if user_id not in user_data:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user_data[user_id])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Efficiency Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2e8b57;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #2e8b57;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #3cb371;
        }
        #results {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            display: none;
        }
        .recommendation {
            margin-bottom: 10px;
            padding-left: 15px;
            border-left: 3px solid #2e8b57;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Energy Efficiency Calculator</h1>
        <form id="energyForm">
            <div class="form-group">
                <label for="user_id">User ID:</label>
                <input type="text" id="user_id" name="user_id" required>
            </div>
            <div class="form-group">
                <label for="monthly_kwh">Monthly Energy Consumption (kWh):</label>
                <input type="number" id="monthly_kwh" name="monthly_kwh" min="1" required>
            </div>
            <div class="form-group">
                <label for="building_type">Building Type:</label>
                <select id="building_type" name="building_type">
                    <option value="residential">Residential</option>
                    <option value="commercial">Commercial</option>
                    <option value="industrial">Industrial</option>
                </select>
            </div>
            <button type="submit">Get Recommendations</button>
        </form>
        <div id="results">
            <h2>Your Energy Efficiency Report</h2>
            <p><strong>Efficiency Level:</strong> <span id="efficiencyLevel"></span></p>
            <h3>Recommendations:</h3>
            <div id="recommendations"></div>
        </div>
    </div>

    <script>
        document.getElementById('energyForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const response = await fetch('/submit', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (response.ok) {
                document.getElementById('efficiencyLevel').textContent = data.efficiency_level;
                const recommendationsDiv = document.getElementById('recommendations');
                recommendationsDiv.innerHTML = '';
                
                data.recommendations.forEach(rec => {
                    const recElement = document.createElement('div');
                    recElement.className = 'recommendation';
                    recElement.textContent = rec;
                    recommendationsDiv.appendChild(recElement);
                });
                
                document.getElementById('results').style.display = 'block';
            } else {
                alert('Error: ' + data.error);
            }
        });
    </script>
</body>
</html>
```
