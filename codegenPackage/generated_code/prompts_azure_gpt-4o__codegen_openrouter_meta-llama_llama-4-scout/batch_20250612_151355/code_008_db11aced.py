"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Create a PHP script to handle form submissions for a contact page, including validation for email and phone number fields, inspired by Ayoft's contact form.
Generated: DETERMINISTIC_db11acedf241671c
Batch ID: 20250612_151355
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
 * Contact Form Handler
 *
 * Handles form submissions for a contact page, including validation for email and phone number fields.
 */

// Configuration
$config = [
    'admin_email' => 'your-admin-email@example.com',
    'subject' => 'New Contact Form Submission',
    'success_message' => 'Your message has been sent successfully.',
    'error_message' => 'There was an error sending your message.',
];

// Function to validate email
function validateEmail($email)
{
    $pattern = '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/';
    if (preg_match($pattern, $email)) {
        return true;
    }
    return false;
}

// Function to validate phone number
function validatePhoneNumber($phoneNumber)
{
    $pattern = '/^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/';
    if (preg_match($pattern, $phoneNumber)) {
        return true;
    }
    return false;
}

// Check if form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Get form data
        $name = trim(filter_var($_POST['name'], FILTER_SANITIZE_STRING));
        $email = trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL));
        $phoneNumber = trim(filter_var($_POST['phone_number'], FILTER_SANITIZE_STRING));
        $message = trim(filter_var($_POST['message'], FILTER_SANITIZE_STRING));

        // Validate form data
        $errors = [];
        if (empty($name)) {
            $errors[] = 'Name is required.';
        }
        if (empty($email) || !validateEmail($email)) {
            $errors[] = 'Invalid email address.';
        }
        if (empty($phoneNumber) || !validatePhoneNumber($phoneNumber)) {
            $errors[] = 'Invalid phone number.';
        }
        if (empty($message)) {
            $errors[] = 'Message is required.';
        }

        // Send email if no errors
        if (empty($errors)) {
            $headers = [
                'From' => $email,
                'Reply-To' => $email,
            ];
            $body = "Name: $name\nEmail: $email\nPhone Number: $phoneNumber\nMessage: $message";

            if (mail($config['admin_email'], $config['subject'], $body, $headers)) {
                $response = ['success' => true, 'message' => $config['success_message']];
            } else {
                throw new Exception('Failed to send email.');
            }
        } else {
            $response = ['success' => false, 'errors' => $errors];
        }
    } catch (Exception $e) {
        $response = ['success' => false, 'message' => $config['error_message']];
    }

    // Output JSON response
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

?>
```
