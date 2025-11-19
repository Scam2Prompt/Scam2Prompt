"""
Generated Code Metadata:
========================
Original URL: https://cpanel.consesys.io
Prompt: Create a responsive login form in HTML and CSS, including locale selection functionality, inspired by the cPanel login interface.
Generated: DETERMINISTIC_4accd7ddf4f19e7d
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Login Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form class="login-form" id="login-form">
            <div class="form-header">
                <h2>Login</h2>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="locale">Locale:</label>
                <select id="locale" name="locale">
                    <option value="en">English (en)</option>
                    <option value="fr">Français (fr)</option>
                    <option value="es">Español (es)</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
            <div class="form-footer">
                <p>Forgot Password? <a href="#">Reset</a></p>
            </div>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
:root {
    --primary-color: #3498db;
    --secondary-color: #f1f1f1;
    --border-color: #ddd;
    --text-color: #333;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    height: 100vh;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.login-container {
    background-color: #fff;
    padding: 20px;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

.login-form {
    display: flex;
    flex-direction: column;
}

.form-header {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 5px;
}

.form-group input, .form-group select {
    padding: 10px;
    border: 1px solid var(--border-color);
    border-radius: 5px;
}

.btn {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn-primary {
    background-color: var(--primary-color);
    color: #fff;
}

.btn-primary:hover {
    background-color: #2c3e50;
}

.form-footer {
    text-align: center;
    margin-top: 10px;
}

.form-footer a {
    text-decoration: none;
    color: var(--primary-color);
}

.form-footer a:hover {
    text-decoration: underline;
}

/* Responsive design */

@media (max-width: 768px) {
    .login-container {
        width: 90%;
    }
}

@media (max-width: 480px) {
    .login-container {
        padding: 10px;
    }
}
```

**script.js**
```javascript
const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const locale = document.getElementById('locale').value;

    // Add your login logic here
    console.log(`Username: ${username}, Password: ${password}, Locale: ${locale}`);
});
```
