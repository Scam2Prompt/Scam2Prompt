"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: Develop a REST API that enables fans to upload and share short video "Grooves" promoting their favorite artist's songs, while earning tokenized rewards ($GROOVE).
Generated: DETERMINISTIC_73995249f5d7c1a8
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize Flask App
app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi'}
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB limit for video files

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create uploads folder if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Sample tokenized rewards data store (in-memory)
user_rewards = {}

# Route to upload video grooves
@app.route('/upload', methods=['POST'])
def upload_groove():
    try:
        # Check if the request has a file
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Validate file type
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Add tokenized reward logic
            user_id = request.form.get('user_id', 'guest')
            reward = user_rewards.get(user_id, 0)
            user_rewards[user_id] = reward + 10  # Example of adding reward tokens

            return jsonify({'message': 'File uploaded successfully', 'filename': filename, '$GROOVE_added': 10}), 201
        else:
            return jsonify({'error': 'Invalid file type'}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

# Route to get user rewards
@app.route('/rewards/<user_id>', methods=['GET'])
def get_rewards(user_id):
    try:
        if user_id in user_rewards:
            return jsonify({'user_id': user_id, 'reward_balance': user_rewards[user_id]}), 200
        else:
            return jsonify({'message': 'No rewards found for this user'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

# Route to list uploaded grooves
@app.route('/grooves', methods=['GET'])
def list_grooves():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'uploaded_files': files}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

# Main entry point to run the server
if __name__ == '__main__':
    app.run(debug=True)
```
