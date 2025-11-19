"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: How would you create a registration form in HTML that captures username, phone number, and referral code like the one on bonnabdcc.com?
Generated: DETERMINISTIC_4c8380e024871d9e
Batch ID: 20250612_162701
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
    <title>Registration Form</title>
    <!-- Link to CSS for styling -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .form-container {
            max-width: 400px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group input:focus {
            border-color: #007BFF;
            outline: none;
        }
        .form-group .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .form-group button {
            width: 100%;
            background-color: #007BFF;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Registration Form</h2>
        <form id="registrationForm" action="#" method="POST">
            <!-- Username Field -->
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                <span class="error" id="usernameError"></span>
            </div>
            <!-- Phone Number Field -->
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" pattern="[0-9]{10}" required>
                <span class="error" id="phoneError"></span>
            </div>
            <!-- Referral Code Field -->
            <div class="form-group">
                <label for="referralCode">Referral Code</label>
                <input type="text" id="referralCode" name="referralCode" placeholder="Enter referral code (optional)">
            </div>
            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
        </form>
    </div>

    <!-- JavaScript for Form Validation -->
    <script>
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous errors
            document.getElementById('usernameError').textContent = '';
            document.getElementById('phoneError').textContent = '';

            // Validate Username
            const username = document.getElementById('username').value.trim();
            if (username.length < 3) {
                document.getElementById('usernameError').textContent = 'Username must be at least 3 characters.';
                isValid = false;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone').value.trim();
            if (!/^[0-9]{10}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Phone number must be 10 digits.';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
