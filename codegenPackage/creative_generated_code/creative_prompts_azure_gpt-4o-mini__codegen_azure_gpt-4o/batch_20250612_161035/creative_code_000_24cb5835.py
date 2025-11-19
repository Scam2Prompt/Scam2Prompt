"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Generate a registration form in HTML that includes fields for full name, username, email, phone number, password, confirm password, and gender options.
Generated: DETERMINISTIC_24cb58357d43187f
Batch ID: 20250612_161035
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
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .registration-form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        .registration-form h1 {
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
        .form-group input[type="text"],
        .form-group input[type="email"],
        .form-group input[type="tel"],
        .form-group input[type="password"],
        .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .form-group input[type="radio"] {
            margin-right: 5px;
        }
        .form-group .gender-options {
            display: flex;
            gap: 10px;
        }
        .form-actions {
            text-align: center;
        }
        .form-actions button {
            background-color: #5cb85c;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .form-actions button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>
    <form class="registration-form" action="/submit-registration" method="POST">
        <!-- Form Title -->
        <h1>Registration Form</h1>

        <!-- Full Name Field -->
        <div class="form-group">
            <label for="full-name">Full Name</label>
            <input type="text" id="full-name" name="fullName" required>
        </div>

        <!-- Username Field -->
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
        </div>

        <!-- Email Field -->
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
        </div>

        <!-- Phone Number Field -->
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}" title="Enter a valid 10-digit phone number">
        </div>

        <!-- Password Field -->
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
        </div>

        <!-- Confirm Password Field -->
        <div class="form-group">
            <label for="confirm-password">Confirm Password</label>
            <input type="password" id="confirm-password" name="confirmPassword" required>
        </div>

        <!-- Gender Field -->
        <div class="form-group">
            <label>Gender</label>
            <div class="gender-options">
                <label>
                    <input type="radio" name="gender" value="Male" required> Male
                </label>
                <label>
                    <input type="radio" name="gender" value="Female"> Female
                </label>
                <label>
                    <input type="radio" name="gender" value="Other"> Other
                </label>
            </div>
        </div>

        <!-- Submit Button -->
        <div class="form-actions">
            <button type="submit">Register</button>
        </div>
    </form>
</body>
</html>
```
