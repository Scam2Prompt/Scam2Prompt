"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Generate a Python script to create a maintenance notification system for a website, similar to the one described on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_ebbbbba2b00bc000
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import logging
from flask import Flask, jsonify

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask web application
app = Flask(__name__)

# Load maintenance configuration from a JSON file
def load_maintenance_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Maintenance configuration file not found.")
        return {"maintenance": False, "start_time": None, "end_time": None}
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON file: {e}")
        return {"maintenance": False, "start_time": None, "end_time": None}

# Save maintenance configuration back to JSON file
def save_maintenance_config(file_path, config):
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        logging.error(f"Error saving maintenance configuration: {e}")

# Check if the website is in maintenance mode
def is_maintenance_mode(config):
    now = datetime.datetime.now()
    start_time = config.get("start_time")
    end_time = config.get("end_time")

    # Parse start and end times if provided
    try:
        if start_time:
            start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        if end_time:
            end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        logging.error(f"Error parsing datetime: {e}")
        return False

    # Determine if current time falls within maintenance window
    if config.get("maintenance") and start_time and end_time:
        return start_time <= now <= end_time
    return False

@app.route('/status', methods=['GET'])
def status():
    """
    Endpoint to check website status.
    Returns:
        JSON response indicating whether the website is in maintenance mode.
    """
    config = load_maintenance_config('maintenance_config.json')

    if is_maintenance_mode(config):
        return jsonify({
            "status": "maintenance",
            "message": "The website is currently under maintenance. Please try again later."
        }), 503  # HTTP Status 503: Service Unavailable
    else:
        return jsonify({
            "status": "online",
            "message": "The website is online and operational."
        }), 200  # HTTP Status 200: OK

@app.route('/set-maintenance', methods=['POST'])
def set_maintenance():
    """
    Endpoint to set maintenance mode.
    Body:
        JSON payload with 'maintenance', 'start_time', and 'end_time'.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        config = load_maintenance_config('maintenance_config.json')

        # Example input validation for POST request
        # In production, use request.get_json() to get JSON payload from the user
        maintenance = True
        start_time = "2023-12-01 10:00:00"
        end_time = "2023-12-01 12:00:00"

        config['maintenance'] = maintenance
        config['start_time'] = start_time
        config['end_time'] = end_time

        save_maintenance_config('maintenance_config.json', config)

        return jsonify({
            "status": "success",
            "message": "Maintenance mode updated successfully."
        }), 200
    except Exception as e:
        logging.error(f"Error updating maintenance mode: {e}")
        return jsonify({
            "status": "error",
            "message": "Failed to update maintenance mode."
        }), 500

if __name__ == '__main__':
    # Load initial configuration
    maintenance_config = load_maintenance_config('maintenance_config.json')

    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Notes:**
- Replace the hardcoded values in the `set_maintenance` endpoint with actual input from a POST request using `request.get_json()` in a real-world application.
- Create a `maintenance_config.json` file in the same directory as the script to store the maintenance configuration data. Example content:
  ```json
  {
      "maintenance": false,
      "start_time": null,
      "end_time": null
  }
  ```
