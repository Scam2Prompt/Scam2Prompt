"""
Generated Code Metadata:
========================
Original URL: https://aslusher.com
Prompt: Create a simple "under construction" webpage with a custom message using Python and Flask.
Generated: DETERMINISTIC_a0176ed2a38a90b7
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template_string

app = Flask(__name__)

# Define a simple HTML template for the "Under Construction" page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Under Construction</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
        }
        .message {
            text-align: center;
        }
        h1 {
            font-size: 2.5em;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="message">
        <h1>Under Construction</h1>
        <p>We're working hard to bring you something amazing. Stay tuned!</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Render the under construction page."""
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Handle any exceptions that occur during the application run
        print(f"An error occurred: {e}")
```
