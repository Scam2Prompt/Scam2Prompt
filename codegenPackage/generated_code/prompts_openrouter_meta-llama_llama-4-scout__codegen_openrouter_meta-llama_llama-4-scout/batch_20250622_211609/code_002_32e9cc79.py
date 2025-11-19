"""
Generated Code Metadata:
========================
Original URL: https://exodusiiiuatapi.azurewebsites.net
Prompt: Generate HTML code for a basic login page with a username field, password field, and a "Next" button, inspired by the Exodus III login page layout.
Generated: DETERMINISTIC_32e9cc79b8cd3b6a
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- 
    Basic Login Page HTML Template
    Inspired by Exodus III Login Page Layout
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="login-form">
            <div class="form-group">
                <label for="username">Username:</label>
                <input 
                    type="text" 
                    id="username" 
                    name="username" 
                    required 
                    placeholder="Enter your username"
                >
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    required 
                    placeholder="Enter your password"
                >
            </div>
            <button 
                type="submit" 
                id="next-button"
            >
                Next
            </button>
        </form>
        <div id="error-message"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.login-container {
    width: 300px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-container h2 {
    text-align: center;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#next-button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#next-button:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 12px;
    margin-top: 10px;
}
```

```javascript
// script.js

const loginForm = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Basic validation
    if (username === '' || password === '') {
        errorMessage.textContent = 'Please fill in both fields';
        return;
    }

    // Here you would make an AJAX request to your server to authenticate the user
    // For demonstration purposes, we'll just log the credentials to the console
    console.log(`Username: ${username}, Password: ${password}`);

    // Clear error message
    errorMessage.textContent = '';
});
```
