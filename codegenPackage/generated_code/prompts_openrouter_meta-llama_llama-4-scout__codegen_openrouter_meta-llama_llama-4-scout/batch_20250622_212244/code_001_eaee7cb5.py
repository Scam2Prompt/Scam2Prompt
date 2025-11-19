"""
Generated Code Metadata:
========================
Original URL: https://www.metaprofx.com
Prompt: Generate HTML and CSS code for a basic login form with fields for username and password.
Generated: DETERMINISTIC_eaee7cb5393611d7
Batch ID: 20250622_212244
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
    <title>Login Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="login-container">
        <h2>Login Form</h2>
        <form id="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Login</button>
        </form>
        <div id="error-message"></div>
    </div>

    <script>
        // Get the form and error message elements
        const form = document.getElementById('login-form');
        const errorMessage = document.getElementById('error-message');

        // Add event listener to form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Get the username and password values
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Basic validation
            if (username.trim() === '' || password.trim() === '') {
                errorMessage.textContent = 'Please fill in both fields.';
                return;
            }

            // TODO: Implement actual login logic here
            console.log(`Login attempt with username: ${username} and password: ${password}`);
        });
    </script>
</body>
</html>
```

**style.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.login-container {
    width: 300px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-container h2 {
    text-align: center;
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
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
    font-size: 14px;
    margin-top: 10px;
}
```
