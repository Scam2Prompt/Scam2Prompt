"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wholygood.com
Prompt: How can I create a subscription form for email updates like the one on wholygood.com? Provide a code example.
Generated: DETERMINISTIC_6b8c317b4fd75b4d
Batch ID: 20250612_155737
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
    <title>Email Subscription Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }
        .subscription-form {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="email"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 10px;
            color: green;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

    <div class="subscription-form">
        <h2>Subscribe for Updates</h2>
        <form id="subscriptionForm">
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <button type="submit">Subscribe</button>
        </form>
        <div class="message" id="message"></div>
        <div class="error" id="error"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('subscriptionForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const emailInput = document.getElementById('email');
            const messageElement = document.getElementById('message');
            const errorElement = document.getElementById('error');

            // Clear previous messages
            messageElement.textContent = '';
            errorElement.textContent = '';

            // Validate email format
            const email = emailInput.value.trim();
            if (!validateEmail(email)) {
                errorElement.textContent = 'Please enter a valid email address.';
                return;
            }

            // Simulate an API call to submit the email
            submitEmail(email)
                .then(response => {
                    messageElement.textContent = 'Thank you for subscribing!';
                })
                .catch(err => {
                    errorElement.textContent = 'An error occurred. Please try again later.';
                    console.error('Error during email submission:', err);
                });
        });

        // Function to validate email format
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }

        // Function to simulate an API call for email submission
        function submitEmail(email) {
            return new Promise((resolve, reject) => {
                // Simulate a successful submission after 1 second
                setTimeout(() => {
                    // You can replace this with actual AJAX call
                    if (email) {
                        resolve({ status: 'success' });
                    } else {
                        reject({ status: 'error' });
                    }
                }, 1000);
            });
        }
    </script>

</body>
</html>
```
