"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Create a script that redirects users to an alternative webpage if JavaScript is disabled, inspired by the functionality mentioned on https://getin.co.il.
Generated: DETERMINISTIC_e865cdcc238f6467
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Redirect</title>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/no-js">
    </noscript>
</head>
<body>
    <h1>Welcome to our website!</h1>
    <script>
        // Check if JavaScript is enabled
        const jsEnabled = () => {
            try {
                return navigator.userAgent.toString().indexOf('Headless') === -1;
            } catch (e) {
                console.error('Error checking user agent:', e);
                return true; // Assume JS is enabled if error occurs
            }
        };

        // Redirect to alternative page if JavaScript is disabled
        if (!jsEnabled()) {
            window.location.href = '/no-js';
        }
    </script>
</body>
</html>
```

```html
<!-- no-js.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No JavaScript</title>
</head>
<body>
    <h1>JavaScript is disabled.</h1>
    <p>Please enable JavaScript to use our website.</p>
</body>
</html>
```

```python
# app.py (using Flask)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/no-js')
def no_js():
    return render_template('no-js.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt

Flask==2.2.2
```

```bash
# Run the application

# Create a new directory for the project
mkdir js-redirect

# Navigate into the project directory
cd js-redirect

# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a new directory for templates
mkdir templates

# Create index.html and no-js.html in the templates directory
# Copy the provided HTML code into their respective files

# Run the application
python app.py
```
