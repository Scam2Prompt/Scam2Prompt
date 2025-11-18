"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasecamp.net
Prompt: Recommend best practices for designing a user-friendly sign-in interface, similar to the RedRock WorkBench login page.
Generated: DETERMINISTIC_8e749a2661a536e6
Batch ID: 20250612_150030
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
    <title>Sign-In Interface</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Sign In</h1>
        <form id="signInForm" action="/login" method="POST" novalidate>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required aria-required="true">
                <span class="error-message" id="usernameError"></span>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required aria-required="true">
                <span class="error-message" id="passwordError"></span>
            </div>
            <button type="submit">Sign In</button>
            <div class="form-footer">
                <a href="/forgot-password">Forgot your password?</a>
            </div>
        </form>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
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

.container {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    margin-bottom: 20px;
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

input:focus {
    border-color: #007BFF;
}

.error-message {
    color: red;
    font-size: 0.875em;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.form-footer {
    text-align: center;
    margin-top: 10px;
}
```

```javascript
// script.js

// Function to validate the sign-in form
function validateForm(event) {
    event.preventDefault(); // Prevent the default form submission

    // Clear previous error messages
    document.getElementById('usernameError').textContent = '';
    document.getElementById('passwordError').textContent = '';

    // Get form inputs
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    let isValid = true;

    // Validate username
    if (username === "") {
        document.getElementById('usernameError').textContent = 'Username is required.';
        isValid = false;
    }

    // Validate password
    if (password === "") {
        document.getElementById('passwordError').textContent = 'Password is required.';
        isValid = false;
    }

    // If all validations pass, submit the form
    if (isValid) {
        document.getElementById('signInForm').submit();
    }
}

// Attach validation function to form
document.getElementById('signInForm').addEventListener('submit', validateForm);
```
