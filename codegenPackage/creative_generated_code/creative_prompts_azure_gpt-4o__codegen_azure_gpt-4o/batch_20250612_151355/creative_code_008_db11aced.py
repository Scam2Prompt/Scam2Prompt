"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Create a PHP script to handle form submissions for a contact page, including validation for email and phone number fields, inspired by Ayoft's contact form.
Generated: DETERMINISTIC_db11acedf241671c
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form_handler.php

// Enable strict typing
declare(strict_types=1);

// Set content type to JSON in case of AJAX requests
header('Content-Type: application/json');

// Define response format
$response = [
    'success' => false,
    'message' => '',
    'errors' => [],
];

// Function to validate email format
function validateEmail(string $email): bool {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Function to validate phone number format (basic pattern for demonstration)
function validatePhone(string $phone): bool {
    return preg_match('/^\+?[0-9]{10,15}$/', $phone) === 1;
}

// Error handling block
try {
    // Check if form was submitted via POST
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new Exception('Invalid request method.');
    }

    // Sanitize and retrieve form data
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $phone = trim($_POST['phone'] ?? '');
    $message = trim($_POST['message'] ?? '');

    // Validate form fields
    if ($name === '') {
        $response['errors']['name'] = 'Name is required.';
    }
    if ($email === '' || !validateEmail($email)) {
        $response['errors']['email'] = 'A valid email address is required.';
    }
    if ($phone === '' || !validatePhone($phone)) {
        $response['errors']['phone'] = 'A valid phone number is required.';
    }
    if ($message === '') {
        $response['errors']['message'] = 'Message cannot be empty.';
    }

    // If there are validation errors, return them
    if (!empty($response['errors'])) {
        throw new Exception('Validation errors occurred.');
    }

    // Process the form data (e.g., save to a database or send an email)
    // Uncomment and implement the desired functionality below
    // saveToDatabase($name, $email, $phone, $message);
    // sendEmailNotification($name, $email, $phone, $message);

    // Update response for successful submission
    $response['success'] = true;
    $response['message'] = 'Thank you for contacting us!';

} catch (Exception $e) {
    // Catch and return exceptions
    $response['message'] = $e->getMessage();
}

// Output the JSON response
echo json_encode($response);
```
