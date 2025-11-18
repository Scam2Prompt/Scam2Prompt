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
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Form for the token-gated survey
class SurveyForm(FlaskForm):
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Begin')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = SurveyForm()
    if form.validate_on_submit():
        token = form.token.data
        # Validate token (placeholder for actual token validation logic)
        if token == 'valid_token':  # Replace with actual token validation
            session['start_time'] = time.time()
            return redirect(url_for('survey'))
        else:
            flash('Invalid token. Please try again.', 'danger')
    return render_template('home.html', form=form)

# Route for the survey page
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    # Check if the survey is still active based on time
    if 'start_time' not in session:
        flash('Session expired or not started. Please begin again.', 'danger')
        return redirect(url_for('home'))
    
    elapsed_time = time.time() - session['start_time']
    if elapsed_time > 180:  # 180 seconds = 3 minutes
        flash('Time is up! Submission is no longer allowed.', 'danger')
        session.pop('start_time', None)
        return redirect(url_for('home'))
    
    # Render survey (placeholder for survey content)
    return render_template('survey.html', remaining_time=180 - int(elapsed_time))

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production

```

```html
<!-- templates/home.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Token-Gated Survey</title>
</head>
<body>
    <h1>Welcome to the Token-Gated Survey</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.token.label }} {{ form.token(size=32) }}<br>
        {{ form.submit() }}
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- templates/survey.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survey</title>
    <script>
        // Countdown timer for the survey
        let remainingTime = {{ remaining_time }};
        function startTimer() {
            const timerElement = document.getElementById('timer');
            const interval = setInterval(() => {
                if (remainingTime <= 0) {
                    clearInterval(interval);
                    alert('Time is up! Please submit your responses.');
                    window.location.href = '/'; // Redirect to home
                } else {
                    timerElement.textContent = remainingTime + ' seconds remaining';
                    remainingTime--;
                }
            }, 1000);
        }
        window.onload = startTimer;
    </script>
</head>
<body>
    <h1>Survey</h1>
    <p id="timer"></p>
    <p>Please answer the following questions...</p>
    <!-- Placeholder for survey questions -->
    <form method="POST">
        <!-- Add survey questions here -->
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
