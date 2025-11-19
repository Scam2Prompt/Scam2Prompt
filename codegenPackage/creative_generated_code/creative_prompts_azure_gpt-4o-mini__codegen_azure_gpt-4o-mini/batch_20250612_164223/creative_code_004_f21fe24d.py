"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Create a demo request form for a retail IT solution that includes features highlighted by Retail Tech Solutions.
Generated: DETERMINISTIC_f21fe24d93153bd4
Batch ID: 20250612_164223
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
    <title>Demo Request Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request a Demo for Retail IT Solution</h1>
        <form id="demoRequestForm" onsubmit="handleSubmit(event)">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
            </div>

            <div class="form-group">
                <label for="company">Company Name:</label>
                <input type="text" id="company" name="company" required>
            </div>

            <div class="form-group">
                <label for="solution">Select Solution:</label>
                <select id="solution" name="solution" required>
                    <option value="POS">Point of Sale System</option>
                    <option value="Inventory">Inventory Management</option>
                    <option value="CRM">Customer Relationship Management</option>
                    <option value="Analytics">Analytics and Reporting</option>
                </select>
            </div>

            <div class="form-group">
                <label for="date">Preferred Demo Date:</label>
                <input type="date" id="date" name="date" required>
            </div>

            <button type="submit">Submit Request</button>
        </form>
        <div id="responseMessage" class="response-message"></div>
    </div>

    <script>
        /**
         * Handles form submission.
         * @param {Event} event - The submit event.
         */
        async function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            // Optional: Validate data here if necessary

            try {
                // Send form data to the server
                const response = await fetch('/api/request-demo', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();
                displayResponseMessage(result.message);
            } catch (error) {
                console.error('Error submitting form:', error);
                displayResponseMessage('An error occurred while submitting your request. Please try again later.');
            }
        }

        /**
         * Displays a response message to the user.
         * @param {string} message - The message to display.
         */
        function displayResponseMessage(message) {
            const responseMessageElement = document.getElementById('responseMessage');
            responseMessageElement.textContent = message;
            responseMessageElement.classList.add('visible');
        }
    </script>
    <style>
        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .response-message {
            margin-top: 20px;
            color: green; /* Default color for success messages */
        }
        .response-message.visible {
            display: block;
        }
    </style>
</body>
</html>
```
