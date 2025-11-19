"""
Generated Code Metadata:
========================
Original URL: https://tojsat.net
Prompt: Create a REST API endpoint that allows users to submit their research articles to an open-access journal, incorporating features similar to those found in TOJSAT's submission guidelines.
Generated: DETERMINISTIC_9250983049b7e65e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submit-article', methods=['POST'])
def submit_article():
    """
    Endpoint to submit a research article.
    Users must provide:
    - 'title': Title of the article
    - 'author': Author's name
    - 'email': Author's email
    - 'file': The article file (PDF, DOC, or DOCX)
    """
    try:
        # Validate required fields
        title = request.form.get('title')
        author = request.form.get('author')
        email = request.form.get('email')
        file = request.files.get('file')

        if not title or not author or not email or not file:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate file type
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Allowed types are: PDF, DOC, DOCX"}), 400

        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Simulate saving metadata to a database (replace with actual DB logic)
        article_metadata = {
            "title": title,
            "author": author,
            "email": email,
            "file_path": file_path
        }

        # Return success response
        return jsonify({
            "message": "Article submitted successfully",
            "article_metadata": article_metadata
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
