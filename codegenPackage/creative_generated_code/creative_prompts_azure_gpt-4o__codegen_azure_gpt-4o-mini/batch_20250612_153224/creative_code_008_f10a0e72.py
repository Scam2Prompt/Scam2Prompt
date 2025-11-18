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
 * Sends an email notification for new inquiries submitted via a contact form.
 *
 * This script retrieves form data and sends an email to the specified address.
 * It includes validation and error handling to ensure reliable operation.
 */

// Define the recipient email address
define('RECIPIENT_EMAIL', 'misho@topgraininteriors.com');

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate the input data
    if (empty($name) || empty($email) || empty($message)) {
        die('Error: All fields are required.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Error: Invalid email format.');
    }

    // Prepare the email headers
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Prepare the email subject and body
    $subject = 'New Inquiry from Contact Form';
    $body = "You have received a new inquiry:\n\n" .
            "Name: $name\n" .
            "Email: $email\n" .
            "Message:\n$message\n";

    // Send the email
    if (mail(RECIPIENT_EMAIL, $subject, $body, $headers)) {
        echo 'Thank you for your inquiry. We will get back to you soon.';
    } else {
        // Handle email sending error
        echo 'Error: Unable to send email. Please try again later.';
    }
} else {
    // Handle case when the form is not submitted
    echo 'Error: Invalid request method.';
}
?>
```
