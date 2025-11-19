"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gam3searly.pages.dev
Prompt: Develop a simple HTML form for users to enter their invite code for early access on a gaming site like GAM3S.GG.
Generated: DETERMINISTIC_99192b94b1650233
Batch ID: 20250612_162207
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
    <title>Early Access Invite Code</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Early Access Invite Code</h1>
        <form id="inviteForm" onsubmit="return handleSubmit(event)">
            <label for="inviteCode">Enter your invite code:</label>
            <input type="text" id="inviteCode" name="inviteCode" required minlength="6" maxlength="12" pattern="[A-Za-z0-9]+" title="Invite code must be 6-12 alphanumeric characters.">
            <button type="submit">Submit</button>
        </form>
        <p id="message" class="message"></p> <!-- Container for messages -->
    </div>

    <script>
        /**
         * Handles form submission for the invite code.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent the default form submission

            // Get the invite code from the input field
            const inviteCode = document.getElementById('inviteCode').value.trim();

            // Basic validation (this can be expanded as needed)
            if (inviteCode.length < 6 || inviteCode.length > 12) {
                displayMessage('Invite code must be between 6 and 12 characters.', 'error');
                return false;
            }

            // Simulate an API call to validate the invite code
            fakeApiCall(inviteCode)
                .then(response => {
                    if (response.success) {
                        displayMessage('Invite code accepted! Welcome to GAM3S.GG!', 'success');
                    } else {
                        displayMessage('Invalid invite code. Please try again.', 'error');
                    }
                })
                .catch(error => {
                    displayMessage(`Error: ${error.message}`, 'error');
                });

            return false; // Prevent form submission
        }

        /**
         * Fake API call to simulate server response for the invite code.
         * @param {string} code - The invite code to validate.
         * @returns {Promise} - A promise that resolves with a simulated response.
         */
        function fakeApiCall(code) {
            return new Promise((resolve) => {
                setTimeout(() => {
                    // Simulate success for a specific invite code, otherwise fail
                    const validCodes = ['ABC123', 'XYZ789'];
                    resolve({ success: validCodes.includes(code) });
                }, 1000); // Simulate network delay
            });
        }

        /**
         * Displays a message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayMessage(message, type) {
            const messageElement = document.getElementById('message');
            messageElement.textContent = message;
            messageElement.className = type; // Set class based on message type
        }
    </script>

    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
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
        .message {
            margin-top: 10px;
            text-align: center;
        }
        .success {
            color: #28a745;
        }
        .error {
            color: #dc3545;
        }
    </style>
</body>
</html>
```
