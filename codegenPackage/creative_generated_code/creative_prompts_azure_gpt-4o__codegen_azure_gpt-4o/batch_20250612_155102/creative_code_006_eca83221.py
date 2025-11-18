"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Create a Flask application that replicates the Monad Echo Awards nomination process, including fields for candidate posts, category selection, and Discord username submission.
Generated: DETERMINISTIC_eca83221f426f3b9
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)

# Secret key for session management (Flash messages)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Replace with a secure key in production

# Categories for Monad Echo Awards
CATEGORIES = [
    "Best Technical Post",
    "Most Inspirational Post",
    "Best Community Contribution",
    "Best Tutorial",
    "Best Design",
]

# In-memory storage for nominations (for demonstration purposes)
# Replace with a database in a production environment
nominations = []


@app.route("/")
def index():
    """
    Home page displaying the nomination form.
    """
    return render_template("index.html", categories=CATEGORIES)


@app.route("/nominate", methods=["POST"])
def nominate():
    """
    Handle nomination submission.
    """
    try:
        # Retrieve form data
        candidate_post = request.form.get("candidate_post")
        category = request.form.get("category")
        discord_username = request.form.get("discord_username")

        # Validate form data
        if not candidate_post or not category or not discord_username:
            flash("All fields are required.", "error")
            return redirect(url_for("index"))

        if category not in CATEGORIES:
            flash("Invalid category selected.", "error")
            return redirect(url_for("index"))

        # Save nomination (in-memory for simplicity)
        nomination = {
            "candidate_post": candidate_post,
            "category": category,
            "discord_username": discord_username,
        }
        nominations.append(nomination)

        flash("Nomination submitted successfully!", "success")
        return redirect(url_for("index"))
    except HTTPException as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("index"))
    except Exception as e:
        flash(f"Unexpected error: {str(e)}", "error")
        return redirect(url_for("index"))


@app.route("/nominations")
def view_nominations():
    """
    View all submitted nominations.
    """
    return render_template("nominations.html", nominations=nominations)


# Error handling for 404 and general exceptions
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return render_template("404.html"), 404


@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle unexpected exceptions.
    """
    return render_template("error.html", error=str(e)), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### Templates:

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monad Echo Awards - Nomination</title>
</head>
<body>
    <h1>Monad Echo Awards - Nomination Form</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('nominate') }}">
        <label for="candidate_post">Candidate Post URL:</label><br>
        <input type="url" id="candidate_post" name="candidate_post" required><br><br>
        
        <label for="category">Category:</label><br>
        <select id="category" name="category" required>
            {% for category in categories %}
            <option value="{{ category }}">{{ category }}</option>
            {% endfor %}
        </select><br><br>
        
        <label for="discord_username">Your Discord Username:</label><br>
        <input type="text" id="discord_username" name="discord_username" required><br><br>
        
        <button type="submit">Submit Nomination</button>
    </form>
</body>
</html>
```

#### `templates/nominations.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monad Echo Awards - Nominations</title>
</head>
<body>
    <h1>Submitted Nominations</h1>
    <ul>
        {% for nomination in nominations %}
        <li>
            <strong>Post:</strong> {{ nomination.candidate_post }}<br>
            <strong>Category:</strong> {{ nomination.category }}<br>
            <strong>Submitted by:</strong> {{ nomination.discord_username }}
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Nomination Form</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

#### `templates/error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error }}</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```
