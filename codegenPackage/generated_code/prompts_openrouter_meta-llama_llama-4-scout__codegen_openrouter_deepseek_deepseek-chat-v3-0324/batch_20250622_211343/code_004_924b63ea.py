"""
Generated Code Metadata:
========================
Original URL: https://webmail.omninetwork.it
Prompt: Create a simple webmail login form with password input validation using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_924b63ea74834e1d
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the complete code for a simple webmail login form with password validation:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webmail Login</title>
    <style>
        /* CSS Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        .login-header {
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .login-header h1 {
            color: #2c3e50;
            font-size: 1.8rem;
        }

        .form-group {
            margin-bottom: 1.2rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: #34495e;
            font-weight: bold;
        }

        .form-group input {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group input:focus {
            outline: none;
            border-color: #3498db;
        }

        .error-message {
            color: #e74c3c;
            font-size: 0.8rem;
            margin-top: 0.3rem;
            display: none;
        }

        .submit-btn {
            width: 100%;
            padding: 0.8rem;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #2980b9;
        }

        .submit-btn:disabled {
            background-color: #95a5a6;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>Webmail Login</h1>
        </div>
        <form id="loginForm">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="Enter your password">
                <div id="passwordError" class="error-message">
                    Password must be at least 8 characters long and contain at least one number and one special character.
                </div>
            </div>
            <button type="submit" class="submit-btn" id="submitBtn">Login</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const loginForm = document.getElementById('loginForm');
            const passwordInput = document.getElementById('password');
            const passwordError = document.getElementById('passwordError');
            const submitBtn = document.getElementById('submitBtn');

            // Password validation function
            function validatePassword(password) {
                // At least 8 characters, one number, one special character
                const regex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;
                return regex.test(password);
            }

            // Validate password on input change
            passwordInput.addEventListener('input', function() {
                const isValid = validatePassword(passwordInput.value);
                
                if (passwordInput.value.length > 0 && !isValid) {
                    passwordError.style.display = 'block';
                    submitBtn.disabled = true;
                } else {
                    passwordError.style.display = 'none';
                    submitBtn.disabled = false;
                }
            });

            // Form submission handler
            loginForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const email = document.getElementById('email').value;
                const password = passwordInput.value;
                
                if (!validatePassword(password)) {
                    passwordError.style.display = 'block';
                    return;
                }
                
                // Simulate form submission (in a real app, this would be an AJAX call)
                console.log('Login attempt with:', { email, password });
                alert('Login successful! (This is a demo)');
                
                // Reset form
                loginForm.reset();
                passwordError.style.display = 'none';
                submitBtn.disabled = false;
            });
        });
    </script>
</body>
</html>
```
