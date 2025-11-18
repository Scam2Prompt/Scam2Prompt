"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://login.futurx.live
Prompt: Create a login form using HTML, CSS, and JavaScript that mimics the structure and functionality of the FuturX login page.
Generated: DETERMINISTIC_3973306c3ab02956
Batch ID: 20250612_145626
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
    <title>FuturX Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h1>FuturX Login</h1>
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
            <div class="error-message" id="error-message"></div>
        </form>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.login-container {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-bottom: 1.5rem;
    text-align: center;
}

.form-group {
    margin-bottom: 1rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
}

input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 0.5rem;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error-message {
    color: red;
    margin-top: 1rem;
    text-align: center;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission behavior

    // Extracting username and password values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation (this can be expanded with more complex logic)
    if (username === "" || password === "") {
        showError("Please fill out both fields.");
        return;
    }

    // Simulate a login request (replace with real authentication logic)
    fakeLogin(username, password)
        .then(response => {
            if (response.success) {
                // Handle successful login (e.g., redirect to another page)
                window.location.href = 'dashboard.html'; // Change to your dashboard URL
            } else {
                showError(response.message);
            }
        })
        .catch(error => {
            showError("An unexpected error occurred. Please try again later.");
            console.error("Login error:", error);
        });
});

// Function to simulate a login request
function fakeLogin(username, password) {
    return new Promise((resolve) => {
        // Simulate an API call with a timeout
        setTimeout(() => {
            if (username === 'user' && password === 'pass') {
                resolve({ success: true });
            } else {
                resolve({ success: false, message: "Invalid username or password." });
            }
        }, 1000);
    });
}

// Function to display error messages
function showError(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}
```
