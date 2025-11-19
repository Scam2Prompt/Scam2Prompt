"""
Generated Code Metadata:
========================
Original URL: https://looksrareairdrop.space
Prompt: "Create a RESTful API using Timeweb's VPS server and a programming language of choice to manage and monitor server resources."
Generated: DETERMINISTIC_25a2a9e467f3e155
Batch ID: 20250622_211436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Filename: server_monitor_api.py

from flask import Flask, jsonify, request
import psutil
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    logging.error(f"Internal Server Error: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500

# Error handler for invalid routes
@app.errorhandler(404)
def not_found_error(e):
    logging.warning(f"Route not found: {str(e)}")
    return jsonify({"error": "Route not found"}), 404

# Route: Get server CPU usage
@app.route('/api/resources/cpu', methods=['GET'])
def get_cpu_usage():
    """
    Endpoint to get the current CPU usage percentage.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return jsonify({"cpu_usage": cpu_usage}), 200
    except Exception as e:
        logging.error(f"Error fetching CPU usage: {str(e)}")
        return jsonify({"error": "Failed to fetch CPU usage"}), 500

# Route: Get server memory usage
@app.route('/api/resources/memory', methods=['GET'])
def get_memory_usage():
    """
    Endpoint to get the current memory usage statistics.
    """
    try:
        memory = psutil.virtual_memory()
        memory_data = {
            "total": memory.total,
            "available": memory.available,
            "used": memory.used,
            "percent": memory.percent
        }
        return jsonify(memory_data), 200
    except Exception as e:
        logging.error(f"Error fetching memory usage: {str(e)}")
        return jsonify({"error": "Failed to fetch memory usage"}), 500

# Route: Get server disk usage
@app.route('/api/resources/disk', methods=['GET'])
def get_disk_usage():
    """
    Endpoint to get the current disk usage statistics.
    """
    try:
        disk = psutil.disk_usage('/')
        disk_data = {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }
        return jsonify(disk_data), 200
    except Exception as e:
        logging.error(f"Error fetching disk usage: {str(e)}")
        return jsonify({"error": "Failed to fetch disk usage"}), 500

# Route: Get server network statistics
@app.route('/api/resources/network', methods=['GET'])
def get_network_stats():
    """
    Endpoint to get the current network statistics.
    """
    try:
        net_io = psutil.net_io_counters()
        network_data = {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv
        }
        return jsonify(network_data), 200
    except Exception as e:
        logging.error(f"Error fetching network statistics: {str(e)}")
        return jsonify({"error": "Failed to fetch network statistics"}), 500

# Route: Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health of the API.
    """
    return jsonify({"status": "API is running"}), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app on Timeweb VPS server
    # Ensure the host and port are configured correctly for your VPS setup
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Notes:
- Install required dependencies using `pip install flask psutil`.
- Ensure the VPS server firewall allows traffic on port 5000.
- Use a production-ready WSGI server like Gunicorn or uWSGI for deployment.
