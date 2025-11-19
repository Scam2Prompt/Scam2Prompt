"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Create a PHP script to send automated email confirmations to customers after they book plumbing services with Certified Plumbers Graham, TX, including details of the service and appointment time.
Generated: DETERMINISTIC_ed202018df628727
Batch ID: 20250612_154432
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
 * Automated Email Confirmation Script for Certified Plumbers Graham, TX
 */

// Configuration
$config = [
    'smtp_host' => 'your_smtp_host',
    'smtp_port' => 587,
    'smtp_username' => 'your_smtp_username',
    'smtp_password' => 'your_smtp_password',
    'from_email' => 'your_from_email',
    'from_name' => 'Certified Plumbers Graham, TX',
];

// Email Template
$email_template = [
    'subject' => 'Appointment Confirmation: Plumbing Service',
    'body' => file_get_contents('email_template.html'),
];

// Function to send email
function send_email($to_email, $to_name, $service_details, $appointment_time) {
    global $config, $email_template;

    // Load email template
    $email_body = $email_template['body'];
    $email_body = str_replace('{{SERVICE_DETAILS}}', $service_details, $email_body);
    $email_body = str_replace('{{APPOINTMENT_TIME}}', $appointment_time, $email_body);

    // Create PHPMailer instance
    $mail = new PHPMailer(true);
    try {
        // SMTP settings
        $mail->isSMTP();
        $mail->Host = $GLOBALS['config']['smtp_host'];
        $mail->Port = $GLOBALS['config']['smtp_port'];
        $mail->SMTPSecure = 'tls';
        $mail->Username = $GLOBALS['config']['smtp_username'];
        $mail->Password = $GLOBALS['config']['smtp_password'];

        // Set email headers
        $mail->setFrom($GLOBALS['config']['from_email'], $GLOBALS['config']['from_name']);
        $mail->addAddress($to_email, $to_name);
        $mail->isHTML(true);

        // Set email content
        $mail->Subject = $email_template['subject'];
        $mail->Body = $email_body;

        // Send email
        if (!$mail->send()) {
            throw new Exception($mail->ErrorInfo);
        }
        return true;
    } catch (Exception $e) {
        error_log('Email sending failed: ' . $e->getMessage());
        return false;
    }
}

// Example usage
$service_details = 'Drain Cleaning';
$appointment_time = '2024-09-17 10:00 AM';
$to_email = 'customer@example.com';
$to_name = 'John Doe';

if (send_email($to_email, $to_name, $service_details, $appointment_time)) {
    echo "Email sent successfully!\n";
} else {
    echo "Email sending failed.\n";
}

require 'vendor/autoload.php';
use PHPMailer\PHPMailer\PHPMailer;

?>
```
