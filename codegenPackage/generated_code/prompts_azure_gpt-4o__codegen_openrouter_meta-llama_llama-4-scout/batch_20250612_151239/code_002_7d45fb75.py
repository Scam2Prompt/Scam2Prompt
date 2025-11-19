"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.kesug.com
Prompt: Generate PHP code for a contact form that can be hosted on a service offering multiple PHP versions and SSL support, such as iFastNet. Ensure the form securely handles user input.
Generated: DETERMINISTIC_7d45fb759f74cc3f
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Contact Form Handler
 *
 * This script handles the contact form submission, validates user input,
 * and sends an email to the site administrator.
 */

// Configuration
$config = [
    'adminEmail' => 'your-admin-email@example.com',
    'siteName' => 'Your Site Name',
];

// Define a function to validate and sanitize user input
function validateInput($input)
{
    $input = trim($input);
    $input = htmlspecialchars($input);
    $input = strip_tags($input);
    return $input;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate and sanitize user input
        $name = validateInput($_POST['name']);
        $email = validateInput($_POST['email']);
        $message = validateInput($_POST['message']);

        // Validate email address
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email address');
        }

        // Prepare email content
        $subject = 'New Message from ' . $config['siteName'];
        $body = "Name: $name\nEmail: $email\n\n$message";

        // Send email to administrator
        $headers = 'From: ' . $email . "\r\n";
        mail($config['adminEmail'], $subject, $body, $headers);

        // Display success message
        echo json_encode(['success' => true, 'message' => 'Message sent successfully']);
    } catch (Exception $e) {
        // Display error message
        echo json_encode(['success' => false, 'message' => $e->getMessage()]);
    }
} else {
    // Display error message for invalid request method
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method Not Allowed']);
}

exit;
```

**index.html** (example usage)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Form</h1>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Send">
    </form>

    <script>
        const form = document.getElementById('contact-form');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);

            try {
                const response = await fetch('', {
                    method: 'POST',
                    body: formData,
                });

                const result = await response.json();

                if (result.success) {
                    alert(result.message);
                    form.reset();
                } else {
                    alert(result.message);
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
