"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Write a PHP script to send an email using InfinityFree hosting, ensuring compatibility with its server settings.
Generated: DETERMINISTIC_f556b3358b9f3fff
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Send an email using PHP's mail function.
 * This script is designed to work with InfinityFree hosting.
 * Ensure that your email settings are configured correctly in your InfinityFree account.
 */

// Function to send an email
function sendEmail($to, $subject, $message, $headers) {
    // Check if the email address is valid
    if (!filter_var($to, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("The provided email address is invalid.");
    }

    // Use mail() function to send the email
    $success = mail($to, $subject, $message, $headers);

    // Check if the mail function succeeded
    if (!$success) {
        // Log the error for debugging
        error_log("Email sending failed to: $to");
        throw new Exception("Email could not be sent. Please try again later.");
    }

    return true;
}

// Main script execution
try {
    // Define the recipient email address
    $to = 'recipient@example.com'; // Replace with the actual recipient's email address

    // Define the email subject
    $subject = 'Test Email from InfinityFree';

    // Define the email message
    $message = 'This is a test email sent using PHP mail function.';

    // Define the email headers
    $headers = 'From: sender@example.com' . "\r\n" . // Replace with your sending email address
               'Reply-To: sender@example.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    // Send the email
    sendEmail($to, $subject, $message, $headers);

    // Success message
    echo "Email sent successfully to $to.";
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo 'Error: ' . $e->getMessage();
} catch (InvalidArgumentException $e) {
    // Handle invalid email argument exception
    echo 'Invalid Argument: ' . $e->getMessage();
}
?>
```
