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
<!-- login.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FuturX Login Page</title>
    <!-- External CSS -->
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="login-container">
        <form id="login-form" class="login-form">
            <h1>Login to FuturX</h1>

            <!-- Input for Email -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
            </div>

            <!-- Input for Password -->
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>

            <!-- Login Button -->
            <button type="submit" class="login-button">Login</button>

            <!-- Error Message Placeholder -->
            <p id="error-message" class="error-message"></p>
        </form>
    </div>

    <!-- External JavaScript -->
    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f4;
}

.login-container {
    width: 100%;
    max-width: 400px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

.login-form {
    display: flex;
    flex-direction: column;
}

.login-form h1 {
    text-align: center;
    margin-bottom: 20px;
    font-size: 24px;
    color: #333333;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    font-size: 14px;
    color: #333333;
    margin-bottom: 5px;
}

.form-group input {
    width: 100%;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #cccccc;
    border-radius: 4px;
}

.login-button {
    background-color: #007bff;
    color: #ffffff;
    border: none;
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.login-button:hover {
    background-color: #0056b3;
}

.error-message {
    color: #ff0000;
    font-size: 14px;
    margin-top: 10px;
    text-align: center;
}
```

```javascript
// script.js

// Wait for DOM content to fully load
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    // Add event listener for form submission
    loginForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission behavior

        // Get email and password values from form inputs
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        // Basic validation
        if (!email || !password) {
            errorMessage.textContent = 'Please fill out all fields.';
            return;
        }

        // Simulate login logic (replace with actual authentication logic in production)
        if (email === 'user@futurx.com' && password === 'password123') {
            alert('Login successful!');
            errorMessage.textContent = ''; // Clear error message
        } else {
            errorMessage.textContent = 'Invalid email or password.';
        }
    });
});
```

This code includes HTML, CSS, and JavaScript to create a login form with validation and basic functionality, following best practices and good structure.
