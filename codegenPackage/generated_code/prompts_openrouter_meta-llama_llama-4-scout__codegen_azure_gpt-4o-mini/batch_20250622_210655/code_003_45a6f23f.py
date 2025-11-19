"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Create a code snippet for a simple contact form validation using JavaScript, similar to the one on the TWM Associates website."
Generated: DETERMINISTIC_45a6f23ffbef2138
Batch ID: 20250622_210655
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
    <title>Contact Form Validation</title>
    <style>
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <span class="error" id="nameError"></span>
        <br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <span class="error" id="emailError"></span>
        <br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <span class="error" id="messageError"></span>
        <br>

        <button type="submit">Submit</button>
    </form>

    <script>
        // Function to validate the contact form
        function validateForm(event) {
            // Prevent the default form submission
            event.preventDefault();

            // Clear previous error messages
            clearErrors();

            // Get form field values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Initialize a flag for form validity
            let isValid = true;

            // Validate name
            if (name === "") {
                showError('nameError', 'Name is required.');
                isValid = false;
            }

            // Validate email
            if (email === "") {
                showError('emailError', 'Email is required.');
                isValid = false;
            } else if (!isValidEmail(email)) {
                showError('emailError', 'Please enter a valid email address.');
                isValid = false;
            }

            // Validate message
            if (message === "") {
                showError('messageError', 'Message is required.');
                isValid = false;
            }

            // If the form is valid, you can proceed with form submission (e.g., send data to server)
            if (isValid) {
                alert('Form submitted successfully!');
                // Here you can add code to send the form data to the server
            }
        }

        // Function to show error messages
        function showError(elementId, message) {
            const errorElement = document.getElementById(elementId);
            errorElement.textContent = message;
        }

        // Function to clear error messages
        function clearErrors() {
            const errorElements = document.querySelectorAll('.error');
            errorElements.forEach(element => {
                element.textContent = '';
            });
        }

        // Function to validate email format
        function isValidEmail(email) {
            // Simple regex for email validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }

        // Attach the validateForm function to the form's submit event
        document.getElementById('contactForm').addEventListener('submit', validateForm);
    </script>
</body>
</html>
```
