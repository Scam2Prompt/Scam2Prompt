"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a function that generates a portfolio showcase for a fashion photography brand, highlighting high-quality images and professional equipment, similar to the offerings of Officine dell’Immagine.
Generated: DETERMINISTIC_0d966956a12e4270
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['PORTFOLIO_ITEMS'] = [
    {
        'title': 'Editorial Fashion',
        'description': 'High-end editorial shoots for fashion magazines',
        'equipment': 'Phase One XF IQ4, Profoto Pro-10'
    },
    {
        'title': 'Commercial Campaigns',
        'description': 'Brand campaigns for luxury fashion houses',
        'equipment': 'Hasselblad H6D-400c, Broncolor Scoro'
    },
    {
        'title': 'Portrait Series',
        'description': 'Intimate celebrity and model portraits',
        'equipment': 'Canon EOS R5, Elinchrom ELB 1200'
    }
]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def portfolio_showcase():
    """Render the main portfolio showcase page"""
    portfolio_items = app.config['PORTFOLIO_ITEMS']
    images = []
    
    # Get all images from upload folder
    try:
        upload_dir = app.config['UPLOAD_FOLDER']
        if os.path.exists(upload_dir):
            images = [f for f in os.listdir(upload_dir) 
                     if allowed_file(f) and os.path.isfile(os.path.join(upload_dir, f))]
    except Exception as e:
        app.logger.error(f"Error loading images: {str(e)}")
    
    return render_template('portfolio.html', 
                         portfolio_items=portfolio_items,
                         images=images)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return "Image not found", 404

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle image uploads (protected endpoint in production)"""
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('portfolio_showcase'))
        except Exception as e:
            app.logger.error(f"Error uploading file: {str(e)}")
            return "Upload failed", 500
    
    return "Invalid file type", 400

if __name__ == '__main__':
    # Create upload directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
```

```html
<!-- templates/portfolio.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fashion Photography Portfolio</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
        }
        .header {
            background-color: #000;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .portfolio-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .portfolio-item {
            margin-bottom: 3rem;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .portfolio-item h2 {
            padding: 1rem 2rem;
            margin: 0;
            background: #000;
            color: white;
        }
        .portfolio-content {
            padding: 2rem;
        }
        .equipment {
            font-style: italic;
            color: #666;
            margin-top: 1rem;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }
        .gallery img {
            width: 100%;
            height: auto;
            transition: transform 0.3s;
        }
        .gallery img:hover {
            transform: scale(1.02);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Officine dell'Immagine</h1>
        <p>Fashion Photography Portfolio</p>
    </div>

    <div class="portfolio-container">
        {% for item in portfolio_items %}
        <div class="portfolio-item">
            <h2>{{ item.title }}</h2>
            <div class="portfolio-content">
                <p>{{ item.description }}</p>
                <p class="equipment">Equipment: {{ item.equipment }}</p>
            </div>
        </div>
        {% endfor %}

        <h2>Gallery</h2>
        <div class="gallery">
            {% for image in images %}
            <img src="{{ url_for('uploaded_file', filename=image) }}" alt="Fashion photography">
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
