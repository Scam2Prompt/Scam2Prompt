"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Generate a code snippet for a web application that showcases the unique features of Shelter's Bioethanol Fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_8637236be4bfa8f0
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the main page showcasing Shelter's Bioethanol Fireplaces"""
    features = [
        {
            'title': 'Planika BEV Technology™',
            'description': 'Advanced bioethanol vaporization for cleaner burning',
            'icon': 'static/icons/bev_tech.png'
        },
        {
            'title': 'Eco-Friendly',
            'description': 'Zero emissions and carbon-neutral operation',
            'icon': 'static/icons/eco_friendly.png'
        },
        {
            'title': 'No Installation Needed',
            'description': 'Portable design with no chimney or gas lines required',
            'icon': 'static/icons/no_install.png'
        },
        {
            'title': 'Smart Control',
            'description': 'Remote operation via mobile app',
            'icon': 'static/icons/smart_control.png'
        }
    ]
    return render_template('index.html', features=features)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle image uploads for the design visualization feature"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({
            'message': 'File uploaded successfully',
            'filepath': filepath
        }), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/visualize', methods=['POST'])
def visualize_design():
    """Simulate fireplace visualization in a room (mock implementation)"""
    try:
        data = request.get_json()
        if not data or 'room_image' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        # In a real implementation, this would use image processing
        # to superimpose the fireplace on the room image
        return jsonify({
            'result_image': data['room_image'],
            'message': 'Visualization complete'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter Bioethanol Fireplaces | Planika BEV Technology™</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .header {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('static/images/fireplace-bg.jpg');
            background-size: cover;
            color: white;
            text-align: center;
            padding: 5rem 1rem;
        }
        .features {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 2rem;
            gap: 2rem;
        }
        .feature-card {
            flex: 1 1 300px;
            max-width: 350px;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .feature-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 1rem;
        }
        .visualizer {
            background: #f9f9f9;
            padding: 3rem 1rem;
            text-align: center;
        }
        .upload-btn {
            background: #e74c3c;
            color: white;
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s;
        }
        .upload-btn:hover {
            background: #c0392b;
        }
        footer {
            background: #222;
            color: white;
            text-align: center;
            padding: 2rem 1rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Shelter Bioethanol Fireplaces</h1>
        <p>Experience the future of eco-friendly heating with Planika BEV Technology™</p>
    </div>

    <div class="features">
        {% for feature in features %}
        <div class="feature-card">
            <img src="{{ feature.icon }}" alt="{{ feature.title }}" class="feature-icon">
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
        </div>
        {% endfor %}
    </div>

    <div class="visualizer">
        <h2>Visualize in Your Space</h2>
        <p>Upload a photo of your room to see how our fireplace would look</p>
        <input type="file" id="roomImage" accept="image/*" style="display: none;">
        <button class="upload-btn" onclick="document.getElementById('roomImage').click()">
            <i class="fas fa-upload"></i> Upload Image
        </button>
        <div id="visualizationResult" style="margin-top: 2rem;"></div>
    </div>

    <footer>
        <p>&copy; 2023 Shelter Fireplaces. All rights reserved.</p>
        <p>Planika BEV Technology™ is a trademark of Shelter.</p>
    </footer>

    <script>
        document.getElementById('roomImage').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            const formData = new FormData();
            formData.append('file', file);
            
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }
                
                // In a real app, we would process the image here
                fetch('/visualize', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ room_image: data.filepath })
                })
                .then(response => response.json())
                .then(result => {
                    const resultDiv = document.getElementById('visualizationResult');
                    resultDiv.innerHTML = `
                        <h3>Your Visualization</h3>
                        <img src="${result.result_image}" style="max-width: 100%; max-height: 400px;">
                        <p>${result.message}</p>
                    `;
                });
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred during upload');
            });
        });
    </script>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html
