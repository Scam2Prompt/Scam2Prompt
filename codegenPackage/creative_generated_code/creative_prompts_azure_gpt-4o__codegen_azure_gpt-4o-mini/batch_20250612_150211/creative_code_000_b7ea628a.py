"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Write code to implement a "Keep me Logged in" checkbox feature for a login form, similar to the one described on Pavonal's login page.
Generated: DETERMINISTIC_b7ea628a3af0a698
Batch ID: 20250612_150211
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form id="loginForm" action="/login" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <div>
                <input type="checkbox" id="keepLoggedIn" name="keepLoggedIn">
                <label for="keepLoggedIn">Keep me logged in</label>
            </div>

            <button type="submit">Login</button>
        </form>
        <div id="error-message" class="error-message"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('loginForm').onsubmit = async (event) => {
            event.preventDefault(); // Prevent default form submission
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const keepLoggedIn = document.getElementById('keepLoggedIn').checked;

            try {
                // Validate input
                if (!username || !password) {
                    throw new Error('Username and password are required.');
                }

                // Example login request (adjust the URL as necessary)
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password, keepLoggedIn })
                });

                // Check response status
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.message || 'Login failed.');
                }

                // Handle successful login (e.g., redirect to dashboard)
                window.location.href = '/dashboard';
            } catch (error) {
                // Display error message to the user
                document.getElementById('error-message').innerText = error.message;
            }
        };
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.login-container {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.error-message {
    color: red;
    margin-top: 10px;
}
```
