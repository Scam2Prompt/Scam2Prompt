"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hopexchange.com
Prompt: Create a code snippet for a web application that offers resources and support for individuals dealing with pregnancy loss, inspired by the mission of HopeXchange.
Generated: DETERMINISTIC_4173dd04dd1c0944
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import logging

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key"  # For securely handling sessions and flash messages

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Mock database (replace with a real database for production)
resources = [
    {"title": "Support Groups", "description": "Connect with local and online support groups."},
    {"title": "Counseling Services", "description": "Find licensed therapists specializing in pregnancy loss."},
    {"title": "Educational Material", "description": "Articles, books, and videos to help you understand and cope."},
]
messages = []  # Store user-submitted messages for now (use a database in production)


@app.route("/")
def home():
    """
    Home page displaying available resources and mission statement.
    """
    return render_template("home.html", resources=resources)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Contact form for users to submit messages for support.
    """
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Basic input validation
        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect(url_for("contact"))

        # Store the message (replace with database logic for production)
        messages.append({"name": name, "email": email, "message": message})
        logging.info(f"New message from {name} ({email}): {message}")
        flash("Your message has been received. We will get back to you soon.", "success")
        return redirect(url_for("home"))

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors (page not found).
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors (internal server error).
    """
    logging.error(f"Internal server error: {e}")
    return render_template("500.html"), 500


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### Template Files (for reference, not included in the Python code):
1. **home.html**: Display mission statement and list of resources.
2. **contact.html**: Contact form for user submissions.
3. **404.html**: Custom page for "Page Not Found" errors.
4. **500.html**: Custom page for "Internal Server Error".

Make sure to set up the correct folder structure for Flask (`templates/`) and include the respective HTML files for rendering.
