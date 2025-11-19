"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftopesea-nft-logeen.godaddysites.com
Prompt: Develop a simple HTML form that allows users to sign up for discounts on NFT purchases, similar to the subscription feature highlighted on nftopesea-nft-logeen.
Generated: DETERMINISTIC_3b9c96607ab1aa9c
Batch ID: 20250612_162251
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
    <title>NFT Discount Signup</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Sign Up for NFT Discounts</h1>
        <form id="discount-signup-form" action="submit.php" method="POST" onsubmit="return validateForm()">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="interests">Interests (optional):</label>
            <textarea id="interests" name="interests" rows="4" placeholder="e.g. Art, Music, Gaming"></textarea>
            
            <button type="submit">Sign Up</button>
        </form>
        <div id="response-message" class="hidden"></div>
    </div>

    <script>
        /**
         * Validates the form inputs before submission.
         * @returns {boolean} True if the form is valid, false otherwise.
         */
        function validateForm() {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();

            if (name.length === 0) {
                displayMessage('Please enter your full name.', 'error');
                return false;
            }

            if (!validateEmail(email)) {
                displayMessage('Please enter a valid email address.', 'error');
                return false;
            }

            return true; // Form is valid
        }

        /**
         * Validates the email format.
         * @param {string} email - The email address to validate.
         * @returns {boolean} True if the email is valid, false otherwise.
         */
        function validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }

        /**
         * Displays a message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayMessage(message, type) {
            const responseMessageDiv = document.getElementById('response-message');
            responseMessageDiv.textContent = message;
            responseMessageDiv.className = type;
            responseMessageDiv.classList.remove('hidden');
        }
    </script>

    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        label {
            margin-top: 10px;
            display: block;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            margin-top: 15px;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
        .success {
            color: green;
            margin-top: 10px;
        }
        .hidden {
            display: none;
        }
    </style>
</body>
</html>
```
