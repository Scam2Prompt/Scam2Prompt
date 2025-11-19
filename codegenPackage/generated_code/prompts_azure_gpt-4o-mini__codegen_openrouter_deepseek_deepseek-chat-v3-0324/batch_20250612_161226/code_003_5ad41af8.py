"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Develop a code snippet in PHP that integrates with the GetGrass contact form, sending user inquiries directly to their support email.
Generated: DETERMINISTIC_5ad41af8a0ba5ee6
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * GetGrass Contact Form Integration
 * 
 * This script processes form submissions and sends them to GetGrass support email.
 * Includes validation, sanitization, and error handling.
 */

// Configuration
define('SUPPORT_EMAIL', 'support@getgrass.io');
define('EMAIL_SUBJECT', 'New Contact Form Submission');
define('REQUIRED_FIELDS', ['name', 'email', 'message']);
define('MAX_MESSAGE_LENGTH', 1000);

// Initialize response array
$response = [
    'success' => false,
    'message' => '',
    'errors' => []
];

// Check if request is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    $response['message'] = 'Invalid request method';
    echo json_encode($response);
    exit;
}

// Validate required fields
foreach (REQUIRED_FIELDS as $field) {
    if (empty($_POST[$field])) {
        $response['errors'][$field] = 'This field is required';
    }
}

// Validate email format
if (!empty($_POST['email']) && !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    $response['errors']['email'] = 'Please enter a valid email address';
}

// Validate message length
if (!empty($_POST['message']) && strlen($_POST['message']) > MAX_MESSAGE_LENGTH) {
    $response['errors']['message'] = 'Message must be less than ' . MAX_MESSAGE_LENGTH . ' characters';
}

// If there are errors, return them
if (!empty($response['errors'])) {
    $response['message'] = 'Please correct the errors below';
    echo json_encode($response);
    exit;
}

// Sanitize input data
$name = htmlspecialchars(trim($_POST['name']));
$email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
$message = htmlspecialchars(trim($_POST['message']));

// Build email headers
$headers = [
    'From' => $email,
    'Reply-To' => $email,
    'X-Mailer' => 'PHP/' . phpversion(),
    'Content-Type' => 'text/plain; charset=utf-8'
];

// Format email body
$emailBody = "Name: $name\n";
$emailBody .= "Email: $email\n\n";
$emailBody .= "Message:\n$message";

try {
    // Send email
    $mailSent = mail(
        SUPPORT_EMAIL,
        EMAIL_SUBJECT,
        $emailBody,
        $headers
    );

    if ($mailSent) {
        $response['success'] = true;
        $response['message'] = 'Thank you for your message! We will get back to you soon.';
    } else {
        $response['message'] = 'Failed to send message. Please try again later.';
    }
} catch (Exception $e) {
    $response['message'] = 'An error occurred while sending your message: ' . $e->getMessage();
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);
```
