"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: Write code for a minimum viable product (MVP) using Mary AI's platform to rapidly prototype an idea for a startup. Include features for real-time collaboration and AI-assisted development.
Generated: DETERMINISTIC_a7ea5770abc3a1dd
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: mary_ai_mvp.py

"""
Minimum Viable Product (MVP) for a startup using Mary AI's platform.
This MVP includes features for real-time collaboration and AI-assisted development.
Key Features:
1. Real-time Collaboration: Users can edit and share projects simultaneously.
2. AI-Assisted Development: Mary AI suggests code completions and optimizations.

Requirements:
- Python 3.10 or higher
- Mary AI SDK pre-installed (`pip install mary-ai-sdk`)
- Flask for server-side support (`pip install flask flask-socketio`)
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from mary_ai import MaryAI, MaryAIException

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_secret_key")
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize Mary AI client
try:
    mary_ai_client = MaryAI(api_key=os.getenv("MARY_AI_API_KEY"))
except MaryAIException as e:
    raise SystemExit(f"Failed to initialize Mary AI: {str(e)}")

# Real-time collaboration data structure (in-memory store for simplicity; use a database for production)
projects = {}  # Dictionary to store project content: {project_id: {users: [], content: ""}}

# Endpoint for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to create a new project
@app.route('/create_project', methods=['POST'])
def create_project():
    try:
        project_id = request.json.get('project_id')
        if not project_id:
            return jsonify({"error": "Missing project_id"}), 400
        
        if project_id in projects:
            return jsonify({"error": "Project already exists"}), 400

        projects[project_id] = {"users": [], "content": ""}
        return jsonify({"message": "Project created successfully", "project_id": project_id}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to create project: {str(e)}"}), 500

@socketio.on('join_project')
def join_project(data):
    """
    Event handler for users joining a project.
    """
    try:
        project_id = data.get('project_id')
        username = data.get('username')

        if not project_id or not username:
            emit('error', {"error": "Missing project_id or username"})
            return
        
        if project_id not in projects:
            emit('error', {"error": "Project not found"})
            return

        # Add user to project
        if username not in projects[project_id]['users']:
            projects[project_id]['users'].append(username)
        emit('joined_project', {"project_id": project_id, "content": projects[project_id]['content']}, broadcast=True)
    except Exception as e:
        emit('error', {"error": f"Failed to join project: {str(e)}"})

@socketio.on('update_content')
def update_content(data):
    """
    Event handler for updating project content.
    """
    try:
        project_id = data.get('project_id')
        content = data.get('content')

        if not project_id or content is None:
            emit('error', {"error": "Missing project_id or content"})
            return

        if project_id not in projects:
            emit('error', {"error": "Project not found"})
            return

        # Update project content
        projects[project_id]["content"] = content
        emit('content_updated', {"project_id": project_id, "content": content}, broadcast=True)
    except Exception as e:
        emit('error', {"error": f"Failed to update content: {str(e)}"})

@app.route('/ai_suggestions', methods=['POST'])
def ai_suggestions():
    """
    Endpoint to provide AI-assisted code suggestions.
    """
    try:
        code_snippet = request.json.get('code_snippet')
        if not code_snippet:
            return jsonify({"error": "Missing code_snippet"}), 400
        
        # Use Mary AI to generate suggestions
        suggestions = mary_ai_client.get_code_suggestions(code_snippet)
        return jsonify({"suggestions": suggestions}), 200
    except MaryAIException as e:
        return jsonify({"error": f"Failed to generate suggestions: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask server with SocketIO
    socketio.run(app, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
```

**Note:** 
- This code assumes Mary AI provides an SDK with a `get_code_suggestions` method.
- Replace the `index.html` with a suitable frontend to interact with the real-time collaboration and AI-assisted development features.
- For production, consider using a database (e.g., PostgreSQL, MongoDB) to store project data instead of an in-memory dictionary.
