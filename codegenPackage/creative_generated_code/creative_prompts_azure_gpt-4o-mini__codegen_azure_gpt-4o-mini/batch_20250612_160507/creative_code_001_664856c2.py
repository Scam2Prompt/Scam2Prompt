"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.uk
Prompt: Can you provide a code snippet for a web form that allows users to inquire about the domain name 1inch.uk for sale?
Generated: DETERMINISTIC_664856c26021d6dd
Batch ID: 20250612_160507
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
    <title>Domain Inquiry Form - 1inch.uk</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <div class="container">
        <h1>Inquire About Domain Name - 1inch.uk</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST">
            <!-- Input for user's name -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <!-- Input for user's email -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <!-- Input for inquiry message -->
            <label for="message">Your Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <!-- Submit button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        // Form submission event listener
        document.getElementById('inquiryForm').addEventListener('submit', function (event) {
            // Validate the form before submission
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                alert('Please fill in all fields.');
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    </script>
</body>

</html>
```

```php
<?php
// submit_inquiry.php

// Check if the form is submitted via POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if (!$email) {
        die('Invalid email address.'); // Exit if email is not valid
    }

    // Prepare email for sending
    $to = 'owner@1inch.uk'; // Specify the recipient's email address
    $subject = 'Domain Inquiry for 1inch.uk';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        // Success message
        echo 'Your inquiry has been submitted successfully!';
    } else {
        // Error message
        echo 'There was an error sending your inquiry. Please try again later.';
    }
} else {
    // If accessed directly, deny access
    http_response_code(405); // Method Not Allowed
    echo 'Method not allowed.';
}
?>
```
