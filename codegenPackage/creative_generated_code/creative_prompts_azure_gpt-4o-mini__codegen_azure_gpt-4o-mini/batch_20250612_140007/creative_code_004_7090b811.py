"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Design a simple HTML form for customers to submit inquiries about christening dresses and boys baptism outfits, including fields for name, email, and message.
Generated: DETERMINISTIC_7090b811dbf31943
Batch ID: 20250612_140007
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
    <title>Inquiry Form for Christening Dresses and Baptism Outfits</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Inquire About Christening Dresses and Boys Baptism Outfits</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST" novalidate>
            <div class="form-group">
                <label for="name">Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">
            </div>

            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">
            </div>

            <div class="form-group">
                <label for="message">Message <span class="required">*</span></label>
                <textarea id="message" name="message" required placeholder="Enter your message" rows="5"></textarea>
            </div>

            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
            </div>
        </form>
        <div id="formFeedback" class="form-feedback"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Simple client-side validation
            let valid = this.checkValidity();
            if (!valid) {
                document.getElementById('formFeedback').innerText = "Please fill out all required fields.";
                return;
            }

            // Perform AJAX submission (optional)
            const formData = new FormData(this);
            fetch('submit_inquiry.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok.');
                return response.text();
            })
            .then(data => {
                document.getElementById('formFeedback').innerText = "Inquiry submitted successfully!";
                this.reset(); // Reset the form on successful submission
            })
            .catch(error => {
                document.getElementById('formFeedback').innerText = "There was a problem with your submission: " + error.message;
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
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad request
        echo "Invalid email format.";
        exit;
    }

    // Process the inquiry (e.g., save to database, send email, etc.)
    // Example: Sending an email (this requires a configured mail server)
    $to = 'your-email@example.com'; // Change to your email
    $subject = 'New Inquiry about Christening Dresses and Baptism Outfits';
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Inquiry successfully submitted.";
    } else {
        http_response_code(500); // Internal server error
        echo "Failed to send inquiry.";
    }
} else {
    // Respond with a 405 Method Not Allowed error if not a POST request
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```
