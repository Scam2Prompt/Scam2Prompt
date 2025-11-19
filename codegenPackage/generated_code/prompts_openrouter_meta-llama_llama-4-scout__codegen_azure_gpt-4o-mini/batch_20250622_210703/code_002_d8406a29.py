"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Generate a code snippet in JavaScript to create a simple eye care newsletter subscription form, similar to the one found on eyemagazine.gr.
Generated: DETERMINISTIC_d8406a290255a589
Batch ID: 20250622_210703
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
    <title>Eye Care Newsletter Subscription</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
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
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #218838;
        }
        .message {
            margin-top: 15px;
            font-size: 14px;
            color: #d9534f;
        }
    </style>
</head>
<body>

<div class="subscription-form">
    <h2>Subscribe to Our Eye Care Newsletter</h2>
    <form id="newsletterForm">
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
        </div>
        <button type="submit">Subscribe</button>
        <div class="message" id="message"></div>
    </form>
</div>

<script>
    // Function to handle form submission
    document.getElementById('newsletterForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const emailInput = document.getElementById('email');
        const messageDiv = document.getElementById('message');
        const email = emailInput.value.trim();

        // Validate email format
        if (!validateEmail(email)) {
            messageDiv.textContent = 'Please enter a valid email address.';
            return;
        }

        // Simulate an API call to subscribe the user
        subscribeUser(email)
            .then(response => {
                messageDiv.textContent = 'Thank you for subscribing!';
                messageDiv.style.color = '#28a745'; // Green color for success
                emailInput.value = ''; // Clear the input field
            })
            .catch(error => {
                messageDiv.textContent = 'Subscription failed. Please try again later.';
                console.error('Subscription error:', error);
            });
    });

    // Function to validate email format using a regular expression
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Simulated API call to subscribe the user
    function subscribeUser(email) {
        return new Promise((resolve, reject) => {
            // Simulate a network request with a timeout
            setTimeout(() => {
                // Randomly resolve or reject to simulate success or failure
                Math.random() > 0.2 ? resolve() : reject(new Error('Network error'));
            }, 1000);
        });
    }
</script>

</body>
</html>
```
