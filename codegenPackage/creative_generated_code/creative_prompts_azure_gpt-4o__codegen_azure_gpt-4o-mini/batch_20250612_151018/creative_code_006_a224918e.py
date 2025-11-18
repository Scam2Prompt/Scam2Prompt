"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a newsletter subscription form using JavaScript that mimics the functionality described on Joe Previte's website, including email validation and submission.
Generated: DETERMINISTIC_a224918ea14e5a4d
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
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .subscription-form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        .form-group button:hover {
            background-color: #218838;
        }
        .message {
            margin-top: 10px;
            font-size: 1em;
        }
    </style>
</head>
<body>

    <div class="subscription-form">
        <h2>Subscribe to Our Newsletter</h2>
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" placeholder="Enter your email" required>
        </div>
        <div class="form-group">
            <button id="subscribeButton">Subscribe</button>
        </div>
        <div class="message" id="message"></div>
    </div>

    <script>
        // Function to validate email format
        function validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }

        // Function to handle the subscription form submission
        function handleSubscription(event) {
            event.preventDefault(); // Prevent the default form submission

            const emailInput = document.getElementById('email');
            const messageDiv = document.getElementById('message');
            const email = emailInput.value.trim();

            // Clear previous messages
            messageDiv.textContent = '';

            // Validate the email input
            if (!validateEmail(email)) {
                messageDiv.textContent = 'Please enter a valid email address.';
                messageDiv.style.color = 'red';
                return;
            }

            // Simulate a network request to submit the email
            try {
                // Normally you'd send a request to your server here
                // Example: fetch('/subscribe', { method: 'POST', body: JSON.stringify({ email }) });

                // Simulate success response
                setTimeout(() => {
                    messageDiv.textContent = 'Thank you for subscribing!';
                    messageDiv.style.color = 'green';
                    emailInput.value = ''; // Clear the input field
                }, 1000);
            } catch (error) {
                // Handle any errors that occur during submission
                messageDiv.textContent = 'An error occurred while subscribing. Please try again later.';
                messageDiv.style.color = 'red';
                console.error('Subscription error:', error);
            }
        }

        // Attach event listener to the subscribe button
        document.getElementById('subscribeButton').addEventListener('click', handleSubscription);
    </script>

</body>
</html>
```
