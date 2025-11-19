"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: "Develop an API for monitoring and controlling a water filtration system, incorporating features such as real-time water quality monitoring and automated filter replacement alerts."
Generated: DETERMINISTIC_149df9eb743214ea
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

# Simulated water quality data
water_quality = {
    "pH": 7.0,
    "turbidity": 1.0,  # NTU (Nephelometric Turbidity Units)
    "temperature": 25.0,  # Celsius
    "last_filter_replacement": datetime.datetime.now() - datetime.timedelta(days=30),
    "filter_lifespan_days": 90
}

# Helper function to check filter replacement status
def check_filter_status():
    days_since_replacement = (datetime.datetime.now() - water_quality["last_filter_replacement"]).days
    if days_since_replacement >= water_quality["filter_lifespan_days"]:
        return "Filter replacement required"
    return f"Filter is operational. {water_quality['filter_lifespan_days'] - days_since_replacement} days remaining."

# Endpoint: Get real-time water quality data
@app.route('/api/water-quality', methods=['GET'])
def get_water_quality():
    try:
        # Simulate real-time data fluctuations
        water_quality["pH"] = round(random.uniform(6.5, 7.5), 2)
        water_quality["turbidity"] = round(random.uniform(0.5, 2.0), 2)
        water_quality["temperature"] = round(random.uniform(20.0, 30.0), 2)

        response = {
            "status": "success",
            "data": {
                "pH": water_quality["pH"],
                "turbidity": water_quality["turbidity"],
                "temperature": water_quality["temperature"],
                "filter_status": check_filter_status()
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Endpoint: Replace filter
@app.route('/api/replace-filter', methods=['POST'])
def replace_filter():
    try:
        water_quality["last_filter_replacement"] = datetime.datetime.now()
        response = {
            "status": "success",
            "message": "Filter replacement recorded successfully."
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Endpoint: Get filter replacement history
@app.route('/api/filter-history', methods=['GET'])
def get_filter_history():
    try:
        response = {
            "status": "success",
            "data": {
                "last_filter_replacement": water_quality["last_filter_replacement"].strftime("%Y-%m-%d %H:%M:%S"),
                "filter_lifespan_days": water_quality["filter_lifespan_days"]
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "Endpoint not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
