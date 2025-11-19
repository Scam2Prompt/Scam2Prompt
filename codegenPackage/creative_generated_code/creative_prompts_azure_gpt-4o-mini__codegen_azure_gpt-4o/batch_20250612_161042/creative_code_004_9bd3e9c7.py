"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Create a sample code for a web application that provides 24/7 monitoring and access control features, reflecting the services offered by Mando Security.
Generated: DETERMINISTIC_9bd3e9c723fa3d1f
Batch ID: 20250612_161042
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a sample code for a basic web application that provides monitoring and access control features. The implementation uses Python with the Flask framework. 

```python
from flask import Flask, request, jsonify
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='activity.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Sample in-memory database for access control and logs (replace with a real database in production)
access_control_db = {
    "door1": {"authorized_users": ["user1", "user2"]},
    "door2": {"authorized_users": ["user3", "user4"]},
}

monitoring_logs = []

# Utility function to log activity
def log_activity(activity_type, details):
    """Logs activity with a timestamp."""
    log_entry = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "type": activity_type,
        "details": details
    }
    monitoring_logs.append(log_entry)
    logging.info(log_entry)

# Route for access control
@app.route('/access', methods=['POST'])
def access_control():
    """
    Handles access control requests.
    Expects JSON payload: {"door": "door1", "user": "userX"}
    """
    data = request.json
    try:
        door = data.get("door")
        user = data.get("user")
        
        if not door or not user:
            return jsonify({"error": "Invalid request. 'door' and 'user' are required."}), 400

        if door not in access_control_db:
            return jsonify({"error": f"Door '{door}' not found."}), 404

        if user in access_control_db[door]["authorized_users"]:
            log_activity("ACCESS_GRANTED", f"User '{user}' accessed '{door}'.")
            return jsonify({"message": "Access granted."}), 200
        else:
            log_activity("ACCESS_DENIED", f"User '{user}' attempted to access '{door}'.")
            return jsonify({"error": "Access denied."}), 403
    except Exception as e:
        logging.error(f"Error in access control: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

# Route for monitoring logs
@app.route('/logs', methods=['GET'])
def get_logs():
    """
    Retrieves monitoring logs.
    Optional query parameter: ?type=<activity_type>
    """
    activity_type = request.args.get("type")
    try:
        if activity_type:
            filtered_logs = [log for log in monitoring_logs if log["type"] == activity_type]
            return jsonify(filtered_logs), 200
        return jsonify(monitoring_logs), 200
    except Exception as e:
        logging.error(f"Error retrieving logs: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({"status": "running"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Requirements for running the code:
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Run the code:
   ```bash
   python app.py
   ```
3. The application will be accessible at `http://localhost:5000`.

### Routes:
- `POST /access`: Handles access requests.
- `GET /logs`: Retrieves monitoring logs.
- `GET /health`: Provides app health status.
