"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Write a newsletter subscription form in JavaScript that matches the functionality described on Joe Previte's webpage.
Generated: DETERMINISTIC_21f176e9d41c67bb
Batch ID: 20250612_151018
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
    <title>Newsletter Subscription</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            max-width: 400px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .success {
            color: green;
            font-size: 1em;
        }
    </style>
</head>
<body>

    <h1>Subscribe to our Newsletter</h1>
    <form id="subscriptionForm">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" required>
            <div id="emailError" class="error"></div>
        </div>
        <button type="submit">Subscribe</button>
        <div id="formMessage" class="success"></div>
    </form>

    <script>
        // Get form elements
        const form = document.getElementById('subscriptionForm');
        const emailInput = document.getElementById('email');
        const emailError = document.getElementById('emailError');
        const formMessage = document.getElementById('formMessage');

        // Form submit event handler
        form.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            // Clear previous messages
            emailError.textContent = '';
            formMessage.textContent = '';

            // Validate email format
            const emailValue = emailInput.value.trim();
            if (!validateEmail(emailValue)) {
                emailError.textContent = 'Please enter a valid email address.';
                return;
            }

            // Simulate API call for subscription (replace with actual API call)
            try {
                const response = await subscribeEmail(emailValue);
                if (response.success) {
                    formMessage.textContent = 'Thank you for subscribing!';
                    emailInput.value = ''; // Clear input field
                } else {
                    emailError.textContent = response.message || 'An error occurred. Please try again.';
                }
            } catch (error) {
                emailError.textContent = 'An unexpected error occurred. Please try again later.';
                console.error('Error during subscription:', error); // Log error for debugging
            }
        });

        // Function to validate email format using regex
        function validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }

        // Simulated async function to mimic API subscription (to be replaced with a real API call)
        async function subscribeEmail(email) {
            // Simulate success response after a delay
            return new Promise((resolve) => {
                setTimeout(() => {
                    resolve({ success: true });
                }, 1000); // Simulated 1 second delay
            });
        }
    </script>

</body>
</html>
```
