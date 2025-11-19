"""
Generated Code Metadata:
========================
Original URL: https://www.mirrorcommunity.com
Prompt: How can I implement a password protection feature for an online store similar to the Mirror Mirror Community?
Generated: DETERMINISTIC_5badb6768d17654d
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import secrets
from functools import wraps
from flask import Flask, request, redirect, url_for, session, flash, render_template

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Secure secret key for session management

# Database simulation (in production, use a real database)
users_db = {
    "admin": {
        "password_hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # sha256 of "password"
        "salt": "random_salt_value"
    }
}

def hash_password(password, salt=None):
    """Hash password with salt using SHA-256"""
    if salt is None:
        salt = secrets.token_hex(16)
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest(), salt

def login_required(f):
    """Decorator to ensure user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to access this page.')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('login'))
        
        user = users_db.get(username)
        if not user:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        
        hashed_password, _ = hash_password(password, user['salt'])
        if hashed_password != user['password_hash']:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        
        session['username'] = username
        flash('Logged in successfully!')
        
        next_page = request.args.get('next')
        return redirect(next_page or url_for('protected_page'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/protected')
@login_required
def protected_page():
    return render_template('protected.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match.')
            return redirect(url_for('register'))
        
        if username in users_db:
            flash('Username already exists.')
            return redirect(url_for('register'))
        
        password_hash, salt = hash_password(password)
        users_db[username] = {
            'password_hash': password_hash,
            'salt': salt
        }
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # For development only, use proper SSL in production
```

```html
<!-- templates/login.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('login') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

```html
<!-- templates/register.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('register') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required><br>
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{{ url_for('login') }}">Login</a></p>
</body>
</html>
```

```html
<!-- templates/protected.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Protected Page</title>
</head>
<body>
    <h1>Welcome, {{ session.username }}!</h1>
    <p>This is a protected page.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to our Store</h1>
    {% if 'username' in session %}
        <p>Hello, {{ session.username }}! <a href="{{ url_for('logout') }}">Logout</a></p>
        <p><a href="{{ url_for('protected_page') }}">Go to protected page</a></p>
    {% else %}
        <p><a href="{{ url_for('login') }}">Login</a> or <a href="{{ url_for('register') }}">Register</a></p>
    {% endif %}
</body>
</html>
```
