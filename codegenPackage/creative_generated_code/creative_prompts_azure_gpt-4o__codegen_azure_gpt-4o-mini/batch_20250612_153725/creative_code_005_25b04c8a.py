"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Create a JavaScript function to display a password strength meter on the Signalrextrack registration form, dynamically updating based on user input.
Generated: DETERMINISTIC_25b04c8a52e54255
Batch ID: 20250612_153725
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
    <title>Password Strength Meter</title>
    <style>
        /* Basic styles for the password strength meter */
        #strength-meter {
            height: 10px;
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 5px;
            margin-top: 10px;
        }
        .strength-weak {
            background-color: red;
        }
        .strength-fair {
            background-color: yellow;
        }
        .strength-good {
            background-color: blue;
        }
        .strength-strong {
            background-color: green;
        }
    </style>
</head>
<body>

    <form id="registration-form">
        <label for="password">Password:</label>
        <input type="password" id="password" required>
        <div id="strength-meter"></div>
        <div id="strength-text"></div>
    </form>

    <script>
        /**
         * Function to update password strength meter based on password input
         * @param {string} password - The password input from the user
         * @returns {void}
         */
        function updatePasswordStrength(password) {
            const strengthMeter = document.getElementById('strength-meter');
            const strengthText = document.getElementById('strength-text');
            let strength = 0;

            // Check password length
            if (password.length >= 8) strength++;
            if (password.match(/[A-Z]/)) strength++; // Uppercase letter
            if (password.match(/[a-z]/)) strength++; // Lowercase letter
            if (password.match(/[0-9]/)) strength++; // Number
            if (password.match(/[\W_]/)) strength++; // Special character

            // Update the strength meter and text based on strength value
            switch (strength) {
                case 0:
                case 1:
                    strengthMeter.className = 'strength-weak';
                    strengthText.textContent = 'Weak password';
                    break;
                case 2:
                    strengthMeter.className = 'strength-fair';
                    strengthText.textContent = 'Fair password';
                    break;
                case 3:
                    strengthMeter.className = 'strength-good';
                    strengthText.textContent = 'Good password';
                    break;
                case 4:
                case 5:
                    strengthMeter.className = 'strength-strong';
                    strengthText.textContent = 'Strong password';
                    break;
                default:
                    strengthMeter.className = '';
                    strengthText.textContent = '';
            }

            // Update the width of the strength meter
            strengthMeter.style.width = `${(strength / 5) * 100}%`;
        }

        // Event listener for password input
        document.getElementById('password').addEventListener('input', (event) => {
            try {
                const password = event.target.value;
                updatePasswordStrength(password);
            } catch (error) {
                console.error('Error updating password strength:', error);
            }
        });
    </script>

</body>
</html>
```
