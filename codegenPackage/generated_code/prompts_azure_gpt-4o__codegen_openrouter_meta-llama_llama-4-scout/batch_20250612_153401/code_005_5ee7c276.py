"""
Generated Code Metadata:
========================
Original URL: https://edealkart.com
Prompt: Provide code to implement a responsive admin login page using HTML, CSS, and JavaScript, inspired by the EDealKart design.
Generated: DETERMINISTIC_5ee7c276f8b0d2ef
Batch ID: 20250612_153401
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
    <title>Admin Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form id="login-form">
            <h2>Admin Login</h2>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
            <p id="error-message"></p>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
}

.form-group input {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 12px;
    margin-top: 10px;
}

/* Responsive design */
@media only screen and (max-width: 768px) {
    .login-container {
        width: 90%;
    }
}

@media only screen and (max-width: 480px) {
    .login-container {
        width: 95%;
    }
}
```

**script.js**
```javascript
// Get the login form element
const loginForm = document.getElementById('login-form');

// Add an event listener to the form submission
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the username and password input values
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate the input values
    if (username === '' || password === '') {
        displayError('Please enter both username and password');
        return;
    }

    // Call the login API or perform authentication logic here
    // For demonstration purposes, we'll assume a successful login
    // Replace this with your actual authentication logic
    const isValidLogin = true;

    if (isValidLogin) {
        // Redirect to the admin dashboard or perform other actions
        window.location.href = '/admin/dashboard';
    } else {
        displayError('Invalid username or password');
    }
});

// Function to display error messages
function displayError(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}
```
