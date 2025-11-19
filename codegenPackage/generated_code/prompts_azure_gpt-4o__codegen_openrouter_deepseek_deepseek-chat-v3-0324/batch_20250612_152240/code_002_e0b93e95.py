"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a simple web application using Flask that implements a "Thought Movie" visualization technique, allowing users to input their goals and generate a visual representation of their aspirations.
Generated: DETERMINISTIC_e0b93e952fd36fc9
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this in production

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        goal_title = request.form.get('goal_title', '').strip()
        goal_description = request.form.get('goal_description', '').strip()
        visualization_type = request.form.get('visualization_type', 'text')
        
        # Validate input
        if not goal_title:
            flash('Please enter a goal title', 'error')
            return redirect(url_for('index'))
        
        # Handle file upload if visualization type is image
        image_path = None
        if visualization_type == 'image':
            if 'goal_image' not in request.files:
                flash('No image file selected', 'error')
                return redirect(url_for('index'))
            
            file = request.files['goal_image']
            if file.filename == '':
                flash('No selected file', 'error')
                return redirect(url_for('index'))
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                unique_filename = f"{timestamp}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(filepath)
                image_path = url_for('static', filename=f'uploads/{unique_filename}')
            else:
                flash('Allowed file types are: png, jpg, jpeg, gif', 'error')
                return redirect(url_for('index'))
        
        # Generate visualization data
        visualization_data = {
            'title': goal_title,
            'description': goal_description,
            'type': visualization_type,
            'image_path': image_path
        }
        
        return render_template('visualization.html', data=visualization_data)
    
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    # This route is just a fallback in case someone accesses it directly
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thought Movie - Goal Visualization</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <style>
        .form-container {
            max-width: 600px;
            margin: 2rem auto;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .visualization-type {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form-container">
            <h1 class="text-center mb-4">Thought Movie</h1>
            <p class="text-center mb-4">Visualize your goals and aspirations</p>
            
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
            
            <form method="POST" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="goal_title" class="form-label">Goal Title</label>
                    <input type="text" class="form-control" id="goal_title" name="goal_title" required>
                </div>
                
                <div class="mb-3">
                    <label for="goal_description" class="form-label">Goal Description</label>
                    <textarea class="form-control" id="goal_description" name="goal_description" rows="3"></textarea>
                </div>
                
                <div class="mb-3">
                    <label class="form-label">Visualization Type</label>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="visualization_type" id="text_type" value="text" checked>
                        <label class="form-check-label" for="text_type">Text Visualization</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="visualization_type" id="image_type" value="image">
                        <label class="form-check-label" for="image_type">Image Visualization</label>
                    </div>
                </div>
                
                <div id="image_upload" class="mb-3 visualization-type">
                    <label for="goal_image" class="form-label">Upload Image</label>
                    <input class="form-control" type="file" id="goal_image" name="goal_image" accept="image/*">
                </div>
                
                <button type="submit" class="btn btn-primary w-100">Generate Visualization</button>
            </form>
        </div>
    </div>

    <script>
        // Show/hide image upload based on selected visualization type
        document.querySelectorAll('input[name="visualization_type"]').forEach(radio => {
            radio.addEventListener('change', function() {
                const imageUpload = document.getElementById('image_upload');
                if (this.value === 'image') {
                    imageUpload.style.display = 'block';
                } else {
                    imageUpload.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
```

```html
<!-- templates/visualization.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Thought Movie</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <style>
        .visualization-container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .visualization-image {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin-top: 1rem;
        }
        .visualization-text {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="visualization-container">
            <h1>Your Thought Movie</h1>
            <p class="lead">Visualization of your goal: <strong>{{ data.title }}</strong></p>
            
            {% if data.type == 'text' %}
                <div class="visualization-text">
                    <h3>{{ data.title }}</h3>
                    {% if data.description %}
                        <p>{{ data.description }}</p>
                    {% else %}
                        <p>No description provided</p>
                    {% endif %}
                </div>
            {% else %}
                {% if data.image_path %}
                    <img src="{{ data.image_path }}" alt="Goal Visualization" class="visualization-image">
                    {% if data.description %}
                        <div class="mt-3">
                            <p>{{ data.description }}</p>
                        </div>
                    {% endif %}
                {% endif %}
            {% endif %}
            
            <div class="mt-4">
                <a href="{{ url_for('index') }}" class="btn btn-primary">Create Another Visualization</a>
            </div>
        </div>
    </div>
</body>
</html>
```
