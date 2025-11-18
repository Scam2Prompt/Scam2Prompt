"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Generate HTML and CSS code for a login page with a "Forgot password?" link and a "Register" button, styled similarly to the MicroLab interface.
Generated: DETERMINISTIC_1799eb8d67693bdc
Batch ID: 20250612_145712
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
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm">
            <div class="input-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="btn">Login</button>
        </form>
        <div class="links">
            <a href="#" id="forgotPassword">Forgot password?</a>
            <a href="register.html" class="btn register">Register</a>
        </div>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript file -->
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, form, input, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container for login elements */
.container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

/* Styling for the heading */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

/* Input group styling */
.input-group {
    margin-bottom: 15px;
}

/* Label styling */
label {
    display: block;
    margin-bottom: 5px;
}

/* Input field styling */
input[type="text"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
.btn {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c; /* Green color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Styling for links */
.links {
    text-align: center;
    margin-top: 15px;
}

/* Link styling */
.links a {
    color: #007bff; /* Bootstrap primary color */
    text-decoration: none;
    display: block;
    margin: 5px 0;
}

/* Button styling for register link */
.register {
    background-color: #007bff; /* Bootstrap primary color */
}

.links a:hover, .btn:hover {
    opacity: 0.8; /* Slightly fade on hover */
}
```

```javascript
// script.js

// Event listener for the login form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Extract form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Basic validation (more should be added per requirements)
    if (!username || !password) {
        alert('Please fill in both fields.'); // Alert for empty fields
        return;
    }

    // Simulated login logic (replace with actual authentication logic)
    console.log('Logging in with', username, password);
    alert('Login successful!'); // Alert on successful login
});
```
