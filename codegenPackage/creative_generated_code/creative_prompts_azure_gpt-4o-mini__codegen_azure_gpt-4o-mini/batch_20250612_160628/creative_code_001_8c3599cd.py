"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartcats.vip
Prompt: Write a Python script that generates a registration form for an educational program, incorporating features that empower children's creativity as described on the Cats, Cats, Cats, and Lasagna website.
Generated: DETERMINISTIC_8c3599cd4bc6b92d
Batch ID: 20250612_160628
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
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
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key for production

# Registration form route
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        age = request.form.get('age')
        creativity = request.form.get('creativity')
        
        # Validate input data
        if not name or not age or not creativity:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        try:
            age = int(age)
            if age < 5 or age > 18:
                flash('Age must be between 5 and 18 years.', 'error')
                return redirect(url_for('register'))
        except ValueError:
            flash('Age must be a number!', 'error')
            return redirect(url_for('register'))
        
        # Here we would typically save the data to a database or file.
        # For simplicity, we'll just flash a success message.
        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('registration_form.html')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**Template: registration_form.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Registration Form</h1>
        
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="alert alert-info mt-3">
                    {{ messages[0] }}
                </div>
            {% endif %}
        {% endwith %}
        
        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="name">Child's Name:</label>
                <input type="text" id="name" name="name" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" class="form-control" required min="5" max="18">
            </div>
            <div class="form-group">
                <label for="creativity">Creative Interests:</label>
                <textarea id="creativity" name="creativity" class="form-control" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</body>
</html>
```

**Instructions to Run:**
1. Make sure you have Flask installed: `pip install Flask`.
2. Save the Python code in a file named `app.py`.
3. Save the HTML code in a folder named `templates` as `registration_form.html`.
4. Run the Flask application with the command: `python app.py`.
5. Open your web browser and navigate to `http://127.0.0.1:5000/` to see the registration form.
