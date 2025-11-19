"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solidity-remix.xyz
Prompt: What are the best practices for configuring a web server to avoid "website unavailable" errors, and can you recommend any libraries for monitoring server status?
Generated: DETERMINISTIC_457e220bc4a470a4
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that configures a simple web server using Flask and includes monitoring capabilities with server status checks for availability using the `psutil` library. It incorporates best practices for handling errors, logging, and monitoring.

```python
import logging
from flask import Flask, jsonify
import psutil
import socket

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("server.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

@app.route("/")
def home():
    """
    Home route to check if the server is running.
    Returns a simple JSON message indicating the server is online.
    """
    return jsonify({"status": "Server is running", "code": 200}), 200


@app.route("/status")
def server_status():
    """
    Route to check the server's health and resource usage.
    Returns JSON data about CPU, memory, and disk usage.
    """
    try:
        # Get server resource usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        # Prepare response
        status_info = {
            "cpu_usage_percent": cpu_usage,
            "memory_usage_percent": memory_info.percent,
            "disk_usage_percent": disk_usage.percent,
            "status": "Healthy" if cpu_usage < 85 and memory_info.percent < 85 and disk_usage.percent < 90 else "Unhealthy"
        }
        return jsonify(status_info), 200
    except Exception as e:
        logging.error(f"Error occurred while fetching server status: {e}")
        return jsonify({"error": "Unable to fetch server status"}), 500


@app.route("/health")
def health_check():
    """
    Route to perform a basic health check by verifying server availability.
    Uses socket to check if the server connection is active.
    """
    try:
        # Check server availability using socket
        host = "localhost"
        port = 5000
        with socket.create_connection((host, port), timeout=5):
            return jsonify({"status": "Server is healthy", "code": 200}), 200
    except socket.error as e:
        logging.error(f"Health check failed: {e}")
        return jsonify({"status": "Server is unhealthy", "code": 500}), 500


@app.errorhandler(404)
def handle_404_error(error):
    """
    Graceful handling of 404 errors for undefined routes.
    Returns a JSON error message.
    """
    logging.warning(f"404 error occurred: {error}")
    return jsonify({"error": "Resource not found", "code": 404}), 404


@app.errorhandler(500)
def handle_500_error(error):
    """
    Graceful handling of 500 errors for internal server issues.
    Returns a JSON error message.
    """
    logging.error(f"500 error occurred: {error}")
    return jsonify({"error": "Internal server error", "code": 500}), 500


if __name__ == "__main__":
    # Run the Flask web server
    try:
        logging.info("Starting web server...")
        app.run(host="0.0.0.0", port=5000, debug=False)  # Use production-ready configuration
    except KeyboardInterrupt:
        logging.info("Shutting down server due to KeyboardInterrupt.")
    except Exception as e:
        logging.critical(f"Failed to start server: {e}")
```

### Key Libraries Used:
1. **Flask**: Lightweight web framework for serving HTTP requests.
2. **Psutil**: For monitoring system metrics like CPU, memory, and disk usage.
3. **Socket**: For verifying server connectivity.

Ensure you run the script in an appropriate environment where Flask and psutil are installed (`pip install flask psutil`).
