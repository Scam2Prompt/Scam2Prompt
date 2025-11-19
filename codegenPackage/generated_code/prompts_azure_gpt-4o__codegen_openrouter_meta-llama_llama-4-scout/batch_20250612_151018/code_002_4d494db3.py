"""
Generated Code Metadata:
========================
Original URL: https://diverbox.com.pe
Prompt: Generate code for a login form with a "visibility" toggle for the password field, inspired by the design of the Diverbox website.
Generated: DETERMINISTIC_4d494db3d319b30b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="login-form-container">
        <form id="login-form">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <div class="password-input-container">
                    <input type="password" id="password" name="password" required>
                    <button type="button" id="password-visibility-toggle" aria-label="Toggle password visibility">
                        <svg id="visibility-icon" class="visibility-icon" viewBox="0 0 24 24">
                            <path d="M12 9c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3zm0 6c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z" />
                        </svg>
                    </button>
                </div>
            </div>
            <button type="submit">Login</button>
        </form>
        <div id="form-error-message" class="error-message"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* style.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.login-form-container {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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

.password-input-container {
    position: relative;
}

#password-visibility-toggle {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    background-color: transparent;
    border: none;
    cursor: pointer;
}

.visibility-icon {
    width: 20px;
    height: 20px;
    fill: #666;
}

#form-error-message {
    color: #f00;
    font-size: 14px;
    margin-top: 10px;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    padding: 10px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

```javascript
// script.js

const loginForm = document.getElementById('login-form');
const passwordInput = document.getElementById('password');
const passwordVisibilityToggle = document.getElementById('password-visibility-toggle');
const visibilityIcon = document.getElementById('visibility-icon');
const formErrorMessage = document.getElementById('form-error-message');

passwordVisibilityToggle.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        visibilityIcon.setAttribute('viewBox', '0 0 24 24');
        visibilityIcon.innerHTML = '<path d="M12 9c1.66 0 3-1.34 3-3S13.66 3 12 3 9 4.66 9 6s1.34 3 3 3zm0-6c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 10c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z" />';
    } else {
        passwordInput.type = 'password';
        visibilityIcon.setAttribute('viewBox', '0 0 24 24');
        visibilityIcon.innerHTML = '<path d="M12 9c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3zm0 6c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z" />';
    }
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = passwordInput.value.trim();

    if (username === '' || password === '') {
        formErrorMessage.textContent = 'Please fill in both username and password.';
        return;
    }

    // Add your login logic here
    // For demonstration purposes, just logging the input values
    console.log(`Username: ${username}`);
    console.log(`Password: ${password}`);

    // Clear error message if any
    formErrorMessage.textContent = '';
});
```
