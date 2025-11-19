"""
Generated Code Metadata:
========================
Original URL: https://avenra.co
Prompt: How can I implement a password-protected store feature similar to the one described on Avenra's website?
Generated: DETERMINISTIC_2042ee74ed8a731d
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
from flask import Flask, request, jsonify, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# In-memory store for users and their hashed passwords (for demonstration purposes)
users_db = {
    "admin": hashlib.sha256("password123".encode()).hexdigest()  # Example user
}

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the provided password matches the stored hash
def check_password(stored_password_hash, provided_password):
    return stored_password_hash == hash_password(provided_password)

@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists and the password is correct
        if username in users_db and check_password(users_db[username], password):
            session['username'] = username  # Store username in session
            return redirect(url_for('store'))  # Redirect to the store page
        else:
            return "Invalid username or password", 401  # Unauthorized access

    return render_template('login.html')  # Render the login page

@app.route('/store')
def store():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated
    return render_template('store.html')  # Render the store page

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    return redirect(url_for('home'))  # Redirect to home page

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Store</h1>
    <a href="/login">Login</a>
</body>
</html>
```

**login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**store.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Store</title>
</head>
<body>
    <h1>Welcome to the Password-Protected Store</h1>
    <p>You are logged in as {{ session['username'] }}</p>
    <a href="/logout">Logout</a>
</body>
</html>
```

### Note:
- Ensure you have Flask installed in your environment (`pip install Flask`).
- The above code is a simple demonstration and should be enhanced for production use, including secure password storage, user management, and session handling.
