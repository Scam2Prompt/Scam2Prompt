"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Create a PHP script to handle email inquiries sent to preowned.royalenfield@gmail.com, including validation for email and message fields.
Generated: DETERMINISTIC_aac57ef535119a77
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// email_handler.php

// Define constants for the email recipient and subject
define('EMAIL_RECIPIENT', 'preowned.royalenfield@gmail.com');
define('EMAIL_SUBJECT', 'New Inquiry from Website');

// Function to validate email address
function validateEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Function to validate message content
function validateMessage($message) {
    return !empty(trim($message));
}

// Function to send email
function sendEmail($name, $email, $message) {
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send the email and return the result
    return mail(EMAIL_RECIPIENT, EMAIL_SUBJECT, $message, $headers);
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize input data
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = htmlspecialchars(trim($_POST['email'] ?? ''));
    $message = htmlspecialchars(trim($_POST['message'] ?? ''));

    // Validate email and message
    if (!validateEmail($email)) {
        echo json_encode(['status' => 'error', 'message' => 'Invalid email address.']);
        exit;
    }

    if (!validateMessage($message)) {
        echo json_encode(['status' => 'error', 'message' => 'Message cannot be empty.']);
        exit;
    }

    // Attempt to send the email
    if (sendEmail($name, $email, $message)) {
        echo json_encode(['status' => 'success', 'message' => 'Email sent successfully!']);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Failed to send email. Please try again later.']);
    }
} else {
    // Handle invalid request method
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}
?>
```

**Usage:**
- This script should be placed on a server with PHP support.
- Ensure that the server is configured to send emails (e.g., using sendmail or SMTP).
- The script expects a POST request with `name`, `email`, and `message` fields.
