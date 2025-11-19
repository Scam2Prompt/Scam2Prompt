"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: What libraries can I use to build a server monitoring tool that aligns with the features mentioned on SQUID.WTF?
Generated: DETERMINISTIC_f4ebbc30c47dcb16
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import psutil  # For system and process utilities
import time    # For handling time-related tasks
import logging  # For logging information and errors
from flask import Flask, jsonify  # For creating a web server

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to gather CPU usage statistics
def get_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1-second interval
        logging.info(f"CPU Usage: {cpu_usage}%")
        return cpu_usage
    except Exception as e:
        logging.error(f"Error fetching CPU usage: {e}")
        return None

# Function to gather memory usage statistics
def get_memory_usage():
    try:
        memory_info = psutil.virtual_memory()  # Get memory usage details
        memory_usage = {
            "total": memory_info.total,
            "available": memory_info.available,
            "used": memory_info.used,
            "percent": memory_info.percent
        }
        logging.info(f"Memory Usage: {memory_usage['percent']}%")
        return memory_usage
    except Exception as e:
        logging.error(f"Error fetching memory usage: {e}")
        return None

# Function to gather disk usage statistics
def get_disk_usage():
    try:
        disk_info = psutil.disk_usage('/')  # Get disk usage details
        disk_usage = {
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        }
        logging.info(f"Disk Usage: {disk_usage['percent']}%")
        return disk_usage
    except Exception as e:
        logging.error(f"Error fetching disk usage: {e}")
        return None

# Route to get server statistics
@app.route('/api/status', methods=['GET'])
def server_status():
    """API endpoint to get server monitoring statistics."""
    try:
        stats = {
            "cpu_usage": get_cpu_usage(),
            "memory_usage": get_memory_usage(),
            "disk_usage": get_disk_usage(),
        }
        return jsonify(stats), 200  # Return stats with HTTP status code 200
    except Exception as e:
        logging.error(f"Error fetching server status: {e}")
        return jsonify({"error": "Failed to retrieve server status"}), 500  # Return error with HTTP status code 500

# Start the Flask application
if __name__ == "__main__":
    try:
        logging.info("Starting server monitoring tool...")
        app.run(host='0.0.0.0', port=5000)  # Run server on all interfaces at port 5000
    except Exception as e:
        logging.error(f"Error starting the server: {e}")
```
