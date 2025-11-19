"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patwacompany.com
Prompt: Develop a simple HTML form for users to subscribe to special offers from Patwa And Company, ensuring it captures their email address.
Generated: DETERMINISTIC_52d179c8f011a5c0
Batch ID: 20250612_163051
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
    <title>Subscribe to Special Offers</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>

    <div class="container">
        <h1>Subscribe to Special Offers from Patwa And Company</h1>
        <form id="subscriptionForm" action="/subscribe" method="POST">
            <!-- Input field for email address -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email" aria-describedby="emailHelp">

            <button type="submit">Subscribe</button>
        </form>
        <p id="message" aria-live="polite"></p> <!-- Placeholder for messages to the user -->
    </div>

    <script>
        // Listen for the form submission
        document.getElementById('subscriptionForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form from submitting immediately

            const emailInput = document.getElementById('email').value; // Get the email input

            // Validate the email format
            if (validateEmail(emailInput)) {
                // Send the subscription request
                fetch('/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json' // Specify content type
                    },
                    body: JSON.stringify({ email: emailInput }) // Send email as JSON
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    return response.json(); // Parse JSON response
                })
                .then(data => {
                    document.getElementById('message').textContent = data.message; // Display success message
                })
                .catch(error => {
                    document.getElementById('message').textContent = 'Error: ' + error.message; // Display error message
                });
            } else {
                document.getElementById('message').textContent = 'Please enter a valid email address.'; // Error message for invalid email
            }
        });

        // Function to validate email format
        function validateEmail(email) {
            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex
            return regex.test(email);
        }
    </script>

</body>
</html>
```
