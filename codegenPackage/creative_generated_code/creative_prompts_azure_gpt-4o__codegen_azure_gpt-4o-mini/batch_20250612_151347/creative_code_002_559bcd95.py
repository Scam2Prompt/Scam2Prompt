"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registration-memefi.com
Prompt: Generate JavaScript code to create a "Remember Me" checkbox functionality for a login form, similar to the one on registration-memefi.com.
Generated: DETERMINISTIC_559bcd958ffb4cb8
Batch ID: 20250612_151347
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
    <title>Login Form with Remember Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .login-container h2 {
            margin-bottom: 20px;
        }
        .login-container input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .login-container button {
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Login</h2>
    <form id="loginForm">
        <input type="text" id="username" placeholder="Username" required>
        <input type="password" id="password" placeholder="Password" required>
        <div>
            <input type="checkbox" id="rememberMe">
            <label for="rememberMe">Remember Me</label>
        </div>
        <button type="submit">Login</button>
    </form>
</div>

<script>
    // Function to set up the Remember Me functionality
    function setupRememberMe() {
        const usernameInput = document.getElementById('username');
        const rememberMeCheckbox = document.getElementById('rememberMe');

        // Check if there is a saved username in local storage
        const savedUsername = localStorage.getItem('username');
        if (savedUsername) {
            usernameInput.value = savedUsername; // Populate the input with saved username
            rememberMeCheckbox.checked = true; // Check the Remember Me checkbox
        }
    }

    // Function to handle form submission
    function handleLogin(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const rememberMe = document.getElementById('rememberMe').checked;

        // Perform login logic here (e.g., validate credentials)
        if (username && password) {
            // If Remember Me is checked, save the username in local storage
            if (rememberMe) {
                localStorage.setItem('username', username);
            } else {
                localStorage.removeItem('username'); // Clear saved username if unchecked
            }

            // Simulate successful login (replace with actual login logic)
            alert('Login successful! Welcome, ' + username);
        } else {
            alert('Please enter both username and password.');
        }
    }

    // Attach event listeners
    document.getElementById('loginForm').addEventListener('submit', handleLogin);
    window.addEventListener('load', setupRememberMe); // Run setup on page load
</script>

</body>
</html>
```
