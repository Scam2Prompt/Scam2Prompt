"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Implement a login form in HTML and JavaScript that includes fields for username and password, along with a dropdown for locale selection, modeled after the cPanel login interface.
Generated: DETERMINISTIC_e99a983e4a208db5
Batch ID: 20250612_145455
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
    <title>Login Form</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="loginForm" onsubmit="return handleLogin(event)">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="locale">Select Locale:</label>
                <select id="locale" name="locale" required>
                    <option value="">Choose your locale...</option>
                    <option value="en-US">English (US)</option>
                    <option value="en-GB">English (UK)</option>
                    <option value="fr-FR">Français</option>
                    <option value="de-DE">Deutsch</option>
                </select>
            </div>
            <button type="submit">Login</button>
        </form>
        <div id="error-message" class="error-message"></div>
    </div>
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
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    border: none;
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error-message {
    color: red;
    margin-top: 10px;
}
```

```javascript
// script.js

/**
 * Handles the login form submission.
 * @param {Event} event - The event object from the form submission.
 * @returns {boolean} Returns false to prevent default form submission.
 */
function handleLogin(event) {
    event.preventDefault(); // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const locale = document.getElementById('locale').value;
    const errorMessageElement = document.getElementById('error-message');

    // Validate form fields
    if (!username || !password || !locale) {
        errorMessageElement.innerText = "All fields are required.";
        return false;
    }

    // Simulate an API call with a promise
    fakeApiCall(username, password, locale)
        .then((response) => {
            // Handle successful login here (e.g., redirect)
            console.log("Login successful:", response);
            alert("Login successful!"); // Placeholder action
        })
        .catch((error) => {
            // Handle login failure
            errorMessageElement.innerText = error.message;
        });

    return false; // Prevent default form submission
}

/**
 * Simulates an API call for user login.
 * @param {string} username - The username input by the user.
 * @param {string} password - The password input by the user.
 * @param {string} locale - The selected locale.
 * @returns {Promise} A promise that resolves or rejects based on simulated login success.
 */
function fakeApiCall(username, password, locale) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simulate a successful login response
            if (username === "user" && password === "pass") {
                resolve({ status: "success", locale });
            } else {
                reject(new Error("Invalid username or password."));
            }
        }, 1000); // Simulate network delay
    });
}
```
