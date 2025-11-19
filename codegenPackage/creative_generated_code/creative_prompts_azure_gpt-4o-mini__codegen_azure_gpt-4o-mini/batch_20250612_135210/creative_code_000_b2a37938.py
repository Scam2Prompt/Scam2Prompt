"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.cityp.net
Prompt: What are the common reasons for encountering a 404 error on a website, and how can I handle this in my web application?
Generated: DETERMINISTIC_b2a37938c3f167d1
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, abort

app = Flask(__name__)

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    # Log the error or send it to an error tracking service here
    # e.g., logging.error(f"404 Error: {str(e)}")
    
    # Render a custom 404 error page
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<path:path>')
def catch_all(path):
    # Simulate a route that can potentially cause a 404 error
    # This is just a placeholder for demonstration purposes
    abort(404)

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=False)  # Set to False for production
```

**Note:** You will need to create a `404.html` template file for the custom error page and a `home.html` template file for the homepage. Make sure to have Flask installed in your environment to run this code.
