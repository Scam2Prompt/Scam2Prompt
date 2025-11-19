"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Develop a code example in PHP for creating a simple email sending functionality, similar to the "Send a Message" feature on the website, using a mail server for sending emails to the counselor.
Generated: DETERMINISTIC_f6082f6ef29002a4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Email sending functionality in PHP

// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_PORT', 587);               // Replace with your SMTP port (e.g., 587 for TLS)
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your email address
define('SMTP_PASSWORD', 'your_password');         // Replace with your email password
define('COUNSELOR_EMAIL', 'counselor@example.com'); // Replace with the counselor's email address

// Function to send an email
function sendEmail($from, $subject, $message) {
    // Validate input
    if (empty($from) || empty($subject) || empty($message)) {
        throw new InvalidArgumentException('All fields are required.');
    }

    // Sanitize input
    $from = filter_var($from, FILTER_SANITIZE_EMAIL);
    $subject = htmlspecialchars($subject, ENT_QUOTES, 'UTF-8');
    $message = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');

    // Check if the email is valid
    if (!filter_var($from, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email address.');
    }

    // Create email headers
    $headers = "From: $from\r\n";
    $headers .= "Reply-To: $from\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Use PHP's mail function to send the email
    $success = mail(COUNSELOR_EMAIL, $subject, $message, $headers);

    // Check if the email was sent successfully
    if (!$success) {
        throw new RuntimeException('Failed to send email.');
    }

    return true;
}

// Example usage
try {
    // Replace these values with user input
    $userEmail = 'user@example.com';
    $emailSubject = 'Request for Counseling';
    $emailMessage = 'Hello, I would like to schedule a counseling session.';

    // Send the email
    sendEmail($userEmail, $emailSubject, $emailMessage);

    echo 'Email sent successfully.';
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
}
?>
```
