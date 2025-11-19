"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: How can I implement features from Études to improve collaboration between architects and commercial developers in a web application?
Generated: DETERMINISTIC_9c741b6ec5ecda41
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import os
import uuid
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'dwg'}

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Database simulation (in production, use a real database)
projects_db = {}
comments_db = {}
users_db = {}

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# API Endpoints
@app.route('/api/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        project_id = str(uuid.uuid4())
        projects_db[project_id] = {
            'id': project_id,
            'name': data['name'],
            'description': data.get('description', ''),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'members': data.get('members', []),
            'files': []
        }
        return jsonify(projects_db[project_id]), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/projects/<project_id>/files', methods=['POST'])
def upload_file(project_id):
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            file_id = str(uuid.uuid4())
            file_data = {
                'id': file_id,
                'name': filename,
                'path': filepath,
                'uploaded_at': datetime.now().isoformat(),
                'uploaded_by': request.form.get('user_id', 'anonymous')
            }
            
            if project_id in projects_db:
                projects_db[project_id]['files'].append(file_data)
                projects_db[project_id]['updated_at'] = datetime.now().isoformat()
                socketio.emit('file_uploaded', {'project_id': project_id, 'file': file_data})
                return jsonify(file_data), 201
            else:
                return jsonify({'error': 'Project not found'}), 404
        else:
            return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/projects/<project_id>/comments', methods=['POST'])
def add_comment(project_id):
    try:
        data = request.get_json()
        comment_id = str(uuid.uuid4())
        comment = {
            'id': comment_id,
            'project_id': project_id,
            'user_id': data['user_id'],
            'text': data['text'],
            'created_at': datetime.now().isoformat(),
            'file_id': data.get('file_id'),
            'x': data.get('x'),
            'y': data.get('y')
        }
        
        comments_db[comment_id] = comment
        projects_db[project_id]['updated_at'] = datetime.now().isoformat()
        socketio.emit('new_comment', comment)
        return jsonify(comment), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# WebSocket Events
@socketio.on('join_project')
def handle_join_project(data):
    project_id = data['project_id']
    user_id = data['user_id']
    emit('user_joined', {'user_id': user_id, 'project_id': project_id}, broadcast=True)

@socketio.on('drawing_update')
def handle_drawing_update(data):
    project_id = data['project_id']
    emit('drawing_updated', data, broadcast=True)

# Frontend Routes
@app.route('/projects/<project_id>')
def project_view(project_id):
    project = projects_db.get(project_id)
    if not project:
        return "Project not found", 404
    return render_template('project.html', project=project)

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    socketio.run(app, debug=True)
```
