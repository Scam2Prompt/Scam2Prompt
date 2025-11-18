"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Write code to create a "Sermon Manager" feature for a church website, including functionality for uploading sermons, categorizing them by date and topic, and enabling users to stream or download them. Use ChurchProWeb's design principles for user-friendly navigation.
Generated: DETERMINISTIC_629b04e13608f1c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, send_file, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads/sermons'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'mp4', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database simulation (would ideally be a real database in production)
sermons = []

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Homepage
@app.route('/')
def home():
    return render_template("index.html", sermons=sermons)

# Route: Upload sermon
@app.route('/upload', methods=['GET', 'POST'])
def upload_sermon():
    if request.method == 'POST':
        # Check if file is provided in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        # Validate file type
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Extract sermon metadata
            title = request.form.get('title', 'Untitled Sermon')
            topic = request.form.get('topic', 'General')
            date = datetime.now().strftime('%Y-%m-%d')

            # Add sermon to database (list in this case)
            sermons.append({
                'title': title,
                'filename': filename,
                'topic': topic,
                'date': date,
                'path': file_path
            })

            return redirect(url_for('home'))
        else:
            return jsonify({"error": "Invalid file type"}), 400
    return render_template("upload.html")

# Route: Stream sermon
@app.route('/stream/<filename>')
def stream_sermon(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return jsonify({"error": "File not found"}), 404

# Route: Download sermon
@app.route('/download/<filename>')
def download_sermon(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404

# Route: Filter by topic
@app.route('/filter/topic/<topic>')
def filter_by_topic(topic):
    filtered_sermons = [sermon for sermon in sermons if sermon['topic'].lower() == topic.lower()]
    return render_template("filter.html", sermons=filtered_sermons, filter_type="Topic", filter_value=topic)

# Route: Filter by date
@app.route('/filter/date/<date>')
def filter_by_date(date):
    filtered_sermons = [sermon for sermon in sermons if sermon['date'] == date]
    return render_template("filter.html", sermons=filtered_sermons, filter_type="Date", filter_value=date)

# Error Handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- The `index.html`, `upload.html`, and `filter.html` templates should be created separately for rendering the pages. 
- In a production environment, use a real database (like PostgreSQL or MySQL) instead of an in-memory list for storing sermons.
