"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Develop a web form for guests to submit their preferences for a personalized stay at Chalet Roc Remi, including options for workshops and culinary experiences.
Generated: DETERMINISTIC_2a13ed26b242fa5c
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Flask application to create a web form for guests to submit their preferences
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Route to display the form
@app.route('/', methods=['GET', 'POST'])
def guest_preferences():
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.form.get('name')
            email = request.form.get('email')
            stay_dates = request.form.get('stay_dates')
            workshops = request.form.getlist('workshops')  # Multiple selections
            culinary_experiences = request.form.getlist('culinary_experiences')  # Multiple selections
            special_requests = request.form.get('special_requests')

            # Validate required fields
            if not name or not email or not stay_dates:
                flash('Name, Email, and Stay Dates are required.', 'error')
                return redirect(url_for('guest_preferences'))

            # Process the data (e.g., save to a database or send an email)
            # For demonstration, we'll just flash a success message
            flash('Preferences submitted successfully!', 'success')
            return redirect(url_for('guest_preferences'))

        except HTTPException as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('guest_preferences'))

    # Render the form template
    return render_template('guest_preferences.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- guest_preferences.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chalet Roc Remi - Guest Preferences</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Personalized Stay Preferences</h1>
        <form method="POST" action="/">
            <!-- Name -->
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>

            <!-- Email -->
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>

            <!-- Stay Dates -->
            <div class="mb-3">
                <label for="stay_dates" class="form-label">Stay Dates</label>
                <input type="text" class="form-control" id="stay_dates" name="stay_dates" placeholder="e.g., 2023-12-01 to 2023-12-07" required>
            </div>

            <!-- Workshops -->
            <div class="mb-3">
                <label class="form-label">Workshops</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="workshops" value="Yoga">
                    <label class="form-check-label">Yoga</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="workshops" value="Painting">
                    <label class="form-check-label">Painting</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="workshops" value="Photography">
                    <label class="form-check-label">Photography</label>
                </div>
            </div>

            <!-- Culinary Experiences -->
            <div class="mb-3">
                <label class="form-label">Culinary Experiences</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="culinary_experiences" value="Wine Tasting">
                    <label class="form-check-label">Wine Tasting</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="culinary_experiences" value="Cooking Class">
                    <label class="form-check-label">Cooking Class</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="culinary_experiences" value="Local Cuisine Tour">
                    <label class="form-check-label">Local Cuisine Tour</label>
                </div>
            </div>

            <!-- Special Requests -->
            <div class="mb-3">
                <label for="special_requests" class="form-label">Special Requests</label>
                <textarea class="form-control" id="special_requests" name="special_requests" rows="3"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit" class="btn btn-primary">Submit Preferences</button>
        </form>

        <!-- Flash Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-3">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}" role="alert">
                {{ message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go back to the home page</a>
</body>
</html>
```

```html
<!-- 500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end.</p>
    <a href="/">Go back to the home page</a>
</body>
</html>
```
