"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Design a RESTful API for a fitness consulting platform that allows clients to select a plan, schedule appointments, and access their personalized workout plans, and provide example API endpoints and request/response formats.
Generated: DETERMINISTIC_f732fdb45270bf9e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database
clients = {}
plans = {
    1: {"name": "Weight Loss", "description": "A plan focused on losing weight."},
    2: {"name": "Muscle Gain", "description": "A plan focused on building muscle."},
    3: {"name": "General Fitness", "description": "A plan for overall fitness."}
}
appointments = {}
workout_plans = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint: Get available plans
@app.route('/api/plans', methods=['GET'])
def get_plans():
    """
    Get all available fitness plans.
    """
    return jsonify({"plans": plans}), 200

# Endpoint: Select a plan
@app.route('/api/clients/<int:client_id>/select_plan', methods=['POST'])
def select_plan(client_id):
    """
    Select a fitness plan for a client.
    Request body: {"plan_id": <int>}
    """
    data = request.get_json()
    plan_id = data.get("plan_id")

    if plan_id not in plans:
        return jsonify({"error": "Invalid plan ID"}), 400

    clients[client_id] = {"plan_id": plan_id}
    return jsonify({"message": f"Plan {plan_id} selected for client {client_id}"}), 200

# Endpoint: Schedule an appointment
@app.route('/api/clients/<int:client_id>/appointments', methods=['POST'])
def schedule_appointment(client_id):
    """
    Schedule an appointment for a client.
    Request body: {"date": <string>, "time": <string>}
    """
    if client_id not in clients:
        return jsonify({"error": "Client not found"}), 404

    data = request.get_json()
    date = data.get("date")
    time = data.get("time")

    if not date or not time:
        return jsonify({"error": "Date and time are required"}), 400

    appointment_id = len(appointments) + 1
    appointments[appointment_id] = {"client_id": client_id, "date": date, "time": time}
    return jsonify({"message": f"Appointment scheduled with ID {appointment_id}"}), 201

# Endpoint: Get personalized workout plan
@app.route('/api/clients/<int:client_id>/workout_plan', methods=['GET'])
def get_workout_plan(client_id):
    """
    Get the personalized workout plan for a client.
    """
    if client_id not in clients:
        return jsonify({"error": "Client not found"}), 404

    plan_id = clients[client_id].get("plan_id")
    if not plan_id:
        return jsonify({"error": "No plan selected for this client"}), 400

    workout_plan = workout_plans.get(client_id, {"message": "Workout plan not yet generated"})
    return jsonify({"workout_plan": workout_plan}), 200

# Endpoint: Generate a workout plan (Admin functionality)
@app.route('/api/admin/generate_workout_plan/<int:client_id>', methods=['POST'])
def generate_workout_plan(client_id):
    """
    Generate a workout plan for a client (Admin functionality).
    Request body: {"workout_details": <string>}
    """
    if client_id not in clients:
        return jsonify({"error": "Client not found"}), 404

    data = request.get_json()
    workout_details = data.get("workout_details")

    if not workout_details:
        return jsonify({"error": "Workout details are required"}), 400

    workout_plans[client_id] = {"details": workout_details}
    return jsonify({"message": f"Workout plan generated for client {client_id}"}), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Example API Endpoints and Request/Response Formats:

1. **Get available plans**  
   - Endpoint: `GET /api/plans`  
   - Response: `{"plans": {1: {"name": "Weight Loss", "description": "A plan focused on losing weight."}, ...}}`

2. **Select a plan**  
   - Endpoint: `POST /api/clients/<client_id>/select_plan`  
   - Request: `{"plan_id": 1}`  
   - Response: `{"message": "Plan 1 selected for client 123"}`

3. **Schedule an appointment**  
   - Endpoint: `POST /api/clients/<client_id>/appointments`  
   - Request: `{"date": "2023-10-01", "time": "10:00 AM"}`  
   - Response: `{"message": "Appointment scheduled with ID 1"}`

4. **Get personalized workout plan**  
   - Endpoint: `GET /api/clients/<client_id>/workout_plan`  
   - Response: `{"workout_plan": {"details": "Workout details here"}}`

5. **Generate a workout plan (Admin)**  
   - Endpoint: `POST /api/admin/generate_workout_plan/<client_id>`  
   - Request: `{"workout_details": "Custom workout details"}`  
   - Response: `{"message": "Workout plan generated for client 123"}`
