"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: Create a sandbox environment for experimenting with new AI models using Mary AI's platform. Include features for collaborative research and rapid prototyping.
Generated: DETERMINISTIC_d91b6a3db72d3a95
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required imports
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import os
import uuid
import threading

# Initialize Flask app and SocketIO for real-time collaboration
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configuration for file uploads
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"py", "txt", "json", "yaml"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory storage for session and experiment data
sessions = {}
experiments = {}

# Helper functions
def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_id():
    """Generate a unique identifier for sessions and experiments."""
    return str(uuid.uuid4())

# API to create a new sandbox session
@app.route("/create_session", methods=["POST"])
def create_session():
    """Create a new sandbox session."""
    session_id = generate_unique_id()
    sessions[session_id] = {
        "users": [],
        "experiments": []
    }
    return jsonify({"success": True, "session_id": session_id}), 201

# API to upload files for experiments
@app.route("/upload_file", methods=["POST"])
def upload_file():
    """Handle file uploads for experiments."""
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        return jsonify({"success": True, "filepath": filepath}), 200

    return jsonify({"error": "Invalid file type"}), 400

# API to create a new experiment in a sandbox session
@app.route("/create_experiment/<session_id>", methods=["POST"])
def create_experiment(session_id):
    """Create a new experiment within a specific session."""
    if session_id not in sessions:
        return jsonify({"error": "Session not found"}), 404

    experiment_id = generate_unique_id()
    experiment_data = {
        "id": experiment_id,
        "name": request.json.get("name", "Untitled Experiment"),
        "description": request.json.get("description", ""),
        "status": "created",
        "files": []
    }
    sessions[session_id]["experiments"].append(experiment_data)
    experiments[experiment_id] = experiment_data
    return jsonify({"success": True, "experiment_id": experiment_id}), 201

# API to get details of a session
@app.route("/get_session/<session_id>", methods=["GET"])
def get_session(session_id):
    """Retrieve details of a specific session."""
    if session_id not in sessions:
        return jsonify({"error": "Session not found"}), 404

    return jsonify(sessions[session_id]), 200

# Real-time collaboration: Join session
@socketio.on("join_session")
def join_session(data):
    """Handle user joining a session for collaboration."""
    session_id = data.get("session_id")
    username = data.get("username")

    if session_id not in sessions:
        emit("error", {"error": "Session not found"})
        return

    if username not in sessions[session_id]["users"]:
        sessions[session_id]["users"].append(username)

    emit("user_joined", {"username": username}, broadcast=True, room=session_id)

# Real-time collaboration: Broadcast changes
@socketio.on("experiment_update")
def experiment_update(data):
    """Broadcast updates to an experiment in real-time."""
    session_id = data.get("session_id")
    if session_id not in sessions:
        emit("error", {"error": "Session not found"})
        return

    emit("experiment_update", data, broadcast=True, room=session_id)

# Background worker for experiment execution (mockup)
def execute_experiment(experiment_id):
    """Mock function to simulate experiment execution."""
    experiment = experiments.get(experiment_id)
    if not experiment:
        return

    # Mock experiment execution
    experiment["status"] = "running"
    socketio.emit("experiment_status", {"experiment_id": experiment_id, "status": "running"})

    # Simulate execution time
    threading.Timer(10, complete_experiment, args=(experiment_id,)).start()

def complete_experiment(experiment_id):
    """Mock function to complete experiment execution."""
    experiment = experiments.get(experiment_id)
    if not experiment:
        return

    experiment["status"] = "completed"
    socketio.emit("experiment_status", {"experiment_id": experiment_id, "status": "completed"})

# API to start an experiment
@app.route("/start_experiment/<experiment_id>", methods=["POST"])
def start_experiment(experiment_id):
    """Start execution of an experiment."""
    experiment = experiments.get(experiment_id)
    if not experiment:
        return jsonify({"error": "Experiment not found"}), 404

    if experiment["status"] != "created":
        return jsonify({"error": "Experiment already running or completed"}), 400

    # Start the execution in a separate thread
    threading.Thread(target=execute_experiment, args=(experiment_id,)).start()
    return jsonify({"success": True, "status": "running"}), 200

# Main entry point
if __name__ == "__main__":
    # Run the Flask app with SocketIO
    socketio.run(app, host="0.0.0.0", port=5000)
```
