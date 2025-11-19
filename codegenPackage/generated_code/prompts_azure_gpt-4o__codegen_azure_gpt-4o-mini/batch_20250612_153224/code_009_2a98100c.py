"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Provide code to design a dashboard for tracking energy production and savings for residential, business, and agricultural solar systems, inspired by Nexe Energetic's offerings.
Generated: DETERMINISTIC_2a98100c53a1eab3
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`.": {
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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the EnergyProduction model
class EnergyProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    system_type = db.Column(db.String(50), nullable=False)  # 'Residential', 'Business', 'Agricultural'
    production_amount = db.Column(db.Float, nullable=False)  # Amount of energy produced in kWh
    savings_amount = db.Column(db.Float, nullable=False)  # Amount of savings in currency
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EnergyProduction {self.system_type} - {self.production_amount} kWh>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the dashboard
@app.route('/')
def dashboard():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

# Route to get energy production data
@app.route('/api/energy_data', methods=['GET'])
def get_energy_data():
    """Fetch energy production and savings data from the database."""
    try:
        data = EnergyProduction.query.all()
        results = [
            {
                'system_type': entry.system_type,
                'production_amount': entry.production_amount,
                'savings_amount': entry.savings_amount,
                'timestamp': entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
            for entry in data
        ]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add new energy production data
@app.route('/api/energy_data', methods=['POST'])
def add_energy_data():
    """Add new energy production and savings data to the database."""
    try:
        data = request.json
        new_entry = EnergyProduction(
            system_type=data['system_type'],
            production_amount=data['production_amount'],
            savings_amount=data['savings_amount']
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Data added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (dashboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Production Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Energy Production and Savings Dashboard</h1>
        <div id="energy-data" class="mt-4"></div>
        <form id="energy-form" class="mt-4">
            <h3>Add Energy Data</h3>
            <div class="form-group">
                <label for="system_type">System Type</label>
                <input type="text" class="form-control" id="system_type" required>
            </div>
            <div class="form-group">
                <label for="production_amount">Production Amount (kWh)</label>
                <input type="number" class="form-control" id="production_amount" required>
            </div>
            <div class="form-group">
                <label for="savings_amount">Savings Amount</label>
                <input type="number" class="form-control" id="savings_amount" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Data</button>
        </form>
    </div>

    <script>
        // Fetch and display energy data
        async function fetchEnergyData() {
            const response = await fetch('/api/energy_data');
            const data = await response.json();
            const energyDataDiv = document.getElementById('energy-data');
            energyDataDiv.innerHTML = '<h3>Energy Data</h3><ul>' + 
                data.map(entry => `<li>${entry.system_type}: ${entry.production_amount} kWh, Savings: ${entry.savings_amount}</li>`).join('') + 
                '</ul>';
        }

        // Handle form submission
        document.getElementById('energy-form').addEventListener('submit', async (event) => {
            event.preventDefault();
            const systemType = document.getElementById('system_type').value;
            const productionAmount = document.getElementById('production_amount').value;
            const savingsAmount = document.getElementById('savings_amount').value;

            const response = await fetch('/api/energy_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    system_type: systemType,
                    production_amount: parseFloat(productionAmount),
                    savings_amount: parseFloat(savingsAmount)
                })
            });

            if (response.ok) {
                alert('Data added successfully!');
                fetchEnergyData(); // Refresh the data
            } else {
                const error = await response.json();
                alert('Error: ' + error.error);
            }
        });

        // Initial fetch of energy data
        fetchEnergyData();
    </script>
</body>
</html>
```

### Instructions
1. Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
2. Save the Python code in a file named `app.py`.
3. Save the HTML code in a folder named `templates` as `dashboard.html`.
4. Run the application using `python app.py`.
5. Access the dashboard at `http://127.0.0.1:5000/`.
