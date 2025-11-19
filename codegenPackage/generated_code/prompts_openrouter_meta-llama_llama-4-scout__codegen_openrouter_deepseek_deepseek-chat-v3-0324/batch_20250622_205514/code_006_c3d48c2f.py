"""
Generated Code Metadata:
========================
Original URL: https://hope-exchange.com
Prompt: "Design a basic email sign-up form using JavaScript, HTML, and CSS that could be used for a site like Hope Exchange."
Generated: DETERMINISTIC_c3d48c2f27772532
Batch ID: 20250622_205514
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
    <title>Hope Exchange - Email Sign Up</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 400px;
        }

        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
            font-size: 24px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #2c3e50;
            font-weight: bold;
        }

        input[type="email"] {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        input[type="email"]:focus {
            outline: none;
            border-color: #3498db;
        }

        button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px;
            width: 100%;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #2980b9;
        }

        .message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            text-align: center;
            display: none;
        }

        .success {
            background-color: #d4edda;
            color: #155724;
        }

        .error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Join Hope Exchange</h1>
        <form id="signupForm">
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">
            </div>
            <button type="submit">Sign Up</button>
        </form>
        <div id="message" class="message"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('signupForm');
            const messageDiv = document.getElementById('message');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const email = document.getElementById('email').value.trim();
                
                // Validate email format
                if (!isValidEmail(email)) {
                    showMessage('Please enter a valid email address', 'error');
                    return;
                }
                
                // Simulate form submission
                setTimeout(() => {
                    showMessage('Thank you for signing up!', 'success');
                    form.reset();
                }, 1000);
            });

            /**
             * Validates email format
             * @param {string} email - Email address to validate
             * @returns {boolean} True if email is valid
             */
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }

            /**
             * Shows a message to the user
             * @param {string} text - Message to display
             * @param {string} type - Type of message ('success' or 'error')
             */
            function showMessage(text, type) {
                messageDiv.textContent = text;
                messageDiv.className = 'message ' + type;
                messageDiv.style.display = 'block';
                
                // Hide message after 5 seconds
                setTimeout(() => {
                    messageDiv.style.display = 'none';
                }, 5000);
            }
        });
    </script>
</body>
</html>
```
