"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorcommunity.com
Prompt: Can you provide a code snippet for creating a login form that restricts access to a specific section of a website?
Generated: DETERMINISTIC_d160fea4559b7566
Batch ID: 20250612_163423
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
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .login-container {
            width: 300px;
            margin: 100px auto;
            padding: 20px;
            background: white;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .login-container input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
        }
        .login-container button {
            width: 100%;
            padding: 10px;
            background: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .login-container button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Login</h2>
    <form id="loginForm">
        <input type="text" id="username" placeholder="Username" required>
        <input type="password" id="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <div id="message" style="color: red;"></div>
</div>

<script>
    // Dummy credentials for demonstration
    const validUsername = 'admin';
    const validPassword = 'password123';

    // Form submission event listener
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Retrieve input values
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const messageElement = document.getElementById('message');

        // Validate credentials
        if (username === validUsername && password === validPassword) {
            // Redirect to restricted section
            window.location.href = 'restricted.html'; // Change this to the restricted page URL
        } else {
            // Display error message for invalid credentials
            messageElement.textContent = 'Invalid username or password.';
        }
    });
</script>

</body>
</html>
```

```html
<!-- restricted.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restricted Area</title>
</head>
<body>
    <h1>Welcome to the Restricted Section</h1>
    <p>You have successfully logged in!</p>
</body>
</html>
```
