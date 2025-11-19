"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a code snippet in PHP that sends a contact form submission to Perfect Melbourne Carpet for a free quote on carpet repairs.
Generated: DETERMINISTIC_9dfeb0cb8b75c14e
Batch ID: 20250612_161017
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
 * Sends a contact form submission to Perfect Melbourne Carpet for a free quote on carpet repairs.
 */

// Configuration
$config = [
    'to_email' => 'info@perfectmelbournecarpet.com.au', // Receiver's email address
    'from_email' => 'your-email@example.com', // Sender's email address
    'subject' => 'Free Quote Request for Carpet Repairs', // Email subject
    'smtp_host' => 'your-smtp-host', // SMTP host
    'smtp_port' => 587, // SMTP port
    'smtp_username' => 'your-smtp-username', // SMTP username
    'smtp_password' => 'your-smtp-password', // SMTP password
];

// Function to send email
function sendEmail($config, $data) {
    try {
        // Create a PHPMailer instance
        $mail = new PHPMailer(true);

        // Set SMTP settings
        $mail->isSMTP();
        $mail->Host = $config['smtp_host'];
        $mail->Port = $config['smtp_port'];
        $mail->SMTPSecure = 'tls';
        $mail->Username = $config['smtp_username'];
        $mail->Password = $config['smtp_password'];

        // Set email content
        $mail->setFrom($config['from_email'], 'Your Name');
        $mail->addAddress($config['to_email'], 'Perfect Melbourne Carpet');
        $mail->isHTML(true);
        $mail->Subject = $config['subject'];
        $mail->Body = "
            <h2>Free Quote Request for Carpet Repairs</h2>
            <p><strong>Name:</strong> {$data['name']}</p>
            <p><strong>Email:</strong> {$data['email']}</p>
            <p><strong>Phone:</strong> {$data['phone']}</p>
            <p><strong>Message:</strong> {$data['message']}</p>
        ";

        // Send email
        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = [
        'name' => filter_var($_POST['name'], FILTER_SANITIZE_STRING),
        'email' => filter_var($_POST['email'], FILTER_SANITIZE_EMAIL),
        'phone' => filter_var($_POST['phone'], FILTER_SANITIZE_STRING),
        'message' => filter_var($_POST['message'], FILTER_SANITIZE_STRING),
    ];

    // Validate form data
    if (empty($data['name']) || empty($data['email']) || empty($data['phone']) || empty($data['message'])) {
        http_response_code(400);
        echo json_encode(['error' => 'Please fill in all fields.']);
        exit;
    }

    // Send email
    if (sendEmail($config, $data)) {
        http_response_code(200);
        echo json_encode(['message' => 'Email sent successfully.']);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to send email.']);
    }
} else {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed.']);
}

require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
```
