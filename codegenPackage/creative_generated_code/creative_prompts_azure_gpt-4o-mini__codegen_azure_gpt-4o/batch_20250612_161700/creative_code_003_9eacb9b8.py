"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Develop a simple web application that enables users to create custom avatars for the Meme Moguls game using their favorite memes.
Generated: DETERMINISTIC_9eacb9b8c9275312
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a complete implementation using Python with the Flask framework for the backend and HTML/CSS/JavaScript for the frontend. The application allows users to upload an image and create a custom avatar.

### `app.py` (Flask Backend)
```python
from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Limit uploads to 5MB

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and creation of avatar."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
```

---

### `templates/index.html` (Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Moguls - Avatar Creator</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Create Your Avatar for Meme Moguls</h1>
        <form id="uploadForm" enctype="multipart/form-data">
            <label for="fileInput">Choose your favorite meme:</label>
            <input type="file" id="fileInput" name="file" accept="image/*" required>
            <button type="submit">Upload & Create Avatar</button>
        </form>
        <div id="result"></div>
    </div>
    <script src="/static/script.js"></script>
</body>
</html>
```

---

### `static/style.css` (Styling)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

.container {
    width: 50%;
    margin: 0 auto;
    padding: 20px;
    background: white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

h1 {
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input[type="file"] {
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

#result {
    margin-top: 20px;
    text-align: center;
}
```

---

### `static/script.js` (JavaScript)
```javascript
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const resultDiv = document.getElementById('result');

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `
                <p style="color: green;">${data.message}</p>
                <img src="/static/uploads/${data.filename}" alt="Avatar" width="200">
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `<p style="color: red;">An error occurred: ${error.message}</p>`;
    });
});
```

---

### Notes:
- The application includes a simple frontend form for uploading images.
- The backend validates file types and limits file uploads to 5MB.
- Proper error handling is implemented for file uploads and unsupported formats.
- This application is ready to deploy, but remember to add security measures like HTTPS, authentication, and rate limiting for production use.
