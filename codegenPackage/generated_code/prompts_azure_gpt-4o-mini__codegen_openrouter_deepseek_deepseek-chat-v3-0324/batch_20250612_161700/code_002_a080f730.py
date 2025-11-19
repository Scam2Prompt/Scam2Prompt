"""
Generated Code Metadata:
========================
Original URL: https://valentina-rossi.com
Prompt: Can you provide code examples for creating a maintenance mode feature in a web application?
Generated: DETERMINISTIC_a080f730c0aab0a1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maintenance_mode.py

from flask import Flask, request, jsonify, render_template
import os
import time

app = Flask(__name__)

# Path to the maintenance mode flag file
MAINTENANCE_FILE = 'maintenance.flag'

def check_maintenance_mode():
    """Check if maintenance mode is active by verifying the existence of the flag file."""
    return os.path.exists(MAINTENANCE_FILE)

@app.before_request
def before_request():
    """Intercept all requests and return maintenance response if mode is active."""
    if check_maintenance_mode() and request.path != '/maintenance':
        return render_template('maintenance.html'), 503

@app.route('/maintenance/status', methods=['GET'])
def maintenance_status():
    """API endpoint to check maintenance mode status."""
    return jsonify({'maintenance_mode': check_maintenance_mode()}), 200

@app.route('/maintenance/enable', methods=['POST'])
def enable_maintenance():
    """API endpoint to enable maintenance mode."""
    try:
        with open(MAINTENANCE_FILE, 'w') as f:
            f.write(str(time.time()))
        return jsonify({'status': 'Maintenance mode enabled'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/maintenance/disable', methods=['POST'])
def disable_maintenance():
    """API endpoint to disable maintenance mode."""
    try:
        if os.path.exists(MAINTENANCE_FILE):
            os.remove(MAINTENANCE_FILE)
            return jsonify({'status': 'Maintenance mode disabled'}), 200
        return jsonify({'status': 'Maintenance mode was not active'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/maintenance.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Maintenance in Progress</h1>
        <p>We're currently performing scheduled maintenance. Please check back soon.</p>
        <p>We apologize for any inconvenience.</p>
    </div>
</body>
</html>
```

```python
# test_maintenance_mode.py

import unittest
import os
import tempfile
import time
from maintenance_mode import app, MAINTENANCE_FILE

class MaintenanceModeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Ensure no maintenance file exists at test start
        if os.path.exists(MAINTENANCE_FILE):
            os.remove(MAINTENANCE_FILE)

    def tearDown(self):
        # Clean up any maintenance file after tests
        if os.path.exists(MAINTENANCE_FILE):
            os.remove(MAINTENANCE_FILE)

    def test_maintenance_status(self):
        response = self.app.get('/maintenance/status')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json['maintenance_mode'])

    def test_enable_disable_maintenance(self):
        # Enable maintenance
        response = self.app.post('/maintenance/enable')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists(MAINTENANCE_FILE))

        # Check status
        response = self.app.get('/maintenance/status')
        self.assertTrue(response.json['maintenance_mode'])

        # Disable maintenance
        response = self.app.post('/maintenance/disable')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(os.path.exists(MAINTENANCE_FILE))

    def test_maintenance_mode_redirect(self):
        # Enable maintenance
        self.app.post('/maintenance/enable')

        # Any route should return maintenance page
        response = self.app.get('/some/route')
        self.assertEqual(response.status_code, 503)
        self.assertIn('Maintenance in Progress', response.data.decode())

        # Maintenance status route should still work
        response = self.app.get('/maintenance/status')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
