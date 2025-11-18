"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Generate code to create a dashboard for tracking patient health metrics in real-time, using the concepts of Hooshmand Teb's device for patient monitoring.
Generated: DETERMINISTIC_3e412d8447478d97
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import Flask
from flask import Flask, jsonify, request, render_template
import random
import time
import threading

app = Flask(__name__)

# Sample data structure for storing patient health metrics
class PatientHealthMetric:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.heart_rate = 0
        self.blood_pressure = (0, 0)
        self.temperature = 0.0

    def update_metrics(self):
        # Simulate real-time data updates
        self.heart_rate = random.randint(60, 100)  # Simulate heart rate
        self.blood_pressure = (random.randint(90, 120), random.randint(60, 80))  # Simulate blood pressure
        self.temperature = round(random.uniform(36.0, 38.5), 1)  # Simulate temperature

# Global dictionary to store patient metrics
patients = {}

def generate_patient_data(patient_id):
    """Thread function to continuously update patient metrics."""
    while True:
        if patient_id not in patients:
            patients[patient_id] = PatientHealthMetric(patient_id)
        patients[patient_id].update_metrics()
        time.sleep(2)  # Update every 2 seconds

@app.route('/')
def index():
    """Render the dashboard for patient health metrics."""
    return render_template('dashboard.html')

@app.route('/api/patient/<patient_id>', methods=['GET'])
def get_patient_metrics(patient_id):
    """API endpoint to retrieve the health metrics of a specific patient."""
    if patient_id in patients:
        metrics = patients[patient_id]
        return jsonify({
            'patient_id': metrics.patient_id,
            'heart_rate': metrics.heart_rate,
            'blood_pressure': metrics.blood_pressure,
            'temperature': metrics.temperature
        })
    else:
        return jsonify({'error': 'Patient not found'}), 404

if __name__ == '__main__':
    # Start a background thread for simulated patient data generation
    patient_thread = threading.Thread(target=generate_patient_data, args=('patient_1',))
    patient_thread.daemon = True  # Allow thread to exit when the main program exits
    patient_thread.start()

    # Run the Flask app
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

**dashboard.html (Place this file in the 'templates' directory)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Health Dashboard</title>
    <script>
        async function fetchMetrics() {
            const response = await fetch('/api/patient/patient_1');
            if (response.ok) {
                const data = await response.json();
                document.getElementById('heart-rate').innerText = data.heart_rate;
                document.getElementById('blood-pressure').innerText = data.blood_pressure.join('/');
                document.getElementById('temperature').innerText = data.temperature;
            } else {
                console.error('Error fetching patient metrics:', response.statusText);
            }
        }

        // Fetch metrics every 2 seconds
        setInterval(fetchMetrics, 2000);
    </script>
</head>
<body>
    <h1>Patient Health Dashboard</h1>
    <div>
        <h2>Patient ID: patient_1</h2>
        <p>Heart Rate: <span id="heart-rate">--</span> bpm</p>
        <p>Blood Pressure: <span id="blood-pressure">--</span> mmHg</p>
        <p>Temperature: <span id="temperature">--</span> °C</p>
    </div>
</body>
</html>
```
