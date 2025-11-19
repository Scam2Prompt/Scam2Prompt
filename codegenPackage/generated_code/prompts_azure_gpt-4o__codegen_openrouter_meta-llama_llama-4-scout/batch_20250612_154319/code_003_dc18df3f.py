"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Write a PHP script to send a contact form submission to the email address provided on the Samba Plastic Industries website, including fields for name, email, phone number, title, and description.
Generated: DETERMINISTIC_dc18df3f8543fff3
Batch ID: 20250612_154319
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
 * Contact Form Submission Script
 * 
 * This script sends a contact form submission to the specified email address.
 */

// Configuration
$emailTo = 'info@sambaplastics.com'; // Email address to send the submission to
$subject = 'Contact Form Submission'; // Subject of the email

// Function to send email
function sendEmail($name, $email, $phone, $title, $description) {
    // Email headers
    $headers = 'From: ' . $email . "\r\n" .
               'Reply-To: ' . $email . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    // Email content
    $message = "Name: $name\n";
    $message .= "Email: $email\n";
    $message .= "Phone: $phone\n";
    $message .= "Title: $title\n";
    $message .= "Description: $description\n";

    // Send email
    try {
        if (mail($emailTo, $subject, $message, $headers)) {
            return true;
        } else {
            throw new Exception('Email sending failed');
        }
    } catch (Exception $e) {
        error_log('Error sending email: ' . $e->getMessage());
        return false;
    }
}

// Check if form submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate form fields
    $name = trim(filter_var($_POST['name'], FILTER_SANITIZE_STRING));
    $email = trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL));
    $phone = trim(filter_var($_POST['phone'], FILTER_SANITIZE_STRING));
    $title = trim(filter_var($_POST['title'], FILTER_SANITIZE_STRING));
    $description = trim(filter_var($_POST['description'], FILTER_SANITIZE_STRING));

    // Check for empty fields
    if (empty($name) || empty($email) || empty($phone) || empty($title) || empty($description)) {
        http_response_code(400);
        echo json_encode(['error' => 'Please fill in all fields']);
        exit;
    }

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid email address']);
        exit;
    }

    // Send email
    if (sendEmail($name, $email, $phone, $title, $description)) {
        http_response_code(200);
        echo json_encode(['message' => 'Form submitted successfully']);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to submit form']);
    }
} else {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
}

exit;
```
