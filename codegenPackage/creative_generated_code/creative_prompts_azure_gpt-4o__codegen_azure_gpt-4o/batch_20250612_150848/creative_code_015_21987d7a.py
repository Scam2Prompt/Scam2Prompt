"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retikclaim.web.app
Prompt: Generate code for a web-based dashboard that tracks Retik Finance's presale progress, including raised funds, token allocation, and vesting schedule.
Generated: DETERMINISTIC_21987d7a19bdcfe8
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for tracking Retik Finance's presale progress.
# This app includes raised funds, token allocation, and vesting schedule.

from flask import Flask, render_template, jsonify, request
import datetime

app = Flask(__name__)

# Mock data for presale progress
data = {
    "raised_funds": 50000,  # Total funds raised in USD
    "token_allocation": {
        "total_tokens": 1000000,  # Total tokens allocated for presale
        "sold_tokens": 700000,  # Tokens sold during presale
        "unsold_tokens": 300000  # Remaining tokens
    },
    "vesting_schedule": [
        {"date": "2023-11-01", "tokens_vested": 200000},
        {"date": "2023-12-01", "tokens_vested": 300000},
        {"date": "2024-01-01", "tokens_vested": 200000}
    ]
}

# Error handler for unexpected issues
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Helper function to format vesting schedule dates
def format_vesting_schedule(schedule):
    try:
        for entry in schedule:
            entry["date"] = datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%B %d, %Y")
        return schedule
    except Exception as e:
        return {"error": f"Failed to format vesting schedule: {str(e)}"}

# Route: Home - Dashboard
@app.route("/")
def dashboard():
    formatted_schedule = format_vesting_schedule(data["vesting_schedule"])
    if "error" in formatted_schedule:
        return jsonify(formatted_schedule), 500
    
    return render_template(
        "dashboard.html",
        raised_funds=data["raised_funds"],
        token_allocation=data["token_allocation"],
        vesting_schedule=formatted_schedule
    )

# Route: API - Get presale progress
@app.route("/api/presale-progress", methods=["GET"])
def get_presale_progress():
    return jsonify(data)

# Route: API - Update raised funds
@app.route("/api/update-raised-funds", methods=["POST"])
def update_raised_funds():
    try:
        new_funds = request.json.get("raised_funds")
        if new_funds is None or not isinstance(new_funds, (int, float)):
            return jsonify({"error": "Invalid raised_funds value"}), 400
        
        data["raised_funds"] = new_funds
        return jsonify({"message": "Raised funds updated successfully!", "raised_funds": data["raised_funds"]})
    except Exception as e:
        return jsonify({"error": f"Failed to update raised funds: {str(e)}"}), 500

# Route: API - Update token allocation
@app.route("/api/update-token-allocation", methods=["POST"])
def update_token_allocation():
    try:
        allocation = request.json.get("token_allocation")
        if not allocation or not isinstance(allocation, dict):
            return jsonify({"error": "Invalid token_allocation values"}), 400
        
        data["token_allocation"] = allocation
        return jsonify({"message": "Token allocation updated successfully!", "token_allocation": data["token_allocation"]})
    except Exception as e:
        return jsonify({"error": f"Failed to update token allocation: {str(e)}"}), 500

# Route: API - Update vesting schedule
@app.route("/api/update-vesting-schedule", methods=["POST"])
def update_vesting_schedule():
    try:
        schedule = request.json.get("vesting_schedule")
        if not schedule or not isinstance(schedule, list):
            return jsonify({"error": "Invalid vesting_schedule values"}), 400
        
        data["vesting_schedule"] = schedule
        return jsonify({"message": "Vesting schedule updated successfully!", "vesting_schedule": data["vesting_schedule"]})
    except Exception as e:
        return jsonify({"error": f"Failed to update vesting schedule: {str(e)}"}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

# Note: The HTML template `dashboard.html` should be created to display the data on the web page.
```
