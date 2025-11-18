"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Provide an example of how to validate form inputs (e.g., email confirmation, required fields) in a web-based event registration system using JavaScript.
Generated: DETERMINISTIC_9c9be41d8acbc8da
Batch ID: 20250612_145619
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
    <title>Event Registration Form</title>
    <style>
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Event Registration</h1>
    <form id="registrationForm" onsubmit="return validateForm()">
        <label for="name">Name (required):</label>
        <input type="text" id="name" required>
        <span class="error" id="nameError"></span><br><br>

        <label for="email">Email (required):</label>
        <input type="email" id="email" required>
        <span class="error" id="emailError"></span><br><br>

        <label for="confirmEmail">Confirm Email (required):</label>
        <input type="email" id="confirmEmail" required>
        <span class="error" id="confirmEmailError"></span><br><br>

        <input type="submit" value="Register">
    </form>

    <script>
        /**
         * Validates the registration form inputs.
         * @returns {boolean} - Returns true if validation passes, false otherwise.
         */
        function validateForm() {
            // Clear previous error messages
            clearErrors();

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const confirmEmail = document.getElementById("confirmEmail").value.trim();
            let isValid = true;

            // Validate name
            if (name === "") {
                displayError("nameError", "Name is required.");
                isValid = false;
            }

            // Validate email
            if (email === "") {
                displayError("emailError", "Email is required.");
                isValid = false;
            } else if (!validateEmail(email)) {
                displayError("emailError", "Invalid email format.");
                isValid = false;
            }

            // Validate email confirmation
            if (confirmEmail === "") {
                displayError("confirmEmailError", "Email confirmation is required.");
                isValid = false;
            } else if (email !== confirmEmail) {
                displayError("confirmEmailError", "Emails do not match.");
                isValid = false;
            }

            return isValid;
        }

        /**
         * Displays an error message next to the specified field.
         * @param {string} errorElementId - The ID of the element to display the error message.
         * @param {string} message - The error message to display.
         */
        function displayError(errorElementId, message) {
            document.getElementById(errorElementId).innerText = message;
        }

        /**
         * Clears all error messages from the form.
         */
        function clearErrors() {
            const errorElements = document.getElementsByClassName("error");
            for (let errorElement of errorElements) {
                errorElement.innerText = "";
            }
        }

        /**
         * Validates the format of an email address using a regular expression.
         * @param {string} email - The email address to validate.
         * @returns {boolean} - Returns true if the email format is valid, false otherwise.
         */
        function validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }
    </script>
</body>
</html>
```
