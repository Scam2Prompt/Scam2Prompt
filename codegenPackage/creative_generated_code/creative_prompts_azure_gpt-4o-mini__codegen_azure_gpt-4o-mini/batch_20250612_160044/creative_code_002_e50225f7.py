"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Create a PHP code snippet that submits a request to the Terminal Tunja contact email with user inquiries about the "Protocolo de bioseguridad."
Generated: DETERMINISTIC_e50225f71325107f
Batch ID: 20250612_160044
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
 * Sends an inquiry about "Protocolo de bioseguridad" to the Terminal Tunja contact email.
 */

// Define constants for email configuration
define('CONTACT_EMAIL', 'contact@terminaltunja.com'); // Replace with the actual contact email
define('EMAIL_SUBJECT', 'Inquiry about Protocolo de bioseguridad');

// Function to send email
function sendInquiryEmail($userName, $userEmail, $inquiryMessage) {
    // Validate input
    if (empty($userName) || empty($userEmail) || empty($inquiryMessage)) {
        throw new InvalidArgumentException('All fields are required.');
    }

    // Sanitize email
    $userEmail = filter_var($userEmail, FILTER_SANITIZE_EMAIL);
    if (!filter_var($userEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Construct email headers
    $headers = "From: $userName <$userEmail>\r\n";
    $headers .= "Reply-To: $userEmail\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Construct email body
    $emailBody = "User Name: $userName\n";
    $emailBody .= "User Email: $userEmail\n\n";
    $emailBody .= "Inquiry Message:\n$inquiryMessage\n";

    // Attempt to send the email
    if (!mail(CONTACT_EMAIL, EMAIL_SUBJECT, $emailBody, $headers)) {
        throw new RuntimeException('Error sending email. Please try again later.');
    }

    return true; // Email sent successfully
}

// Example usage
try {
    // These values would typically come from a form submission
    $name = 'John Doe';
    $email = 'john.doe@example.com';
    $message = 'I would like to know more about the Protocolo de bioseguridad.';

    // Send the inquiry email
    sendInquiryEmail($name, $email, $message);
    echo 'Inquiry sent successfully!';
} catch (Exception $e) {
    // Handle exceptions
    echo 'Error: ' . $e->getMessage();
}
?>
```
