"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Create a web application that includes a "Begin" button for a token-gated survey, with a timer feature that limits completion time to 3 minutes.
Generated: DETERMINISTIC_6444776131a632da
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py - A Flask-based web application for token-gated survey with timer functionality.

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management

# Token for gating the survey (replace with your actual method for handling tokens)
VALID_TOKEN = "12345"

# Global variables for survey timing
SURVEY_TIMEOUT = 180  # Survey time limit in seconds (3 minutes)


@app.route('/')
def index():
    """
    Render the main page with a 'Begin' button.
    """
    return render_template('index.html')


@app.route('/begin', methods=['POST'])
def begin_survey():
    """
    Start the survey if the token is valid.
    Stores the start time in the session for timeout handling.
    """
    token = request.form.get("token")
    if token == VALID_TOKEN:
        session['start_time'] = time.time()  # Record the time when the survey started
        return redirect(url_for('survey'))
    else:
        return render_template('index.html', error="Invalid token. Please try again.")


@app.route('/survey')
def survey():
    """
    Render the survey page and check for timeout.
    """
    start_time = session.get('start_time')
    if not start_time:
        return redirect(url_for('index'))

    elapsed_time = time.time() - start_time
    if elapsed_time > SURVEY_TIMEOUT:
        return render_template('timeout.html')  # Inform the user that the survey session has timed out

    remaining_time = max(SURVEY_TIMEOUT - elapsed_time, 0)
    return render_template('survey.html', remaining_time=int(remaining_time))


@app.route('/submit', methods=['POST'])
def submit_survey():
    """
    Handle survey submission and check for timeout before processing responses.
    """
    start_time = session.get('start_time')
    if not start_time:
        return redirect(url_for('index'))

    elapsed_time = time.time() - start_time
    if elapsed_time > SURVEY_TIMEOUT:
        return render_template('timeout.html')  # Inform the user that the survey session has timed out

    # Process the survey responses (dummy implementation)
    responses = request.form.to_dict()
    session.pop('start_time', None)  # Clear the session data
    return jsonify({"message": "Survey submitted successfully!", "responses": responses})


if __name__ == '__main__':
    app.run(debug=True)

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Token-Gated Survey</title>
</head>
<body>
    <h1>Welcome to the Survey</h1>
    <form action="/begin" method="POST">
        <label for="token">Enter Token:</label>
        <input type="text" id="token" name="token" required>
        <button type="submit">Begin</button>
    </form>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/survey.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survey</title>
</head>
<body>
    <h1>Survey</h1>
    <p>Remaining Time: <span id="remaining-time">{{ remaining_time }}</span> seconds</p>
    <form action="/submit" method="POST">
        <label for="question1">Question 1:</label>
        <input type="text" id="question1" name="question1" required><br>
        <label for="question2">Question 2:</label>
        <input type="text" id="question2" name="question2" required><br>
        <button type="submit">Submit</button>
    </form>

    <script>
        // Countdown timer functionality
        let remainingTime = Number(document.getElementById("remaining-time").innerText);
        const countdown = setInterval(() => {
            if (remainingTime <= 0) {
                clearInterval(countdown);
                alert("Time's up! Redirecting to timeout page...");
                window.location.href = "/survey"; // Redirect to timeout page
            } else {
                remainingTime -= 1;
                document.getElementById("remaining-time").innerText = remainingTime;
            }
        }, 1000);
    </script>
</body>
</html>
```

```html
<!-- templates/timeout.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survey Timeout</title>
</head>
<body>
    <h1>Survey Timeout</h1>
    <p>We’re sorry, but your time to complete the survey has expired.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```
