"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Generate code for a "Refresh" button on a login page that reloads the page without losing entered data, inspired by the Empower login page.
Generated: DETERMINISTIC_025385f2d46b06e4
Batch ID: 20250612_150645
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
    <style>
        /* Basic styles for the login form */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f2f2f2;
        }
        .login-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="loginForm" onsubmit="return handleSubmit(event);">
            <input type="text" id="username" placeholder="Username" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Login</button>
            <button type="button" id="refreshButton">Refresh</button>
        </form>
    </div>

    <script>
        // Function to handle form submission
        function handleSubmit(event) {
            event.preventDefault(); // Prevent the default form submission
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Here you would typically handle login logic (e.g., API call)
            console.log('Username:', username);
            console.log('Password:', password);
            // Placeholder for login action
        }

        // Add event listener to the refresh button
        document.getElementById('refreshButton').addEventListener('click', function() {
            // Store the current values in local storage to preserve them during refresh
            localStorage.setItem('username', document.getElementById('username').value);
            localStorage.setItem('password', document.getElementById('password').value);
            
            // Reload the page
            location.reload();
        });

        // Retrieve stored values from local storage on page load
        window.onload = function() {
            const storedUsername = localStorage.getItem('username');
            const storedPassword = localStorage.getItem('password');

            if (storedUsername) {
                document.getElementById('username').value = storedUsername;
            }
            if (storedPassword) {
                document.getElementById('password').value = storedPassword;
            }
        };
    </script>
</body>
</html>
```
