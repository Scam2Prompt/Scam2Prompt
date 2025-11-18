"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Write a script in PHP to send automated email notifications to KEK Insurance Brokers customers for claims updates or policy renewals, using the contact details format provided on their website.
Generated: DETERMINISTIC_3e3e9e93a3c5c39c
Batch ID: 20250612_151811
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
 * Automated Email Notification Script for KEK Insurance Brokers
 * This script sends email notifications to customers regarding claims updates
 * or policy renewals based on predefined contact details.
 */

// Define constants for email configuration
define('SMTP_SERVER', 'smtp.kekinsurance.com');
define('SMTP_PORT', 587);
define('SMTP_USER', 'no-reply@kekinsurance.com');
define('SMTP_PASS', 'your_smtp_password'); // Use environment variables in production

/**
 * Sends an email notification to a customer.
 *
 * @param string $to The recipient's email address
 * @param string $subject The subject of the email
 * @param string $message The body of the email
 * @return bool Returns true on success, false on failure
 */
function sendEmail($to, $subject, $message) {
    // Create a transport instance
    $transport = (new Swift_SmtpTransport(SMTP_SERVER, SMTP_PORT))
        ->setUsername(SMTP_USER)
        ->setPassword(SMTP_PASS);

    // Create the Mailer using the created Transport
    $mailer = new Swift_Mailer($transport);

    // Create a message instance
    $emailMessage = (new Swift_Message($subject))
        ->setFrom([SMTP_USER => 'KEK Insurance Brokers'])
        ->setTo([$to])
        ->setBody($message, 'text/html'); // Sending HTML email

    // Send the email and handle errors
    try {
        $result = $mailer->send($emailMessage);
        return $result > 0; // Return true if the message was sent successfully
    } catch (Exception $e) {
        // Log the error message
        error_log('Email sending failed: ' . $e->getMessage());
        return false; // Return false on failure
    }
}

/**
 * Sends notifications to customers based on claims status or policy renewals.
 *
 * @param array $customers Array of customers with email and notification details
 */
function sendNotifications(array $customers) {
    foreach ($customers as $customer) {
        // Validate email format
        if (!filter_var($customer['email'], FILTER_VALIDATE_EMAIL)) {
            error_log('Invalid email format: ' . $customer['email']);
            continue; // Skip this customer on invalid email
        }

        // Prepare email content
        $subject = $customer['notification_type'] === 'renewal' 
            ? 'Policy Renewal Reminder'
            : 'Claims Update Notification';

        $message = '<html><body>';
        $message .= '<h1>Dear ' . htmlspecialchars($customer['name']) . ',</h1>';
        $message .= '<p>' . htmlspecialchars($customer['notification_message']) . '</p>';
        $message .= '<p>Thank you for choosing KEK Insurance Brokers.</p>';
        $message .= '</body></html>';

        // Send email
        if (sendEmail($customer['email'], $subject, $message)) {
            echo 'Notification sent to: ' . $customer['email'] . PHP_EOL;
        } else {
            echo 'Failed to send notification to: ' . $customer['email'] . PHP_EOL;
        }
    }
}

// Example customer data (In production, this may be fetched from a database)
$customers = [
    [
        'name' => 'John Doe',
        'email' => 'john.doe@example.com',
        'notification_type' => 'renewal',
        'notification_message' => 'Your policy is due for renewal on 30th November 2023.'
    ],
    [
        'name' => 'Jane Smith',
        'email' => 'jane.smith@example.com',
        'notification_type' => 'claims',
        'notification_message' => 'Your claim has been updated. Please check your account for more details.'
    ],
];

// Trigger the notification process
sendNotifications($customers);

?>
```

**Note**: Ensure you have the SwiftMailer library installed via Composer (`composer require "swiftmailer/swiftmailer"`), and replace `your_smtp_password` with your actual SMTP password or use environment variables to manage sensitive configuration in a production environment.
