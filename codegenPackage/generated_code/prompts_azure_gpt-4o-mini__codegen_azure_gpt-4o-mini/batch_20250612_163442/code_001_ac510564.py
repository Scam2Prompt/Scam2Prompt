"""
Generated Code Metadata:
========================
Original URL: https://elon.vip
Prompt: Write a code snippet for a web form that allows users to make offers on domain names, inspired by the features on elon.vip.
Generated: DETERMINISTIC_ac510564f003bb4d
Batch ID: 20250612_163442
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
    <title>Domain Name Offer Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Make an Offer on a Domain Name</h1>
        <form id="offerForm" method="POST" action="/submit-offer">
            <label for="domainName">Domain Name:</label>
            <input type="text" id="domainName" name="domainName" required placeholder="e.g. example.com">

            <label for="offerAmount">Offer Amount ($):</label>
            <input type="number" id="offerAmount" name="offerAmount" required min="1" step="0.01" placeholder="Enter your offer amount">

            <label for="userEmail">Your Email:</label>
            <input type="email" id="userEmail" name="userEmail" required placeholder="e.g. user@example.com">

            <button type="submit">Submit Offer</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('offerForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this); // Gather form data

            try {
                const response = await fetch(this.action, {
                    method: this.method,
                    body: formData,
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }

                const result = await response.json(); // Parse JSON response
                displayMessage(result.message, 'success'); // Display success message
            } catch (error) {
                displayMessage('Error: ' + error.message, 'error'); // Display error message
            }
        });

        // Function to display messages to the user
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.className = type; // Set class for styling
            responseMessage.classList.remove('hidden'); // Show the message
        }
    </script>

    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
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
        }
        button:hover {
            background-color: #218838;
        }
        .hidden {
            display: none;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
    </style>
</body>
</html>
```
