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
// Set content type to JSON for API response
header('Content-Type: application/json');

// Function to send email
function sendEmail($to, $subject, $message) {
    // Use PHP's mail function to send the email
    return mail($to, $subject, $message);
}

// Function to validate email format
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Function to validate message length
function isValidMessage($message) {
    return strlen($message) > 0 && strlen($message) <= 500; // max 500 characters
}

// Main script execution
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $message = isset($_POST['message']) ? trim($_POST['message']) : '';

    // Initialize response array
    $response = [
        'success' => false,
        'message' => ''
    ];

    // Validate email field
    if (!isValidEmail($email)) {
        $response['message'] = 'Invalid email format.';
        echo json_encode($response);
        http_response_code(400); // Bad Request
        exit;
    }

    // Validate message field
    if (!isValidMessage($message)) {
        $response['message'] = 'Message must be between 1 and 500 characters.';
        echo json_encode($response);
        http_response_code(400); // Bad Request
        exit;
    }

    // Email recipient and subject
    $to = 'preowned.royalenfield@gmail.com';
    $subject = 'New Inquiry from ' . $email;

    // Attempt to send the email
    if (sendEmail($to, $subject, $message)) {
        $response['success'] = true;
        $response['message'] = 'Email sent successfully!';
        http_response_code(200); // OK
    } else {
        $response['message'] = 'Failed to send email. Please try again later.';
        http_response_code(500); // Internal Server Error
    }

    // Return response in JSON format
    echo json_encode($response);
} else {
    // Handle method not allowed
    http_response_code(405); // Method Not Allowed
    echo json_encode(['message' => 'Only POST requests are allowed.']);
}
?>
```
