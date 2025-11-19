"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Create a PHP code snippet to send an email notification to parents about upcoming events at Основна школа "Мокро", including details from the "Родитељи" section.
Generated: DETERMINISTIC_f60be9b1465e3b8d
Batch ID: 20250612_135754
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
 * Email Notification Sender for Основна школа "Мокро"
 *
 * This script sends an email notification to parents about upcoming events
 * at Основна школа "Мокро", including details from the "Родитељи" section.
 */

// Configuration
$config = [
    'schoolName' => 'Основна школа "Мокро"',
    'emailFrom' => 'your-email@example.com',
    'emailSubject' => 'Upcoming Events at ' . $config['schoolName'],
    'smtpHost' => 'your-smtp-host',
    'smtpPort' => 587,
    'smtpUsername' => 'your-smtp-username',
    'smtpPassword' => 'your-smtp-password',
];

// Parent data (simulate database or storage)
$parents = [
    [
        'name' => 'John Doe',
        'email' => 'john.doe@example.com',
    ],
    [
        'name' => 'Jane Doe',
        'email' => 'jane.doe@example.com',
    ],
];

// Upcoming events data (simulate database or storage)
$events = [
    [
        'title' => 'Parent-Teacher Meeting',
        'date' => '2024-09-20',
        'time' => '15:00',
        'description' => 'A meeting between parents and teachers to discuss student progress.',
    ],
    [
        'title' => 'School Holiday',
        'date' => '2024-09-25',
        'time' => '',
        'description' => 'A school holiday for students.',
    ],
];

// Function to send email
function sendEmail($to, $subject, $body, $config) {
    $mail = new PHPMailer(true);
    try {
        // SMTP settings
        $mail->isSMTP();
        $mail->Host = $config['smtpHost'];
        $mail->Port = $config['smtpPort'];
        $mail->SMTPSecure = 'tls';
        $mail->Username = $config['smtpUsername'];
        $mail->Password = $config['smtpPassword'];

        // Email settings
        $mail->setFrom($config['emailFrom'], $config['schoolName']);
        $mail->addAddress($to);
        $mail->isHTML(true);

        // Email content
        $mail->Subject = $subject;
        $mail->Body = $body;

        $mail->send();
        echo "Email sent to $to successfully.\n";
    } catch (Exception $e) {
        echo "Email sending failed: " . $mail->ErrorInfo . "\n";
    }
}

// Generate email body
function generateEmailBody($events) {
    $body = '<h2>Upcoming Events</h2>';
    $body .= '<ul>';
    foreach ($events as $event) {
        $body .= '<li>';
        $body .= '<strong>' . $event['title'] . '</strong> on ' . $event['date'];
        if (!empty($event['time'])) {
            $body .= ' at ' . $event['time'];
        }
        $body .= '<br>' . $event['description'] . '</li>';
    }
    $body .= '</ul>';
    return $body;
}

// Send email notifications
foreach ($parents as $parent) {
    $emailBody = generateEmailBody($events);
    sendEmail($parent['email'], $config['emailSubject'], $emailBody, $config);
}

```

You will also need the PHPMailer library. If not already installed, you can do so via Composer:

```bash
composer require phpmailer/phpmailer
```
