"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: What are the best practices for organizing files in a web server's index directory?
Generated: DETERMINISTIC_17f5537e9a76ebb9
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Constants for directory structure
INDEX_DIR = 'index'
ASSETS_DIR = os.path.join(INDEX_DIR, 'assets')
HTML_DIR = os.path.join(INDEX_DIR, 'html')
CSS_DIR = os.path.join(ASSETS_DIR, 'css')
JS_DIR = os.path.join(ASSETS_DIR, 'js')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')

# Helper function to create directory structure
def create_directories():
    """
    Create the necessary directory structure for the web server's index directory.
    This includes the assets, html, css, js, and images directories.
    """
    directories = [INDEX_DIR, ASSETS_DIR, HTML_DIR, CSS_DIR, JS_DIR, IMAGES_DIR]
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory created: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

# Route to list the structure of the index directory
@app.route('/directory-structure', methods=['GET'])
def directory_structure():
    """
    API endpoint to return the structure of the index directory.
    
    Returns:
        JSON: A representation of the directory structure.
    """
    try:
        structure = {
            'index': {
                'assets': {
                    'css': [],
                    'js': [],
                    'images': []
                },
                'html': []
            }
        }
        return jsonify(structure), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    create_directories()  # Create directories when the application starts
    app.run(host='0.0.0.0', port=5000)  # Start the Flask web server
```
