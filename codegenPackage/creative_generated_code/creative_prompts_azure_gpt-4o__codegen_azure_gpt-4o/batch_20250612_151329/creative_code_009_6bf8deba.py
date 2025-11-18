"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alixa.tech
Prompt: Generate code to display a real-time dashboard summarizing the user's bond activity on Alixa, including active bonds, matured bonds, total value bonded, and pending payouts.
Generated: DETERMINISTIC_6bf8deba37a3230a
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import threading
import time
import random

app = Flask(__name__)

# Simulated data for bond activity (would typically come from a database or API in production)
bond_data = {
    "active_bonds": 10,
    "matured_bonds": 25,
    "total_value_bonded": 500000,  # in USD
    "pending_payouts": 12000  # in USD
}

# Lock for synchronizing access to the bond_data dictionary
data_lock = threading.Lock()

def update_bond_data():
    """
    Simulate real-time updates to bond data.
    This would typically involve pulling data from an external system or service.
    """
    while True:
        with data_lock:
            # Randomly adjust bond data to simulate activity (for demo purposes)
            bond_data["active_bonds"] = max(0, bond_data["active_bonds"] + random.randint(-1, 1))
            bond_data["matured_bonds"] += random.randint(0, 1)
            bond_data["total_value_bonded"] += random.randint(-1000, 1000)
            bond_data["pending_payouts"] += random.randint(-500, 500)
        time.sleep(5)  # Update every 5 seconds (adjust as needed)

@app.route('/')
def dashboard():
    """
    Render the dashboard page.
    """
    return render_template('dashboard.html')

@app.route('/data')
def get_bond_data():
    """
    Endpoint to fetch bond data as JSON for real-time updates on the dashboard.
    """
    with data_lock:
        return jsonify(bond_data)

if __name__ == '__main__':
    # Start the background thread to simulate real-time updates
    updater_thread = threading.Thread(target=update_bond_data, daemon=True)
    updater_thread.start()

    # Run the Flask web server
    app.run(debug=True, threaded=True)
```

**HTML Template (`templates/dashboard.html`)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bond Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        .dashboard {
            margin-top: 20px;
        }
        .dashboard div {
            margin-bottom: 10px;
        }
    </style>
    <script>
        async function fetchBondData() {
            try {
                const response = await fetch('/data');
                const data = await response.json();
                document.getElementById('active_bonds').innerText = data.active_bonds;
                document.getElementById('matured_bonds').innerText = data.matured_bonds;
                document.getElementById('total_value_bonded').innerText = data.total_value_bonded.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
                document.getElementById('pending_payouts').innerText = data.pending_payouts.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
            } catch (error) {
                console.error('Error fetching bond data:', error);
            }
        }

        // Refresh data every 5 seconds
        setInterval(fetchBondData, 5000);
        window.onload = fetchBondData;
    </script>
</head>
<body>
    <h1>Real-Time Bond Dashboard</h1>
    <div class="dashboard">
        <div>Active Bonds: <span id="active_bonds">Loading...</span></div>
        <div>Matured Bonds: <span id="matured_bonds">Loading...</span></div>
        <div>Total Value Bonded: <span id="total_value_bonded">Loading...</span></div>
        <div>Pending Payouts: <span id="pending_payouts">Loading...</span></div>
    </div>
</body>
</html>
```
