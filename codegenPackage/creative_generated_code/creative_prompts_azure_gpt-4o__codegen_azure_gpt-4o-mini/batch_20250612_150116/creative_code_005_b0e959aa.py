"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Write code to implement a "Live Preview" feature for e-books, allowing users to read sample pages before subscribing, as seen on Digielearning.
Generated: DETERMINISTIC_b0e959aa17319271
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)

# Sample e-book data (In production, this would likely come from a database)
EBOOKS = {
    1: {'title': 'E-Book One', 'sample_path': 'samples/sample1.pdf'},
    2: {'title': 'E-Book Two', 'sample_path': 'samples/sample2.pdf'},
    # Add more e-books as needed
}

@app.route('/')
def index():
    """Render the home page with a list of available e-books"""
    return render_template('index.html', ebooks=EBOOKS)

@app.route('/preview/<int:ebook_id>', methods=['GET'])
def preview(ebook_id):
    """Serve the sample PDF for the specified e-book ID.

    Args:
        ebook_id (int): The ID of the e-book to preview.

    Returns:
        Response: The sample PDF file if found, else an error message.
    """
    ebook = EBOOKS.get(ebook_id)

    if not ebook:
        return jsonify({'error': 'E-book not found'}), 404

    sample_path = ebook['sample_path']
    
    # Check if the sample file exists
    if not os.path.exists(sample_path):
        return jsonify({'error': 'Sample file not found'}), 404

    return send_file(sample_path, as_attachment=False)

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Book Preview</title>
</head>
<body>
    <h1>E-Book Library</h1>
    <ul>
        {% for id, ebook in ebooks.items() %}
            <li>
                <strong>{{ ebook.title }}</strong>
                <a href="/preview/{{ id }}">Preview</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Directory Structure
```
/your_project_directory
│
├── app.py               # Main Flask application
├── samples              # Directory containing sample e-books
│   ├── sample1.pdf
│   └── sample2.pdf
└── templates            # Directory for HTML templates
    └── index.html
```

### Notes
- Ensure you have Flask installed (`pip install Flask`).
- Store your sample e-books in the `samples` directory.
- Update `EBOOKS` with the correct paths to your sample files.
- This implementation assumes a basic directory structure. Adjust paths as necessary for your project setup.
