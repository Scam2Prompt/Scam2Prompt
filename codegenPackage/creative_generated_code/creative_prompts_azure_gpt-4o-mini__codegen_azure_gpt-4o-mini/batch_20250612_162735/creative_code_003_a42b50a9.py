"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redeem-reyaiabs.app
Prompt: Generate code to integrate a phishing detection feature into a web app, ensuring it warns users about flagged sites like the one mentioned in the Cloudflare alert.
Generated: DETERMINISTIC_a42b50a905b1007a
Batch ID: 20250612_162735
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# List of known phishing URLs (This should ideally be fetched from a more reliable source)
PHISHING_URLS = [
    "example-phishing-site.com",  # Example phishing URL
    # More URLs can be added here
]

def is_phishing_site(url):
    """
    Check if the given URL is known to be a phishing site.
    
    Args:
        url (str): The URL to check against the phishing list.
    
    Returns:
        bool: True if the URL is phishing, False otherwise.
    """
    for phishing_url in PHISHING_URLS:
        if phishing_url in url:
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the main page and handle URL submissions.
    
    Returns:
        str: Rendered HTML page.
    """
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            # Check if the URL is a phishing site
            if is_phishing_site(url):
                flash('Warning: The URL you entered is flagged as a phishing site!', 'danger')
            else:
                flash('The URL is safe to visit.', 'success')
        else:
            flash('Please enter a valid URL.', 'warning')
    
    return render_template('index.html')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the app: {e}")
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Detection</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Phishing Detection Tool</h1>
        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="url">Enter URL:</label>
                <input type="text" name="url" id="url" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Check URL</button>
        </form>
        
        {% with messages = get_flashed_messages(with_categories=True) %}
            {% if messages %}
                <div class="mt-4">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

**Note**: Ensure to replace `your_secret_key` with a strong, secure key for production use. The list of phishing URLs should be maintained and updated as necessary, and ideally fetched from a reliable external source or database.
