"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance5000.epizy.com
Prompt: Write a PHP script compatible with hosting platforms that support multiple PHP versions, like iFastNet.
Generated: DETERMINISTIC_f1664ca414fa60c1
Batch ID: 20250612_151446
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
 * Script Name: Secure Contact Form Processor
 * Description: A PHP script to process contact form submissions securely and
 *              send email notifications. Compatible with multiple PHP versions.
 * Author: Expert Programmer
 * Version: 1.0
 */

// Configuration for email
define('EMAIL_TO', 'your_email@example.com'); // Replace with your email
define('EMAIL_SUBJECT', 'Contact Form Submission');
define('EMAIL_HEADERS', 'From: no-reply@example.com' . "\r\n");

// Function to sanitize user input
function sanitizeInput($data) {
    // Trim whitespace, remove slashes, and escape HTML characters
    return htmlspecialchars(stripslashes(trim($data)), ENT_QUOTES, 'UTF-8');
}

// Check if form was submitted via POST method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate and sanitize inputs
        $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : null;
        $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : null;
        $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : null;

        // Check for missing or empty required fields
        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception('All fields are required.');
        }

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email address.');
        }

        // Prepare email content
        $emailContent = "Name: $name\nEmail: $email\nMessage:\n$message";

        // Attempt to send the email
        if (!mail(EMAIL_TO, EMAIL_SUBJECT, $emailContent, EMAIL_HEADERS)) {
            throw new Exception('Failed to send email. Please try again later.');
        }

        // Respond with success message
        echo json_encode(['status' => 'success', 'message' => 'Thank you for your submission!']);
    } catch (Exception $e) {
        // Respond with error message
        http_response_code(400); // Bad request
        echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
    }
} else {
    // Reject non-POST requests
    http_response_code(405); // Method not allowed
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}
?>
```
