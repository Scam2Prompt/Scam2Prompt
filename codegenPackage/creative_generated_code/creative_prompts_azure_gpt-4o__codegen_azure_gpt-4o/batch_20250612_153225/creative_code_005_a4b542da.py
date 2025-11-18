"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Develop a REST API in Flask to manage sports club memberships, including features for retrieving class schedules, trainer details, and pricing plans as described on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_a4b542da536ed10e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for the API
class_schedules = [
    {"id": 1, "class_name": "Yoga", "schedule": "Monday, Wednesday, Friday - 10:00 AM"},
    {"id": 2, "class_name": "Pilates", "schedule": "Tuesday, Thursday - 5:00 PM"},
    {"id": 3, "class_name": "Zumba", "schedule": "Saturday - 2:00 PM"},
]

trainer_details = [
    {"id": 1, "name": "John Doe", "specialty": "Yoga"},
    {"id": 2, "name": "Jane Smith", "specialty": "Pilates"},
    {"id": 3, "name": "Mike Brown", "specialty": "Zumba"},
]

pricing_plans = [
    {"id": 1, "plan_name": "Monthly", "price": "$50"},
    {"id": 2, "plan_name": "Quarterly", "price": "$130"},
    {"id": 3, "plan_name": "Yearly", "price": "$500"},
]


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404


# Error handler for general server errors
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"error": error.description}), error.code


# Route to retrieve class schedules
@app.route('/class-schedules', methods=['GET'])
def get_class_schedules():
    return jsonify({"class_schedules": class_schedules})


# Route to retrieve trainer details
@app.route('/trainers', methods=['GET'])
def get_trainers():
    return jsonify({"trainers": trainer_details})


# Route to retrieve pricing plans
@app.route('/pricing-plans', methods=['GET'])
def get_pricing_plans():
    return jsonify({"pricing_plans": pricing_plans})


# Route to retrieve a specific class schedule by ID
@app.route('/class-schedules/<int:schedule_id>', methods=['GET'])
def get_class_schedule_by_id(schedule_id):
    schedule = next((item for item in class_schedules if item["id"] == schedule_id), None)
    if schedule:
        return jsonify({"class_schedule": schedule})
    return jsonify({"error": "Class schedule not found"}), 404


# Route to retrieve a specific trainer by ID
@app.route('/trainers/<int:trainer_id>', methods=['GET'])
def get_trainer_by_id(trainer_id):
    trainer = next((item for item in trainer_details if item["id"] == trainer_id), None)
    if trainer:
        return jsonify({"trainer": trainer})
    return jsonify({"error": "Trainer not found"}), 404


# Route to retrieve a specific pricing plan by ID
@app.route('/pricing-plans/<int:plan_id>', methods=['GET'])
def get_pricing_plan_by_id(plan_id):
    plan = next((item for item in pricing_plans if item["id"] == plan_id), None)
    if plan:
        return jsonify({"pricing_plan": plan})
    return jsonify({"error": "Pricing plan not found"}), 404


# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```
