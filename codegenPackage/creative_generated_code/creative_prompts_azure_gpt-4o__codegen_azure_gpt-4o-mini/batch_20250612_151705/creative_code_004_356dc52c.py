"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dudemine.com
Prompt: Suggest methods or frameworks to build a web-based interface for a Minecraft server problem diagnoser, similar to the one mentioned on dudemine.com.
Generated: DETERMINISTIC_356dc52c852cd665
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import subprocess
import os

# Initialize the Flask application
app = Flask(__name__)

# Define a function to check server status
def check_server_status():
    try:
        # Replace with the command to check your Minecraft server's status
        result = subprocess.run(['screen', '-list'], capture_output=True, text=True)
        return "Minecraft server is running" in result.stdout
    except Exception as e:
        return str(e)

# Define a function to get server logs
def get_server_logs(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ["Log file not found."]
    except Exception as e:
        return [str(e)]

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to check server status
@app.route('/status', methods=['GET'])
def status():
    server_status = check_server_status()
    return jsonify({'status': server_status})

# Define a route to get server logs
@app.route('/logs', methods=['GET'])
def logs():
    log_file_path = request.args.get('log_file', 'server.log')  # Default log file
    logs = get_server_logs(log_file_path)
    return jsonify({'logs': logs})

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An unexpected error occurred."
    }
    return jsonify(response), 500

# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minecraft Server Diagnoser</title>
</head>
<body>
    <h1>Minecraft Server Diagnoser</h1>
    <button onclick="checkStatus()">Check Server Status</button>
    <div id="status"></div>
    
    <h2>View Server Logs</h2>
    <input type="text" id="logFile" placeholder="Enter log file name" value="server.log">
    <button onclick="viewLogs()">Get Logs</button>
    <div id="logs"></div>

    <script>
        async function checkStatus() {
            const response = await fetch('/status');
            const data = await response.json();
            document.getElementById('status').innerText = data.status;
        }

        async function viewLogs() {
            const logFile = document.getElementById('logFile').value;
            const response = await fetch(`/logs?log_file=${logFile}`);
            const data = await response.json();
            document.getElementById('logs').innerHTML = data.logs.join('<br>');
        }
    </script>
</body>
</html>
```

### Note:
Make sure to install Flask using pip if you haven't already:
```bash
pip install Flask
```

Also, ensure your server environment has the necessary permissions and configurations to run this code and that any referenced files (like server logs) exist in the expected locations.
