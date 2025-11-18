"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Develop a PHP-based contact form that sends inquiries to the email address provided on the Apple Market Bali website (applemarketbali@gmail.com).
Generated: DETERMINISTIC_e7832885c4536c2a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Handler Script for Apple Market Bali

// Set the recipient email address
define('RECIPIENT_EMAIL', 'applemarketbali@gmail.com');

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate form inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Prepare response variables
    $errors = [];
    $success = false;

    // Validate required fields
    if (!$name) {
        $errors[] = 'Name is required.';
    }
    if (!$email) {
        $errors[] = 'Valid email address is required.';
    }
    if (!$message) {
        $errors[] = 'Message is required.';
    }

    // Proceed if no validation errors
    if (empty($errors)) {
        // Prepare email headers
        $headers = "From: {$email}\r\n";
        $headers .= "Reply-To: {$email}\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

        // Prepare email subject and body
        $subject = "New Contact Form Inquiry from {$name}";
        $email_body = "Name: {$name}\n";
        $email_body .= "Email: {$email}\n\n";
        $email_body .= "Message:\n{$message}\n";

        // Send email
        if (mail(RECIPIENT_EMAIL, $subject, $email_body, $headers)) {
            $success = true;
        } else {
            $errors[] = 'Failed to send the email. Please try again later.';
        }
    }

    // Return JSON response for AJAX or fetch API requests
    header('Content-Type: application/json');
    echo json_encode([
        'success' => $success,
        'errors' => $errors
    ]);
    exit;
}

?>

<!-- Simple HTML Contact Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Apple Market Bali</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Send Inquiry</button>
    </form>
</body>
</html>
```
