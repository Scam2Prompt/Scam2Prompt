"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Write Python code to create a form for enrolling in music lessons, including fields for selecting instruments like bass guitar, saxophone, or piano, as described on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_d60ae196863dcc34
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for flashing messages

# List of available instruments
INSTRUMENTS = ["Bass Guitar", "Saxophone", "Piano"]

@app.route("/", methods=["GET"])
def enrollment_form():
    """
    Render the music lesson enrollment form.
    """
    return render_template("form.html", instruments=INSTRUMENTS)

@app.route("/submit", methods=["POST"])
def submit_form():
    """
    Handle submission of the music lesson enrollment form.
    """
    try:
        # Extract form data
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        instrument = request.form.get("instrument")
        
        # Validate inputs
        if not name or not email or not age or instrument not in INSTRUMENTS:
            flash("Please fill out all required fields correctly.", "error")
            return redirect(url_for("enrollment_form"))
        
        # Process the enrollment (e.g., save to a database - omitted for simplicity)
        # For demonstration purposes, we'll just flash a success message
        flash(f"Thank you, {name}! You have successfully enrolled for {instrument} lessons.", "success")
        return redirect(url_for("enrollment_form"))
    except Exception as e:
        # Handle unexpected errors
        flash("An error occurred while processing your enrollment. Please try again later.", "error")
        return redirect(url_for("enrollment_form"))

# Entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)

```

### HTML Template (`templates/form.html`)
Save this file as `form.html` inside a `templates` folder in your project directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Lesson Enrollment</title>
</head>
<body>
    <h1>Enroll in Music Lessons</h1>

    <!-- Display flashed messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {{ 'red' if category == 'error' else 'green' }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" min="1" required><br><br>

        <label for="instrument">Select Instrument:</label>
        <select id="instrument" name="instrument" required>
            <option value="" disabled selected>Choose an instrument</option>
            {% for instrument in instruments %}
                <option value="{{ instrument }}">{{ instrument }}</option>
            {% endfor %}
        </select><br><br>

        <button type="submit">Enroll</button>
    </form>
</body>
</html>
```
