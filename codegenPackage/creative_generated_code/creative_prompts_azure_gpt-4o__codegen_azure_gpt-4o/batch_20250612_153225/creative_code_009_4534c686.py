"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Develop an API that facilitates communication between IoT health devices and a centralized smart medical system, referencing the H-IOT framework described by Hooshmand Teb.
Generated: DETERMINISTIC_4534c686acf35daf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated database for storing IoT device data
iot_device_data = {}

# Helper function to validate incoming IoT device data
def validate_device_data(data):
    required_fields = ["device_id", "timestamp", "data_type", "value"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, "Valid data"

# Endpoint: Register IoT device data
@app.route('/api/iot/register', methods=['POST'])
def register_device_data():
    """
    Endpoint for IoT devices to send health-related data to the centralized system.
    Request Body:
        - device_id (str): The unique ID of the IoT device
        - timestamp (str): ISO 8601 formatted timestamp
        - data_type (str): Type of health data (e.g., 'heart_rate', 'temperature')
        - value (float): Health data value
    Response:
        - 200: Success
        - 400: Bad Request with error message
        - 500: Internal Server Error
    """
    try:
        # Parse incoming JSON data
        data = request.json
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        # Validate the data
        is_valid, message = validate_device_data(data)
        if not is_valid:
            return jsonify({"error": message}), 400
        
        # Store the data in the simulated database
        device_id = data["device_id"]
        if device_id not in iot_device_data:
            iot_device_data[device_id] = []
        iot_device_data[device_id].append(data)
        
        logging.info(f"Data registered from device: {device_id}")
        return jsonify({"message": "Data registered successfully"}), 200
        
    except Exception as e:
        logging.error(f"Error while registering device data: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Endpoint: Retrieve IoT device data
@app.route('/api/iot/data/<device_id>', methods=['GET'])
def get_device_data(device_id):
    """
    Endpoint to retrieve health data for a specific IoT device.
    URL Parameters:
        - device_id (str): The unique ID of the IoT device
    Response:
        - 200: Success with data
        - 404: Device not found
    """
    try:
        if device_id not in iot_device_data:
            return jsonify({"error": "Device not found"}), 404
        
        device_data = iot_device_data[device_id]
        return jsonify({"device_id": device_id, "data": device_data}), 200
    
    except Exception as e:
        logging.error(f"Error while retrieving device data: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Endpoint: Health check for the API
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health of the API.
    Response:
        - 200: API is healthy
    """
    return jsonify({"status": "API is running"}), 200

# Run the Flask application
if __name__ == "__main__":
    # Use production-ready configuration for Flask
    app.run(host='0.0.0.0', port=5000)
```
