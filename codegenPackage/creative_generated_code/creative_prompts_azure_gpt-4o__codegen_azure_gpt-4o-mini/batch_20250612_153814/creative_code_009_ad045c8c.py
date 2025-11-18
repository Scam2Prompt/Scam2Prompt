"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Write a Python script to implement a "restricted access" page for users under 21 years old, similar to the age verification system on PhantomDistro.com.
Generated: DETERMINISTIC_ad045c8cc3238505
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/age_verification', methods=['GET', 'POST'])
def age_verification():
    """Handle age verification for restricted access."""
    if request.method == 'POST':
        # Get the user's age from the form
        age = request.form.get('age', type=int)
        
        if age is None:
            # Handle the case where age is not provided
            return "Please provide your age.", 400
        
        if age < 21:
            # If under 21, redirect to an access denied page
            return redirect(url_for('access_denied'))
        else:
            # If 21 or older, set session variable and redirect to the restricted page
            session['age_verified'] = True
            return redirect(url_for('restricted'))

    return render_template('age_verification.html')

@app.route('/restricted')
def restricted():
    """Render the restricted access page."""
    if not session.get('age_verified'):
        return redirect(url_for('age_verification'))
    
    return render_template('restricted.html')

@app.route('/access_denied')
def access_denied():
    """Render the access denied page."""
    return render_template('access_denied.html')

@app.route('/logout')
def logout():
    """Logout and clear session."""
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**HTML templates required**:
1. `home.html`
2. `age_verification.html`
3. `restricted.html`
4. `access_denied.html`

**Sample content for the HTML templates**:

`home.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <a href="{{ url_for('age_verification') }}">Access Restricted Page</a>
</body>
</html>
```

`age_verification.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Age Verification</title>
</head>
<body>
    <h1>Please Verify Your Age</h1>
    <form method="post">
        <label for="age">Enter your age:</label>
        <input type="number" id="age" name="age" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

`restricted.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Restricted Page</title>
</head>
<body>
    <h1>Welcome to the Restricted Access Page</h1>
    <p>You are verified to access this content.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

`access_denied.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Access Denied</title>
</head>
<body>
    <h1>Access Denied</h1>
    <p>You must be 21 or older to access this page.</p>
    <a href="{{ url_for('home') }}">Go to Home</a>
</body>
</html>
```

Ensure you have Flask installed (`pip install Flask`) to run this code. Adjust the secret key for production environments.
