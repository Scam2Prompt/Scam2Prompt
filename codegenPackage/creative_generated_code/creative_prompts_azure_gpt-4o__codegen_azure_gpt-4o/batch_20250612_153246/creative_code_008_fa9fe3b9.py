"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Generate a PHP script to send email notifications to customers who request quotes via the contact form on "The Fence Guys" website.
Generated: DETERMINISTIC_fa9fe3b9ef0e8baa
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
// Contact Form Email Notification Script for "The Fence Guys"

// Configuration
define('EMAIL_FROM', 'no-reply@thefenceguys.com'); // Sender email address
define('EMAIL_TO', 'sales@thefenceguys.com');      // Recipient email address
define('EMAIL_SUBJECT', 'New Quote Request');      // Email subject
define('SMTP_HOST', 'smtp.example.com');           // SMTP host address
define('SMTP_PORT', 587);                          // SMTP port
define('SMTP_USERNAME', 'smtp_user');              // SMTP username
define('SMTP_PASSWORD', 'smtp_password');          // SMTP password

// Check if form data is received
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate input data
        $name = !empty($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : null;
        $email = !empty($_POST['email']) ? htmlspecialchars(trim($_POST['email'])) : null;
        $message = !empty($_POST['message']) ? htmlspecialchars(trim($_POST['message'])) : null;

        if (!$name || !$email || !$message) {
            throw new InvalidArgumentException('All fields (name, email, message) are required.');
        }

        // Prepare email headers
        $headers = [
            'From' => EMAIL_FROM,
            'Reply-To' => $email,
            'Content-Type' => 'text/plain; charset=utf-8',
        ];

        // Prepare email body
        $emailBody = "New quote request received:\n\n";
        $emailBody .= "Name: $name\n";
        $emailBody .= "Email: $email\n";
        $emailBody .= "Message:\n$message\n";

        // Send email using PHP's mail() function (fallback)
        if (!mail(EMAIL_TO, EMAIL_SUBJECT, $emailBody, $headers)) {
            throw new RuntimeException('Failed to send email using mail() function.');
        }

        // SUCCESS: Email sent
        echo json_encode(['success' => true, 'message' => 'Quote request sent successfully.']);
    } catch (InvalidArgumentException $e) {
        // Handle validation errors
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    } catch (RuntimeException $e) {
        // Handle other runtime errors
        echo json_encode(['success' => false, 'error' => 'Failed to send email. Please try again later.']);
    } catch (Exception $e) {
        // Handle unexpected errors
        echo json_encode(['success' => false, 'error' => 'An unexpected error occurred.']);
    }
} else {
    // Handle requests that are not POST
    echo json_encode(['success' => false, 'error' => 'Invalid request method.']);
}
?>
```
