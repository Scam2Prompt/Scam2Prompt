"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenroyale.com
Prompt: Create a JavaScript function to replicate the user-friendly registration process described on Royal Reels Casino, including form validation and password strength checks.
Generated: DETERMINISTIC_b5f5c48d39006f73
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Registration form functionality for a user-friendly registration process.
 * Includes real-time form validation and password strength checks.
 */

// Function to initialize the registration form
function initializeRegistrationForm() {
    const form = document.getElementById('registrationForm');
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirmPassword');
    const submitButton = document.getElementById('submitButton');
    const passwordStrengthIndicator = document.getElementById('passwordStrengthIndicator');

    // Utility function to validate email format
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Utility function to check password strength
    function checkPasswordStrength(password) {
        if (password.length < 8) return 'Weak';
        if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(password)) return 'Strong';
        return 'Medium';
    }

    // Real-time validation for username
    usernameField.addEventListener('input', () => {
        if (usernameField.value.trim() === '') {
            usernameField.setCustomValidity('Username is required.');
        } else if (usernameField.value.length < 3) {
            usernameField.setCustomValidity('Username must be at least 3 characters long.');
        } else {
            usernameField.setCustomValidity('');
        }
    });

    // Real-time validation for email
    emailField.addEventListener('input', () => {
        if (!isValidEmail(emailField.value)) {
            emailField.setCustomValidity('Please enter a valid email address.');
        } else {
            emailField.setCustomValidity('');
        }
    });

    // Real-time password strength check
    passwordField.addEventListener('input', () => {
        const strength = checkPasswordStrength(passwordField.value);
        passwordStrengthIndicator.textContent = `Password Strength: ${strength}`;
        if (strength === 'Weak') {
            passwordField.setCustomValidity('Password is too weak. Must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.');
        } else {
            passwordField.setCustomValidity('');
        }
    });

    // Real-time validation for confirm password
    confirmPasswordField.addEventListener('input', () => {
        if (confirmPasswordField.value !== passwordField.value) {
            confirmPasswordField.setCustomValidity('Passwords do not match.');
        } else {
            confirmPasswordField.setCustomValidity('');
        }
    });

    // Final validation on form submission
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form submission if there are validation errors

        // Check if all fields are valid
        if (form.checkValidity()) {
            alert('Registration successful!');
            // Add production-ready form handling here (e.g., send data to server)
        } else {
            alert('Please fix the errors in the form before submitting.');
        }
    });
}

// Initialize the form functionality when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeRegistrationForm);
```

### HTML Structure Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body>
    <form id="registrationForm">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <span id="passwordStrengthIndicator"></span>
        <br>

        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" name="confirmPassword" required>
        <br>

        <button type="submit" id="submitButton">Register</button>
    </form>

    <script src="registration.js"></script>
</body>
</html>
```
