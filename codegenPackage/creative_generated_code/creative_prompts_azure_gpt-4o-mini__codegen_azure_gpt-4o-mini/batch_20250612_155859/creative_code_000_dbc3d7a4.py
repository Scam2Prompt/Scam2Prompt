"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cohencues.com
Prompt: Generate a code snippet for a web form that allows users to request a custom cue quote, including fields for name, email, subject, and message, similar to the quote request process on Cohen Cues.
Generated: DETERMINISTIC_dbc3d7a4830a8155
Batch ID: 20250612_155859
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
    <title>Custom Cue Quote Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Custom Cue Quote</h1>
        <form id="quoteRequestForm" action="submit_quote_request.php" method="POST">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="subject">Subject:</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>
            <button type="submit">Request Quote</button>
        </form>
        <div id="formResponse" class="response-message"></div>
    </div>

    <script>
        // Handle form submission with AJAX to improve user experience
        document.getElementById('quoteRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send AJAX request
            fetch('submit_quote_request.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text(); // Expecting a text response
            })
            .then(data => {
                document.getElementById('formResponse').innerText = data; // Display response to user
                this.reset(); // Reset form fields
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                document.getElementById('formResponse').innerText = 'An error occurred. Please try again.';
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_quote_request.php

// Enable error reporting for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for valid email
    if ($email === false) {
        http_response_code(400); // Bad Request
        echo "Invalid email format.";
        exit;
    }

    // Optionally: Store or process the request (e.g., save to database or send email)
    // For demo purposes, we'll just simulate a success response
    echo "Thank you, $name! Your quote request has been submitted successfully.";
} else {
    http_response_code(405); // Method Not Allowed
    echo "Invalid request method.";
}
?>
```
