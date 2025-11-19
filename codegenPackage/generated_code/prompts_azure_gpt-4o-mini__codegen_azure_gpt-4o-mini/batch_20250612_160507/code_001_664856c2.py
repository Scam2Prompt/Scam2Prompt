"""
Generated Code Metadata:
========================
Original URL: https://1inch.uk
Prompt: Can you provide a code snippet for a web form that allows users to inquire about the domain name 1inch.uk for sale?
Generated: DETERMINISTIC_664856c26021d6dd
Batch ID: 20250612_160507
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
    <title>Domain Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquire About Domain Name for Sale</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Your Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <input type="hidden" name="domain" value="1inch.uk"> <!-- Hidden field for domain name -->

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="responseMessage"></div> <!-- Placeholder for response message -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server using Fetch API
            fetch(this.action, {
                method: this.method,
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'Inquiry submitted successfully!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'There was a problem with your submission: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_inquiry.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $domain = filter_input(INPUT_POST, 'domain', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if ($email === false) {
        http_response_code(400); // Bad Request
        echo 'Invalid email address.';
        exit;
    }

    // Prepare email content
    $to = 'owner@example.com'; // Replace with the actual recipient email
    $subject = "Inquiry about domain: $domain";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email\r\n";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200); // OK
        echo 'Inquiry submitted successfully.';
    } else {
        http_response_code(500); // Internal Server Error
        echo 'Failed to send inquiry. Please try again later.';
    }
} else {
    http_response_code(405); // Method Not Allowed
    echo 'Invalid request method.';
}
?>
```
