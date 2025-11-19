"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Write a code snippet to create a request form for a paving service quote similar to the one on Bedford Paving's website.
Generated: DETERMINISTIC_0e7b99e622c79c03
Batch ID: 20250612_162806
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
    <title>Paving Service Quote Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Paving Service Quote</h1>
        <form id="quoteRequestForm">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(555) 555-5555">

            <label for="address">Service Address:</label>
            <input type="text" id="address" name="address" required placeholder="123 Main St, City, State, ZIP">

            <label for="details">Project Details:</label>
            <textarea id="details" name="details" rows="4" required placeholder="Provide details about your paving project..."></textarea>

            <button type="submit">Request Quote</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Placeholder for response message -->
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('quoteRequestForm').addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            const formData = new FormData(event.target);

            try {
                // Send the form data to the server
                const response = await fetch('/api/request-quote', {
                    method: 'POST',
                    body: formData,
                });

                // Check response status
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                // Parse JSON response
                const data = await response.json();

                // Display success message
                displayMessage(`Quote request submitted successfully! Reference ID: ${data.id}`, 'success');
            } catch (error) {
                // Handle errors and display error message
                displayMessage(`Error submitting quote request: ${error.message}`, 'error');
            }
        });

        // Function to display response messages
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.className = type; // Add class based on message type
            responseMessage.classList.remove('hidden'); // Show the message
        }
    </script>
    <style>
        /* Basic styles for the form */
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
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
