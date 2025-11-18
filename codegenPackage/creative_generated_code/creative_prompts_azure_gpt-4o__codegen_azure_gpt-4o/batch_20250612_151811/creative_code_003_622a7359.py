"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aaaverify.claimsdetective.com
Prompt: Create a secure web portal for clients to upload biographical files for verification, incorporating features inspired by AAAVerify.com's client portal.
Generated: DETERMINISTIC_622a735939d0f71d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for creating a secure web portal using Python's Flask framework. The portal allows clients to upload biographical files for verification. It incorporates file upload security measures, user authentication, and documentation.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for the app
app.secret_key = 'your_secret_key_here'  # Replace with a secure, randomly generated key
UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}  # Allowed file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Mock user database (replace with actual database in production)
USER_DATABASE = {
    'client1': 'password123',
    'client2': 'securepass'
}

# Utility function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate user
        if username in USER_DATABASE and USER_DATABASE[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('upload'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

# Route: Logout functionality
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

# Route: File upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Check if user is logged in
    if 'user' not in session:
        flash('You need to log in to access this page.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Check if the file is present in the request
        if 'file' not in request.files:
            flash('No file part in the request.', 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if a file is selected
        if file.filename == '':
            flash('No file selected.', 'danger')
            return redirect(request.url)
        
        # Validate file type and save securely
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Sanitize filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash(f'File "{filename}" uploaded successfully!', 'success')
            return redirect(url_for('upload'))
        else:
            flash('Invalid file type. Allowed types are: txt, pdf, docx.', 'danger')
    
    return render_template('upload.html')

# Route: Display uploaded files for verification (mock functionality)
@app.route('/files')
def view_files():
    # Check if user is logged in
    if 'user' not in session:
        flash('You need to log in to access this page.', 'warning')
        return redirect(url_for('login'))
    
    # Fetch list of uploaded files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('files.html', files=files)

# Error handling: Handle request size errors
@app.errorhandler(413)
def file_too_large(error):
    flash('File is too large. Maximum allowed size is 16 MB.', 'danger')
    return redirect(url_for('upload'))

# Templates (HTML files):
# Note: Save these HTML files in a "templates" folder.
# index.html, login.html, upload.html, files.html (simplified examples)

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `your_secret_key_here` with a securely generated key for production.
2. Implement actual database integration for users instead of the mock `USER_DATABASE`.
3. Use HTTPS in production to ensure secure communication.
4. Customize templates to fit your design and branding needs.
