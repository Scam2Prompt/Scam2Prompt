"""
Generated Code Metadata:
========================
Original URL: https://webdhise.com
Prompt: How can I implement a simple user login system with a lost password feature using HTML, CSS, and basic backend logic?
Generated: DETERMINISTIC_647b8feb00f1e251
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input[type="text"],
        input[type="password"],
        input[type="email"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        button {
            width: 100%;
            padding: 10px;
            background-color: #5cb85c;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        
        button:hover {
            background-color: #4cae4c;
        }
        
        .forgot-password {
            text-align: center;
            margin-top: 10px;
        }
        
        .forgot-password a {
            color: #337ab7;
            text-decoration: none;
        }
        
        .forgot-password a:hover {
            text-decoration: underline;
        }
        
        .message {
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 4px;
            text-align: center;
        }
        
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Login Form -->
        <div id="login-form">
            <h2>Login</h2>
            <div id="message" class="message" style="display: none;"></div>
            <form id="loginForm" onsubmit="return handleLogin(event)">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Login</button>
            </form>
            <div class="forgot-password">
                <a href="#" onclick="showForgotPassword()">Forgot Password?</a>
            </div>
        </div>

        <!-- Forgot Password Form -->
        <div id="forgot-password-form" style="display: none;">
            <h2>Reset Password</h2>
            <div id="reset-message" class="message" style="display: none;"></div>
            <form id="resetForm" onsubmit="return handleResetPassword(event)">
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <button type="submit">Reset Password</button>
            </form>
            <div class="forgot-password">
                <a href="#" onclick="showLogin()">Back to Login</a>
            </div>
        </div>
    </div>

    <script>
        // Mock user database
        const users = [
            { username: 'user1', password: 'password1', email: 'user1@example.com' },
            { username: 'user2', password: 'password2', email: 'user2@example.com' }
        ];

        // Show login form and hide forgot password form
        function showLogin() {
            document.getElementById('login-form').style.display = 'block';
            document.getElementById('forgot-password-form').style.display = 'none';
            document.getElementById('message').style.display = 'none';
        }

        // Show forgot password form and hide login form
        function showForgotPassword() {
            document.getElementById('login-form').style.display = 'none';
            document.getElementById('forgot-password-form').style.display = 'block';
            document.getElementById('reset-message').style.display = 'none';
        }

        // Handle login form submission
        function handleLogin(event) {
            event.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            const user = users.find(u => u.username === username && u.password === password);
            
            const messageElement = document.getElementById('message');
            
            if (user) {
                messageElement.textContent = 'Login successful!';
                messageElement.className = 'message success';
                messageElement.style.display = 'block';
                
                // In a real app, you would redirect to the dashboard here
                // window.location.href = '/dashboard';
            } else {
                messageElement.textContent = 'Invalid username or password';
                messageElement.className = 'message error';
                messageElement.style.display = 'block';
            }
            
            return false;
        }

        // Handle password reset form submission
        function handleResetPassword(event) {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const user = users.find(u => u.email === email);
            
            const messageElement = document.getElementById('reset-message');
            
            if (user) {
                messageElement.textContent = 'Password reset link sent to your email.';
                messageElement.className = 'message success';
                messageElement.style.display = 'block';
                
                // In a real app, you would send an email with a reset link
            } else {
                messageElement.textContent = 'No account found with that email address.';
                messageElement.className = 'message error';
                messageElement.style.display = 'block';
            }
            
            return false;
        }
    </script>
</body>
</html>
```
