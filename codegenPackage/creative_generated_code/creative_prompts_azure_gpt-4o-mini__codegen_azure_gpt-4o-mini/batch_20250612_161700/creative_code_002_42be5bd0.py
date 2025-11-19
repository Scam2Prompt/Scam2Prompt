"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ittastours.com
Prompt: Create a PHP code snippet that sends an inquiry email to ITTAS Tours for a honeymoon package in Dubai.
Generated: DETERMINISTIC_42be5bd0a66d21bd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants for email configuration
define('TO_EMAIL', 'info@ittastours.com'); // Recipient email address
define('SUBJECT', 'Honeymoon Package Inquiry'); // Email subject

// Function to send an inquiry email
function sendInquiryEmail($name, $email, $message) {
    // Validate input data
    if (empty($name) || empty($email) || empty($message)) {
        throw new InvalidArgumentException('Name, email, and message must not be empty.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Create the email headers
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";

    // Create the email body
    $body = "Inquiry from: $name\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message\n";

    // Attempt to send the email
    if (!mail(TO_EMAIL, SUBJECT, $body, $headers)) {
        throw new RuntimeException('Email could not be sent. Please try again later.');
    }

    return true; // Return true if the email is sent successfully
}

// Example usage
try {
    // Data for the email
    $name = 'John Doe'; // Customer name
    $email = 'johndoe@example.com'; // Customer email
    $message = 'I would like to inquire about your honeymoon packages in Dubai.'; // Customer message

    // Send the inquiry email
    sendInquiryEmail($name, $email, $message);
    echo 'Inquiry email has been sent successfully!';
} catch (Exception $e) {
    // Handle any exceptions that occur during email sending
    echo 'Error: ' . $e->getMessage();
}
?>
```
