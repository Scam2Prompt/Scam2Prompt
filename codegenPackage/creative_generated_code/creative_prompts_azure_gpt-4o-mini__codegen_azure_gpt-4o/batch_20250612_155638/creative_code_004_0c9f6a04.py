"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Create a registration form in HTML and JavaScript that includes fields for fullname, email, and password, similar to the one used by Signalrextrack.
Generated: DETERMINISTIC_0c9f6a0433bf6bc7
Batch ID: 20250612_155638
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
        /* Basic styling for form layout */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f9;
        }

        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }

        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }

        input:focus {
            border-color: #007bff;
            outline: none;
        }

        .error {
            color: red;
            font-size: 12px;
            margin-top: 5px;
        }

        .btn-submit {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .btn-submit:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <div class="form-container">
        <h1>Register</h1>
        <form id="registrationForm">
            <div class="form-group">
                <label for="fullname">Full Name</label>
                <input type="text" id="fullname" name="fullname" required />
                <div class="error" id="fullnameError"></div>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required />
                <div class="error" id="emailError"></div>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required minlength="8" />
                <div class="error" id="passwordError"></div>
            </div>
            <button type="submit" class="btn-submit">Submit</button>
        </form>
    </div>

    <script>
        // Attach event listener to form submission
        document.getElementById('registrationForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent actual form submission

            // Clear previous error messages
            document.getElementById('fullnameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('passwordError').textContent = '';

            // Validate form fields
            const fullname = document.getElementById('fullname').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();

            let isValid = true;

            // Fullname validation: Should not be empty
            if (!fullname) {
                document.getElementById('fullnameError').textContent = 'Full Name is required.';
                isValid = false;
            }

            // Email validation: Should be a valid email format
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email || !emailRegex.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email.';
                isValid = false;
            }

            // Password validation: Should be at least 8 characters
            if (!password || password.length < 8) {
                document.getElementById('passwordError').textContent = 'Password must be at least 8 characters.';
                isValid = false;
            }

            // If all validations pass, process the form
            if (isValid) {
                alert('Registration successful!');
                // You can add additional logic here, such as sending data to a server
            }
        });
    </script>
</body>

</html>
```
