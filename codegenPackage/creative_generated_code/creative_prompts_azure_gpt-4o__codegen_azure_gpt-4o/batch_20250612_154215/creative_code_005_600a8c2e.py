"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Suggest an API for monitoring uptime and performance of web hosting services in Chile, specifically for Linux and Windows servers.
Generated: DETERMINISTIC_600a8c2ea9785b45
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# uptime_monitor_api.py

from flask import Flask, request, jsonify
import subprocess
import platform

app = Flask(__name__)

# Helper function to perform ping tests
def ping_host(hostname):
    """
    Function to ping a host to check its availability.
    Returns True if the host is reachable, otherwise False.
    """
    try:
        # Determine the OS and construct the appropriate ping command
        ping_command = (
            ["ping", "-c", "2", hostname] if platform.system() != "Windows" 
            else ["ping", "-n", "2", hostname]
        )
        subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Helper function to check server performance
def check_server_performance(server_ip):
    """
    Placeholder for detailed server performance checks.
    For simplicity, this function returns a mock performance result.
    """
    # In production, integrate tools like `top`, `vmstat`, or library APIs for real metrics
    return {
        "CPU_Usage": "15%",
        "Memory_Usage": "40%",
        "Disk_Usage": "30%"
    }

@app.route('/api/uptime', methods=['POST'])
def check_uptime():
    """
    API Endpoint: /api/uptime
    Method: POST
    Description: Check the uptime of a specified server via hostname or IP address.
    Request Body:
        {
            "hostname": "example.com"
        }
    Response:
        {
            "hostname": "example.com",
            "status": "UP"
        }
    """
    try:
        data = request.get_json()
        hostname = data.get("hostname")

        # Validate input
        if not hostname:
            return jsonify({"error": "Hostname is required"}), 400

        # Check server uptime
        is_up = ping_host(hostname)
        status = "UP" if is_up else "DOWN"

        return jsonify({"hostname": hostname, "status": status}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/performance', methods=['POST'])
def check_performance():
    """
    API Endpoint: /api/performance
    Method: POST
    Description: Check the performance metrics of a specified server.
    Request Body:
        {
            "server_ip": "192.168.1.1"
        }
    Response:
        {
            "server_ip": "192.168.1.1",
            "performance": {
                "CPU_Usage": "15%",
                "Memory_Usage": "40%",
                "Disk_Usage": "30%"
            }
        }
    """
    try:
        data = request.get_json()
        server_ip = data.get("server_ip")

        # Validate input
        if not server_ip:
            return jsonify({"error": "Server IP is required"}), 400

        # Fetch performance metrics
        performance = check_server_performance(server_ip)

        return jsonify({"server_ip": server_ip, "performance": performance}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```
