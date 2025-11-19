"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Generate code for a web interface that allows users to upload documents for translation, mimicking the online submission system described on the Solid SRL website.
Generated: DETERMINISTIC_b6d4f844a9f0090d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'doc', 'docx', 'odt', 'rtf'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Handle file upload and form submission."""
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part in the request')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file, browser submits empty file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # Validate file
        if file and allowed_file(file.filename):
            # Secure filename and create unique path
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            
            try:
                # Save file
                file.save(filepath)
                
                # Process form data
                name = request.form.get('name', '').strip()
                email = request.form.get('email', '').strip()
                phone = request.form.get('phone', '').strip()
                source_lang = request.form.get('source_lang', '').strip()
                target_lang = request.form.get('target_lang', '').strip()
                notes = request.form.get('notes', '').strip()
                
                # Validate required fields
                if not all([name, email, source_lang, target_lang]):
                    flash('Please fill all required fields')
                    os.remove(filepath)  # Clean up uploaded file
                    return redirect(request.url)
                
                # Here you would typically:
                # 1. Save the submission to a database
                # 2. Send confirmation email
                # 3. Process the translation request
                
                flash('Your document has been submitted for translation!')
                return redirect(url_for('upload_file'))
            
            except Exception as e:
                flash(f'An error occurred: {str(e)}')
                return redirect(request.url)
        
        else:
            flash('File type not allowed. Allowed types: txt, pdf, doc, docx, odt, rtf')
            return redirect(request.url)
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/upload.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Translation Submission</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .flash-messages {
            margin: 20px 0;
        }
        .flash-message {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
        }
        .error {
            background-color: #ffdddd;
            border-left: 5px solid #f44336;
        }
        .success {
            background-color: #ddffdd;
            border-left: 5px solid #4CAF50;
        }
    </style>
</head>
<body>
    <h1>Document Translation Submission</h1>
    
    <div class="flash-messages">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>
    
    <form method="POST" enctype="multipart/form-data">
        <div class="form-group">
            <label for="name" class="required">Your Name</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email" class="required">Email Address</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone">
        </div>
        
        <div class="form-group">
            <label for="source_lang" class="required">Source Language</label>
            <select id="source_lang" name="source_lang" required>
                <option value="">Select a language</option>
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
                <option value="it">Italian</option>
                <option value="pt">Portuguese</option>
                <option value="ru">Russian</option>
                <option value="zh">Chinese</option>
                <option value="ja">Japanese</option>
                <option value="ar">Arabic</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="target_lang" class="required">Target Language</label>
            <select id="target_lang" name="target_lang" required>
                <option value="">Select a language</option>
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
                <option value="it">Italian</option>
                <option value="pt">Portuguese</option>
                <option value="ru">Russian</option>
                <option value="zh">Chinese</option>
                <option value="ja">Japanese</option>
                <option value="ar">Arabic</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="file" class="required">Document to Translate</label>
            <input type="file" id="file" name="file" required>
            <small>Allowed file types: .txt, .pdf, .doc, .docx, .odt, .rtf (Max 16MB)</small>
        </div>
        
        <div class="form-group">
            <label for="notes">Special Instructions</label>
            <textarea id="notes" name="notes"></textarea>
        </div>
        
        <button type="submit" class="btn">Submit for Translation</button>
    </form>
</body>
</html>
```
