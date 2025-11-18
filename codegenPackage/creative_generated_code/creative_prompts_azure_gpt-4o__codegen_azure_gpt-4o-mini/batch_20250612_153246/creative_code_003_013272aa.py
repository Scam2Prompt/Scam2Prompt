"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Generate HTML and JavaScript code for a login page with "Remember Password" and "Forgot Password" options, inspired by the HBsoft login interface.
Generated: DETERMINISTIC_013272aaad602972
Batch ID: 20250612_153246
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
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <input type="checkbox" id="rememberMe" name="rememberMe">
                <label for="rememberMe">Remember Password</label>
            </div>
            <button type="submit">Login</button>
        </form>
        <div class="links">
            <a href="#" id="forgotPassword">Forgot Password?</a>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
body, h1, p {
    margin: 0;
    padding: 0;
}

/* Styling for the login container */
.login-container {
    width: 300px;
    margin: 100px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Styling for the form groups */
.form-group {
    margin-bottom: 15px;
}

/* Button styling */
button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

/* Link styling */
.links {
    text-align: center;
    margin-top: 15px;
}

.links a {
    text-decoration: none;
    color: #007BFF;
}

.links a:hover {
    text-decoration: underline;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Capture form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('rememberMe').checked;

    // Simple validation
    if (!username || !password) {
        alert('Please fill in all fields.');
        return;
    }

    // Simulate server login process
    login(username, password, rememberMe);
});

// Simulated login function
function login(username, password, rememberMe) {
    // Here you would typically make a request to your server
    // For demonstration, we simulate a successful login
    console.log('Logging in with:', username, password, rememberMe);

    // Simulate storing credentials if "Remember Password" is checked
    if (rememberMe) {
        localStorage.setItem('username', username);
        localStorage.setItem('password', password); // Warning: Storing passwords is not secure!
    }
    
    alert('Login successful!'); // Simulated success message
}

// Handle "Forgot Password" link click
document.getElementById('forgotPassword').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
    alert('Redirecting to password recovery...'); // Simulate password recovery action
});
```
