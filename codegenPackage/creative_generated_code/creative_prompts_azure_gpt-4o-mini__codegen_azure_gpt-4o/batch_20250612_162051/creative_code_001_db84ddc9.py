"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Write a code snippet for a web form that allows users to register and post free ads on Ifesty.
Generated: DETERMINISTIC_db84ddc98a68386b
Batch ID: 20250612_162051
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

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# In-memory storage for simplicity (not suitable for production)
users = {}
ads = []

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions and display error messages."""
    return f"<h1>Error {e.code}</h1><p>{e.description}</p>", e.code

@app.route('/')
def home():
    """Home page displaying all ads."""
    return render_template('home.html', ads=ads)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Input validation
        if not username or not password:
            flash('Username and password are required!', 'danger')
            return redirect(url_for('register'))
        
        if username in users:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Register the user
        users[username] = password
        flash('Registration successful! Please log in to post ads.', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/post-ad', methods=['GET', 'POST'])
def post_ad():
    """Page for posting an ad."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        ad_title = request.form.get('title')
        ad_description = request.form.get('description')
        
        # Validate user credentials
        if username not in users or users[username] != password:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('post_ad'))
        
        # Validate ad details
        if not ad_title or not ad_description:
            flash('Ad title and description are required!', 'danger')
            return redirect(url_for('post_ad'))
        
        # Add ad to the list
        ads.append({
            'username': username,
            'title': ad_title,
            'description': ad_description,
        })
        flash('Ad posted successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('post_ad.html')

# HTML templates (home.html, register.html, post_ad.html) should be created in the "templates" directory.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Directory Structure:
```
/project-directory
    /templates
        home.html
        register.html
        post_ad.html
```

### Example `home.html` Template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Ifesty - Ads</title>
</head>
<body>
    <h1>Welcome to Ifesty</h1>
    <a href="/register">Register</a>
    <a href="/post-ad">Post an Ad</a>
    <h2>Ads:</h2>
    <ul>
        {% for ad in ads %}
            <li><strong>{{ ad.title }}</strong>: {{ ad.description }} (Posted by: {{ ad.username }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Example `register.html` Template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register - Ifesty</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Example `post_ad.html` Template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Post an Ad - Ifesty</title>
</head>
<body>
    <h1>Post an Ad</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="title">Ad Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Ad Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Post Ad</button>
    </form>
</body>
</html>
```
