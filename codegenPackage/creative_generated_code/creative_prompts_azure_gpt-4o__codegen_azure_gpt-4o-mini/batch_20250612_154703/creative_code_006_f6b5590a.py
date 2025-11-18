"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Generate code for a dashboard that displays the status of activated hosting packages in real-time.
Generated: DETERMINISTIC_f6b5590a2a3251c0
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import random
import time
from threading import Thread, Event

app = Flask(__name__)

# Sample data structure to hold hosting package status
hosting_packages = {
    "package1": {"status": "active"},
    "package2": {"status": "inactive"},
    "package3": {"status": "active"},
}

# Event to control the update loop
stop_event = Event()

def update_package_status():
    """Simulates real-time updates to hosting package statuses."""
    while not stop_event.is_set():
        # Randomly change the status of packages to simulate real-time updates
        for package in hosting_packages.keys():
            current_status = hosting_packages[package]["status"]
            new_status = "active" if current_status == "inactive" else "inactive"
            hosting_packages[package]["status"] = new_status
        
        # Sleep for a specified interval before the next update
        time.sleep(5)

@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/api/status', methods=['GET'])
def get_status():
    """API endpoint to retrieve the current status of hosting packages.
    
    Returns:
        JSON response containing the status of hosting packages.
    """
    return jsonify(hosting_packages)

if __name__ == '__main__':
    # Start the background thread for updating package statuses
    update_thread = Thread(target=update_package_status)
    update_thread.start()
    
    try:
        # Run the Flask app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting server: {e}")
    finally:
        # Signal the thread to stop and wait for it to finish
        stop_event.set()
        update_thread.join()
```

### dashboard.html (Create this file in the templates directory)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hosting Packages Dashboard</title>
    <script>
        function fetchStatus() {
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {
                    const statusContainer = document.getElementById('status');
                    statusContainer.innerHTML = '';
                    for (const [packageName, packageInfo] of Object.entries(data)) {
                        const packageElement = document.createElement('div');
                        packageElement.innerText = `${packageName}: ${packageInfo.status}`;
                        statusContainer.appendChild(packageElement);
                    }
                })
                .catch(error => console.error('Error fetching status:', error));
        }

        // Fetch status every 5 seconds
        setInterval(fetchStatus, 5000);
        window.onload = fetchStatus;
    </script>
</head>
<body>
    <h1>Hosting Packages Dashboard</h1>
    <div id="status">
        <!-- Status will be populated here -->
    </div>
</body>
</html>
```
