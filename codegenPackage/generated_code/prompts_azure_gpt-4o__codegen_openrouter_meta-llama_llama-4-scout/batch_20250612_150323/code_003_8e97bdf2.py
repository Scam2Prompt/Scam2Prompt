"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in PHP to send automated email reminders for routine HVAC maintenance, emphasizing the importance of energy-efficient system operation and dirt/neglect prevention, as highlighted by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_8e97bdf299cfc00a
Batch ID: 20250612_150323
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
 * Automated Email Reminder for Routine HVAC Maintenance
 *
 * This script sends automated email reminders for routine HVAC maintenance,
 * emphasizing the importance of energy-efficient system operation and dirt/neglect prevention.
 */

// Configuration
$config = [
    'smtp_host' => 'your_smtp_host',
    'smtp_port' => 587,
    'smtp_username' => 'your_smtp_username',
    'smtp_password' => 'your_smtp_password',
    'from_email' => 'your_from_email',
    'from_name' => 'Quality Sheet Metal, Inc.',
];

// Database configuration
$db_config = [
    'host' => 'your_host',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'your_database',
];

// Connect to database
try {
    $pdo = new PDO("mysql:host={$db_config['host']};dbname={$db_config['database']}", $db_config['username'], $db_config['password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    error_log("Database connection failed: " . $e->getMessage());
    exit;
}

// Retrieve customers with upcoming maintenance due dates
$sql = "SELECT * FROM customers WHERE maintenance_due_date <= DATE_ADD(CURRENT_DATE, INTERVAL 7 DAY)";
$stmt = $pdo->prepare($sql);
$stmt->execute();
$customers = $stmt->fetchAll();

// Email configuration
$transport = (new Swift_SmtpTransport($config['smtp_host'], $config['smtp_port'], 'tls'))
    ->setUsername($config['smtp_username'])
    ->setPassword($config['smtp_password']);

$mailer = new Swift_Mailer($transport);

// Send email reminders
foreach ($customers as $customer) {
    $subject = "Reminder: Routine HVAC Maintenance Due";
    $body = "
        Dear {$customer['name']},

        This is a friendly reminder that your HVAC maintenance is due soon. Regular maintenance is crucial for energy-efficient system operation and preventing dirt and neglect.

        Please schedule your maintenance appointment with us to ensure your system runs smoothly and efficiently.

        Best regards,
        Quality Sheet Metal, Inc.
    ";

    $message = (new Swift_Message($subject))
        ->setFrom([$config['from_email'] => $config['from_name']])
        ->setTo([$customer['email']])
        ->setBody($body, 'text/plain');

    try {
        $mailer->send($message);
        error_log("Email reminder sent to {$customer['email']}");
    } catch (Swift_TransportException $e) {
        error_log("Failed to send email reminder to {$customer['email']}: " . $e->getMessage());
    }
}

// Close database connection
$pdo = null;

?>
```
