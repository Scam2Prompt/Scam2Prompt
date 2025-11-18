"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgraininteriors.com
Prompt: Provide a PHP script to send email notifications for new inquiries submitted via a contact form, using the email address "misho@topgraininteriors.com".
Generated: DETERMINISTIC_f10a0e7215f37480
Batch ID: 20250612_153224
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
 * Contact Form Email Notification Script
 * 
 * This script handles sending email notifications for new inquiries submitted 
 * via a contact form. It uses PHP's mail() function to send an email to the 
 * specified recipient.
 * 
 * Author: Expert Programmer
 * Email: misho@topgraininteriors.com
 */

// Define the recipient email address
define('RECIPIENT_EMAIL', 'misho@topgraininteriors.com');

// Check if the form was submitted via POST method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize user input
    $name = isset($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : null;
    $email = isset($_POST['email']) ? htmlspecialchars(trim($_POST['email'])) : null;
    $message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message'])) : null;

    // Ensure all required fields are provided
    if (!$name || !$email || !$message) {
        http_response_code(400); // Bad Request
        echo "Error: All fields are required.";
        exit;
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request
        echo "Error: Invalid email format.";
        exit;
    }

    // Prepare the email headers
    $headers = "From: noreply@topgraininteriors.com\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";

    // Prepare the email subject and body
    $subject = "New Inquiry from Contact Form";
    $body = "You have received a new inquiry from the contact form:\n\n";
    $body .= "Name: " . $name . "\n";
    $body .= "Email: " . $email . "\n\n";
    $body .= "Message:\n" . $message . "\n";

    // Send the email
    if (mail(RECIPIENT_EMAIL, $subject, $body, $headers)) {
        http_response_code(200); // OK
        echo "Thank you! Your inquiry has been sent.";
    } else {
        http_response_code(500); // Internal Server Error
        echo "Error: Failed to send your inquiry. Please try again later.";
    }
} else {
    // Reject requests that are not POST
    http_response_code(405); // Method Not Allowed
    echo "Error: Only POST requests are allowed.";
}
?>
```
