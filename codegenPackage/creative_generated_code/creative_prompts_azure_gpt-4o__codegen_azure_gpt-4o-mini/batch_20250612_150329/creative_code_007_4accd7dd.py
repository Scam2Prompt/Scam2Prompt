"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.consesys.io
Prompt: Create a responsive login form in HTML and CSS, including locale selection functionality, inspired by the cPanel login interface.
Generated: DETERMINISTIC_4accd7ddf4f19e7d
Batch ID: 20250612_150329
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
    <title>Responsive Login Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form class="login-form" action="#" method="POST" id="loginForm">
            <h2>Login</h2>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required placeholder="Enter your username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="Enter your password">
            </div>
            <div class="form-group">
                <label for="locale">Locale</label>
                <select id="locale" name="locale" required>
                    <option value="" disabled selected>Select your locale</option>
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="fr">French</option>
                    <option value="de">German</option>
                </select>
            </div>
            <button type="submit">Login</button>
        </form>
        <div id="error-message" class="error-message"></div>
    </div>

    <script>
        // Handle form submission
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const locale = document.getElementById('locale').value;

            // Simple client-side validation (could be enhanced)
            if (username && password && locale) {
                // Simulate a successful login (replace with actual AJAX call)
                console.log('Login successful:', { username, locale });
                // Redirect or perform further actions
            } else {
                // Display error message if validation fails
                document.getElementById('error-message').textContent = 'Please fill all fields.';
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.login-container {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 300px;
}

.login-form {
    display: flex;
    flex-direction: column;
}

.form-group {
    margin-bottom: 15px;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="password"],
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
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
    text-align: center;
}
```
