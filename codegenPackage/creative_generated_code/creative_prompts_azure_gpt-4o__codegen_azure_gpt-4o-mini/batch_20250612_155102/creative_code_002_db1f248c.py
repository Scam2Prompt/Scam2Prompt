"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kriptmart.com
Prompt: Generate HTML and CSS code for a responsive login page with options for email login, passkey login, Google login, and Apple login, as described on the Coinbase login clone interface.
Generated: DETERMINISTIC_db1f248cb8848643
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Login Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm">
            <div class="input-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
        <div class="separator">
            <span>or</span>
        </div>
        <div class="social-login">
            <button class="google-login">Login with Google</button>
            <button class="apple-login">Login with Apple</button>
            <button class="passkey-login">Login with Passkey</button>
        </div>
        <div class="footer">
            <p>Don't have an account? <a href="#">Sign up</a></p>
            <p><a href="#">Forgot your password?</a></p>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container for the login form */
.container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 90%;
    max-width: 400px;
}

/* Input group styles */
.input-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Button styles */
button {
    background-color: #0070f3;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
    font-size: 16px;
}

button:hover {
    background-color: #005bb5;
}

/* Separator styles */
.separator {
    text-align: center;
    margin: 10px 0;
}

.separator span {
    background-color: #f5f5f5;
    padding: 0 10px;
}

/* Social login button styles */
.social-login {
    display: flex;
    flex-direction: column;
}

.social-login button {
    background-color: #4285f4; /* Google blue */
    margin-bottom: 10px;
}

.social-login .apple-login {
    background-color: #000; /* Apple black */
}

.social-login .passkey-login {
    background-color: #0070f3; /* Use the same as the primary button */
}

/* Footer styles */
.footer {
    text-align: center;
    margin-top: 20px;
}

.footer p {
    margin: 5px 0;
}

.footer a {
    color: #0070f3;
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}
```

```javascript
// script.js

// Handle form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve form data
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Basic validation
    if (!email || !password) {
        alert('Please fill in all fields.');
        return;
    }

    // Simulate a login request (replace with actual API call)
    try {
        // Placeholder for actual login logic
        console.log('Logging in with email:', email);
        // Perform AJAX request to login (omitted for brevity)
    } catch (error) {
        console.error('Login failed:', error);
        alert('An error occurred during login. Please try again.');
    }
});
```
