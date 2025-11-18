"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Create a PHP script to handle email inquiries sent to preowned.royalenfield@gmail.com, including validation for email and message fields.
Generated: DETERMINISTIC_aac57ef535119a77
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
 * PHP Script to Handle Email Inquiries
 * This script accepts POST data, validates email and message fields,
 * and sends an email inquiry to preowned.royalenfield@gmail.com.
 */

// Configuration
define('RECIPIENT_EMAIL', 'preowned.royalenfield@gmail.com');
define('SUBJECT', 'Royal Enfield Inquiry');

// Function to sanitize input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Main logic
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Initialize response
    $response = [
        'success' => false,
        'message' => '',
    ];

    try {
        // Validate and sanitize email
        if (isset($_POST['email'])) {
            $email = sanitizeInput($_POST['email']);
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                throw new Exception('Invalid email address.');
            }
        } else {
            throw new Exception('Email field is required.');
        }

        // Validate and sanitize message
        if (isset($_POST['message'])) {
            $message = sanitizeInput($_POST['message']);
            if (empty($message)) {
                throw new Exception('Message field cannot be empty.');
            }
        } else {
            throw new Exception('Message field is required.');
        }

        // Prepare email headers
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

        // Send email
        $emailSent = mail(RECIPIENT_EMAIL, SUBJECT, $message, $headers);
        if (!$emailSent) {
            throw new Exception('Failed to send email. Please try again later.');
        }

        // Success response
        $response['success'] = true;
        $response['message'] = 'Your inquiry has been sent successfully.';
    } catch (Exception $e) {
        // Error response
        $response['success'] = false;
        $response['message'] = $e->getMessage();
    }

    // JSON response
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

// If accessed via non-POST method, show error
http_response_code(405); // Method Not Allowed
header('Content-Type: application/json');
echo json_encode([
    'success' => false,
    'message' => 'Invalid request method. Use POST to submit inquiries.',
]);
exit;
?>
```
