"""
Generated Code Metadata:
========================
Original URL: https://test.netlify.app
Prompt: Write code to integrate a "Request a Call Back" feature into a website, including functionality for users to select the number of employees in their company, as seen on Acme's form.
Generated: DETERMINISTIC_cbf6ec8fd50644f7
Batch ID: 20250612_153648
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
    <title>Request a Call Back</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="callback-form-container">
        <h2>Request a Call Back</h2>
        <form id="callbackForm" onsubmit="return handleSubmit(event)">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="employees">Number of Employees:</label>
            <select id="employees" name="employees" required>
                <option value="" disabled selected>Select number of employees</option>
                <option value="1-10">1-10</option>
                <option value="11-50">11-50</option>
                <option value="51-200">51-200</option>
                <option value="201+">201+</option>
            </select>

            <button type="submit">Request Call Back</button>
        </form>
        <div id="responseMessage" class="response-message"></div>
    </div>

    <script>
        /**
         * Handles the form submission for the callback request.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                employees: document.getElementById('employees').value
            };

            // Validate form data
            if (!validateFormData(formData)) {
                displayMessage('Please fill in all fields correctly.', 'error');
                return false;
            }

            // Send data to the server
            sendCallbackRequest(formData);
            return false; // Prevent default form submission
        }

        /**
         * Validates the form data.
         * @param {Object} data - The form data to validate.
         * @returns {boolean} - Returns true if valid, false otherwise.
         */
        function validateFormData(data) {
            return data.name && data.email && data.employees;
        }

        /**
         * Sends the callback request to the server.
         * @param {Object} data - The form data to send.
         */
        async function sendCallbackRequest(data) {
            try {
                const response = await fetch('/api/request-callback', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const result = await response.json();
                displayMessage(result.message, 'success');
            } catch (error) {
                console.error('Error sending callback request:', error);
                displayMessage('There was an error processing your request. Please try again later.', 'error');
            }
        }

        /**
         * Displays a message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.className = type === 'success' ? 'success-message' : 'error-message';
        }
    </script>
    <style>
        .callback-form-container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .response-message {
            margin-top: 10px;
            padding: 10px;
            border-radius: 5px;
        }
        .success-message {
            color: green;
            border: 1px solid green;
        }
        .error-message {
            color: red;
            border: 1px solid red;
        }
    </style>
</body>
</html>
```
