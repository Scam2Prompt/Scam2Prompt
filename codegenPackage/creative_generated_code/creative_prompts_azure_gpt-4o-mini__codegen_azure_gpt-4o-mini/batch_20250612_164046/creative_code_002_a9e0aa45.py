"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketisillegal.com
Prompt: Provide an example of how to implement a subscription form in HTML and JavaScript for a website similar to polymarketisillegal.com to collect user emails.
Generated: DETERMINISTIC_a9e0aa454566e239
Batch ID: 20250612_164046
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
    <title>Subscription Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        .subscription-form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        input[type="email"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
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
    <h2>Subscribe to our Newsletter</h2>
    <form id="subscribeForm">
        <input type="email" id="email" placeholder="Enter your email" required>
        <button type="submit">Subscribe</button>
    </form>
    <div class="message" id="message"></div>
</div>

<script>
    // Function to handle form submission
    document.getElementById('subscribeForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission action

        const emailInput = document.getElementById('email');
        const messageDiv = document.getElementById('message');
        const email = emailInput.value;

        // Validate email format
        if (!validateEmail(email)) {
            showMessage("Please enter a valid email address.", true);
            return;
        }

        // Simulating an API request to send the email
        sendEmailSubscription(email)
            .then(() => {
                showMessage("Thank you for subscribing!", false);
                emailInput.value = ""; // Clear the input field
            })
            .catch(() => {
                showMessage("An error occurred. Please try again later.", true);
            });
    });

    // Function to validate email format
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Simulated function to send email subscription
    function sendEmailSubscription(email) {
        return new Promise((resolve, reject) => {
            // Simulating a network request with a timeout
            setTimeout(() => {
                // Simulate a successful response (for demo purposes)
                const success = true; // Change to false to simulate an error
                if (success) {
                    resolve();
                } else {
                    reject();
                }
            }, 1000);
        });
    }

    // Function to display messages
    function showMessage(message, isError) {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = message;
        messageDiv.className = isError ? 'error' : '';
    }
</script>

</body>
</html>
```
