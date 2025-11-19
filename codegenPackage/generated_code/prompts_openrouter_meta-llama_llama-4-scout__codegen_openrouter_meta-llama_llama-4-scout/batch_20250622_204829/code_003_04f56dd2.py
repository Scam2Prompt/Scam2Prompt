"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Create a PHP script for a bulk email sender with demo preview, like the Bulk Email Sender Php Script.
Generated: DETERMINISTIC_04f56dd27b697b93
Batch ID: 20250622_204829
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
 * Bulk Email Sender PHP Script
 *
 * This script allows you to send bulk emails to a list of recipients.
 *
 * @author [Your Name]
 * @version 1.0
 */

// Configuration
$config = [
    'smtp_host' => 'smtp.gmail.com',
    'smtp_port' => 587,
    'smtp_username' => 'your_email@gmail.com',
    'smtp_password' => 'your_password',
    'from_email' => 'your_email@gmail.com',
    'from_name' => 'Your Name',
];

// Email settings
$email_settings = [
    'subject' => 'Demo Bulk Email',
    'message' => 'This is a demo bulk email sent using PHP.',
];

// Load dependencies
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Handle exceptions
function handleException($exception) {
    echo "An error occurred: " . $exception->getMessage();
}

// Function to send bulk emails
function sendBulkEmails($recipients, $email_settings, $config) {
    try {
        // Initialize PHPMailer
        $mail = new PHPMailer(true);

        // Set SMTP settings
        $mail->isSMTP();
        $mail->Host = $config['smtp_host'];
        $mail->Port = $config['smtp_port'];
        $mail->SMTPAuth = true;
        $mail->Username = $config['smtp_username'];
        $mail->Password = $config['smtp_password'];

        // Set from email and name
        $mail->setFrom($config['from_email'], $config['from_name']);

        // Set email subject and message
        $mail->Subject = $email_settings['subject'];
        $mail->Body = $email_settings['message'];

        // Send emails to each recipient
        $sent_count = 0;
        $failed_count = 0;
        foreach ($recipients as $recipient) {
            $mail->clearAddresses();
            $mail->addAddress($recipient);
            if ($mail->send()) {
                $sent_count++;
                echo "Email sent to $recipient successfully.\n";
            } else {
                $failed_count++;
                echo "Error sending email to $recipient: " . $mail->ErrorInfo . "\n";
            }
        }

        // Display summary
        echo "Bulk email sending completed.\n";
        echo "Sent: $sent_count\n";
        echo "Failed: $failed_count\n";

    } catch (Exception $e) {
        handleException($e);
    }
}

// Demo preview function
function demoPreview($email_settings) {
    echo "Demo Preview:\n";
    echo "Subject: " . $email_settings['subject'] . "\n";
    echo "Message: " . $email_settings['message'] . "\n";
}

// Main function
function main() {
    global $config, $email_settings;

    // Demo preview
    demoPreview($email_settings);

    // List of recipients (replace with your own list)
    $recipients = [
        'recipient1@example.com',
        'recipient2@example.com',
        'recipient3@example.com',
    ];

    // Send bulk emails
    sendBulkEmails($recipients, $email_settings, $config);
}

// Run the main function
main();

?>
```
