"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrolly-claim.xyz
Prompt: Can you provide code examples for handling website downtime gracefully in a web application?
Generated: DETERMINISTIC_9c684d6eb4ed2b05
Batch ID: 20250612_155555
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Example 1: Handling Website Downtime Gracefully with a Maintenance Page (using Python and Flask)

```python
from flask import Flask, render_template

app = Flask(__name__)

# Flag to enable/disable maintenance mode
MAINTENANCE_MODE = True

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the website is in maintenance mode.
    Redirects all requests to the maintenance page if enabled.
    """
    if MAINTENANCE_MODE:
        return render_template("maintenance.html"), 503  # HTTP status code 503 indicates service unavailable.

@app.route("/")
def home():
    """
    Main home route of the website.
    Only accessible when maintenance mode is OFF.
    """
    return "Welcome to the website!"

@app.route("/about")
def about():
    """
    Example route for an 'About' page.
    """
    return "This is the about page!"

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

**Template for `maintenance.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Maintenance</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>We’ll be back soon!</h1>
    <p>Our website is currently undergoing maintenance. Please check back later.</p>
</body>
</html>
```

---

### Example 2: Using Middleware for Downtime Handling (Node.js and Express)

```javascript
const express = require('express');
const app = express();

// Flag to enable/disable maintenance mode
const MAINTENANCE_MODE = true;

// Middleware for checking maintenance mode
app.use((req, res, next) => {
    if (MAINTENANCE_MODE) {
        // Send a maintenance response with status code 503
        res.status(503).send(`
            <html>
                <head><title>Maintenance</title></head>
                <body>
                    <h1>We’ll be back soon!</h1>
                    <p>Our website is currently undergoing maintenance. Please check back later.</p>
                </body>
            </html>
        `);
    } else {
        next(); // Continue if maintenance mode is disabled
    }
});

// Route handlers
app.get('/', (req, res) => {
    res.send('Welcome to the website!');
});

app.get('/about', (req, res) => {
    res.send('This is the about page!');
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

---

### Example 3: Graceful Downtime Handling with a Custom Error Page (Django)

1. **Modify settings.py:**

```python
# settings.py
MAINTENANCE_MODE = True  # Flag to enable/disable maintenance mode
```

2. **Create middleware:**

```python
# middleware.py
from django.http import HttpResponse
from django.conf import settings

def maintenance_mode_middleware(get_response):
    """
    Middleware to handle maintenance mode. Redirects all requests to a custom maintenance page if enabled.
    """
    def middleware(request):
        if getattr(settings, "MAINTENANCE_MODE", False):  # Check if maintenance mode is enabled
            return HttpResponse("""
                <html>
                    <head><title>Maintenance</title></head>
                    <body>
                        <h1>We’ll be back soon!</h1>
                        <p>Our website is currently undergoing maintenance. Please check back later.</p>
                    </body>
                </html>
            """, status=503)
        return get_response(request)

    return middleware
```

3. **Enable middleware in `settings.py`:**

```python
MIDDLEWARE = [
    # Other middleware...
    'your_app.middleware.maintenance_mode_middleware',  # Add the custom maintenance middleware
]
```

4. **Create some example views:**

```python
# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the website!")

def about(request):
    return HttpResponse("This is the about page!")
```

5. **Configure URLs:**

```python
# urls.py
from django.urls import path
from your_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

These examples demonstrate how to gracefully handle website downtime across different web frameworks.
