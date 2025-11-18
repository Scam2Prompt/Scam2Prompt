"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Write a PHP script to send an email inquiry to "turismo@marchigue.cl" using the contact information provided on the Turismo Marchigüe website.
Generated: DETERMINISTIC_fd1d8f7bcfaca437
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure you have an SMTP server configured or use a library like PHPMailer for production-grade email handling.
// This script uses native PHP mail() function for simplicity.

// Define the recipient email address
$recipient = 'turismo@marchigue.cl';

// Define the subject of the email
$subject = 'Inquiry from Turismo Marchigüe Website';

// Collect user input (this is just an example; in a real-world application, you'd validate and sanitize these inputs)
$user_name = 'John Doe'; // Replace with actual input from a form
$user_email = 'john.doe@example.com'; // Replace with actual input from a form
$user_message = 'Hello, I would like to inquire about tourism options available in Marchigüe.'; // Replace with actual input from a form

// Validate email address
if (!filter_var($user_email, FILTER_VALIDATE_EMAIL)) {
    die('Invalid email address.');
}

// Prepare email headers
$headers = "From: $user_name <$user_email>\r\n";
$headers .= "Reply-To: $user_email\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Prepare email message
$message = "You have received a new inquiry from the Turismo Marchigüe website.\n\n";
$message .= "Name: $user_name\n";
$message .= "Email: $user_email\n\n";
$message .= "Message:\n$user_message\n";

// Send the email
if (mail($recipient, $subject, $message, $headers)) {
    echo 'Email sent successfully.';
} else {
    echo 'Failed to send email.';
}
?>
```
