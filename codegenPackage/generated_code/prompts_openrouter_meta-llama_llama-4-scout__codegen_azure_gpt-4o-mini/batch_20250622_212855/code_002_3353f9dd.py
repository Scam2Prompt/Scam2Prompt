"""
Generated Code Metadata:
========================
Original URL: https://jhxdjhgvj.scarexpedition.top
Prompt: Generate a JavaScript code snippet that creates a simple webpage to collect user phone numbers and display a verification step, similar to the process described for receiving free 45GB data.
Generated: DETERMINISTIC_3353f9dd79556260
Batch ID: 20250622_212855
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
    <title>Phone Number Verification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .message {
            color: red;
            margin: 10px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Phone Number Verification</h2>
    <form id="phoneForm">
        <label for="phone">Enter your phone number:</label>
        <input type="text" id="phone" name="phone" placeholder="e.g. +1234567890" required>
        <input type="submit" value="Verify">
        <div class="message" id="message"></div>
    </form>
    <div id="verification" style="display:none;">
        <h3>Verification Step</h3>
        <p>A verification code has been sent to your phone number.</p>
        <label for="code">Enter verification code:</label>
        <input type="text" id="code" name="code" placeholder="Verification code" required>
        <input type="button" value="Submit Code" id="submitCode">
        <div class="message" id="codeMessage"></div>
    </div>
</div>

<script>
    // Function to handle form submission
    document.getElementById('phoneForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const phoneInput = document.getElementById('phone');
        const phoneNumber = phoneInput.value.trim();
        const messageDiv = document.getElementById('message');

        // Basic phone number validation
        const phoneRegex = /^\+\d{10,15}$/; // Example regex for international format
        if (!phoneRegex.test(phoneNumber)) {
            messageDiv.textContent = 'Please enter a valid phone number.';
            return;
        }

        // Simulate sending a verification code
        messageDiv.textContent = '';
        document.getElementById('verification').style.display = 'block';
        phoneInput.disabled = true; // Disable phone input after submission
    });

    // Function to handle verification code submission
    document.getElementById('submitCode').addEventListener('click', function() {
        const codeInput = document.getElementById('code');
        const verificationCode = codeInput.value.trim();
        const codeMessageDiv = document.getElementById('codeMessage');

        // Simulate verification code check (for demo purposes, we assume '123456' is the correct code)
        if (verificationCode === '123456') {
            codeMessageDiv.textContent = 'Phone number verified successfully!';
            codeMessageDiv.style.color = 'green';
        } else {
            codeMessageDiv.textContent = 'Invalid verification code. Please try again.';
            codeMessageDiv.style.color = 'red';
        }
    });
</script>

</body>
</html>
```
