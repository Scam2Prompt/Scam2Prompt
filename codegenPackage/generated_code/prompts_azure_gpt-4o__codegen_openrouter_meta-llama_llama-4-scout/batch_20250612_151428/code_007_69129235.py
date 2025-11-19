"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate code in PHP to send automated email notifications to NSW Police about film shoots involving hired police uniforms, ensuring compliance with the recommendations on Powered Production Film Services.
Generated: DETERMINISTIC_6912923569486ebd
Batch ID: 20250612_151428
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
 * Send automated email notifications to NSW Police about film shoots involving hired police uniforms.
 *
 * This script ensures compliance with the recommendations on Powered Production Film Services.
 */

// Configuration
$config = [
    'nswPoliceEmail' => 'nsw.police@police.nsw.gov.au', // NSW Police email address
    'filmCommissionEmail' => 'film.commission@film.nsw.gov.au', // Film Commission email address
    'senderEmail' => 'your.sender@email.com', // Your email address
    'senderName' => 'Your Name', // Your name
    'emailSubject' => 'Film Shoot Notification: Hired Police Uniforms', // Email subject
];

// Email notification details
$emailNotification = [
    'shootDate' => '', // Date of the film shoot
    'shootLocation' => '', // Location of the film shoot
    'productionCompany' => '', // Production company name
    'uniformQuantity' => 0, // Number of police uniforms hired
];

// Function to send email notification
function sendEmailNotification($config, $emailNotification) {
    try {
        // Create a PHPMailer instance
        $mailer = new PHPMailer\PHPMailer\PHPMailer(true);

        // Set email configuration
        $mailer->isSMTP();
        $mailer->Host = 'your.smtp.host'; // SMTP host
        $mailer->SMTPAuth = true;
        $mailer->Username = $config['senderEmail']; // SMTP username
        $mailer->Password = 'your.smtp.password'; // SMTP password
        $mailer->SMTPSecure = 'tls'; // SMTP security
        $mailer->Port = 587; // SMTP port

        // Set email content
        $mailer->setFrom($config['senderEmail'], $config['senderName']);
        $mailer->addAddress($config['nswPoliceEmail']);
        $mailer->addAddress($config['filmCommissionEmail']);
        $mailer->isHTML(true);
        $mailer->Subject = $config['emailSubject'];

        // Email template
        $emailBody = "
            <h2>Film Shoot Notification: Hired Police Uniforms</h2>
            <p><strong>Shoot Date:</strong> {$emailNotification['shootDate']}</p>
            <p><strong>Shoot Location:</strong> {$emailNotification['shootLocation']}</p>
            <p><strong>Production Company:</strong> {$emailNotification['productionCompany']}</p>
            <p><strong>Uniform Quantity:</strong> {$emailNotification['uniformQuantity']}</p>
        ";

        $mailer->Body = $emailBody;

        // Send email
        if (!$mailer->send()) {
            throw new Exception("Email sending failed: " . $mailer->ErrorInfo);
        }

        echo "Email notification sent successfully.\n";

    } catch (Exception $e) {
        echo "Error sending email notification: " . $e->getMessage() . "\n";
    }
}

// Example usage
$emailNotification['shootDate'] = '2024-09-16';
$emailNotification['shootLocation'] = 'Sydney, NSW';
$emailNotification['productionCompany'] = 'ABC Productions';
$emailNotification['uniformQuantity'] = 5;

sendEmailNotification($config, $emailNotification);

```

Make sure to install PHPMailer library via Composer:

```bash
composer require phpmailer/phpmailer
```

Replace placeholder values (e.g., `your.sender@email.com`, `your.smtp.host`, `your.smtp.password`) with actual values.
