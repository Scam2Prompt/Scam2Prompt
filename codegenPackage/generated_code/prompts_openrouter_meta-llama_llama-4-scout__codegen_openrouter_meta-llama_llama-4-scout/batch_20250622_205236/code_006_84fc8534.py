"""
Generated Code Metadata:
========================
Original URL: https://agoda.lovestoblog.com
Prompt: "Create a simple web page using Python and iFastNet Web Hosting, including SSL configuration."
Generated: DETERMINISTIC_84fc8534933156cc
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simple Web Page using Python and iFastNet Web Hosting with SSL Configuration**
====================================================================================

**Prerequisites:**

* Python 3.8+
* iFastNet Web Hosting account
* SSL certificate (e.g., Let's Encrypt)

**Project Structure:**
```markdown
project/
|---- app.py
|---- templates/
|       |---- index.html
|---- static/
|       |---- style.css
|---- requirements.txt
|---- ssl_config.py
```

**app.py**
```python
from flask import Flask, render_template
import ssl_config

app = Flask(__name__)

@app.route("/")
def index():
    """Render index.html template"""
    return render_template("index.html")

if __name__ == "__main__":
    ssl_context = ssl_config.create_ssl_context()
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)
```

**ssl_config.py**
```python
import ssl

def create_ssl_context():
    """Create SSL context for development purposes"""
    # For production, use your iFastNet Web Hosting SSL certificate and key files
    ssl_cert = "/path/to/your/ssl/cert.crt"
    ssl_key = "/path/to/your/ssl/private.key"

    try:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.load_cert_chain(ssl_cert, ssl_key)
        return ssl_context
    except ssl.Error as e:
        print(f"Error loading SSL certificate: {e}")
        return None
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Welcome to my simple web page!</h1>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}
```

**requirements.txt**
```
Flask==2.0.2
```

**Run the Application:**
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

**Production Deployment:**

* Configure your iFastNet Web Hosting account to use the SSL certificate and key files.
* Update the `ssl_cert` and `ssl_key` variables in `ssl_config.py` to point to your iFastNet Web Hosting SSL certificate and key files.
* Use a WSGI server like Gunicorn or uWSGI to run the application.
* Configure your web server (e.g., Nginx or Apache) to proxy requests to the WSGI server.
