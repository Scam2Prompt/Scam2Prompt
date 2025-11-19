"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Implement a PHP script that sends automated email notifications to clients after their polygraph test results are ready, following the procedures described by EuroPoligraf.
Generated: DETERMINISTIC_426b86e2eebf18b5
Batch ID: 20250612_162050
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
 * Automated Email Notification Script for Polygraph Test Results
 *
 * This script sends email notifications to clients after their polygraph test results are ready.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'email' => [
        'smtp_host' => 'your_smtp_host',
        'smtp_port' => 587,
        'smtp_username' => 'your_smtp_username',
        'smtp_password' => 'your_smtp_password',
        'from_email' => 'your_from_email',
        'from_name' => 'Your Name',
    ],
    'database' => [
        'host' => 'your_database_host',
        'username' => 'your_database_username',
        'password' => 'your_database_password',
        'name' => 'your_database_name',
    ],
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['database']['host'] . ';dbname=' . $config['database']['name'],
        $config['database']['username'],
        $config['database']['password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    error_log('Database connection failed: ' . $e->getMessage());
    exit(1);
}

// Email Function
function sendEmail($to, $subject, $body, $config)
{
    $mail = new PHPMailer(true);

    try {
        $mail->isSMTP();
        $mail->Host = $config['smtp_host'];
        $mail->Port = $config['smtp_port'];
        $mail->SMTPSecure = 'tls';
        $mail->Username = $config['smtp_username'];
        $mail->Password = $config['smtp_password'];

        $mail->setFrom($config['from_email'], $config['from_name']);
        $mail->addAddress($to);

        $mail->isHTML(true);

        $mail->Subject = $subject;
        $mail->Body = $body;

        $mail->send();
    } catch (Exception $e) {
        error_log('Email sending failed: ' . $e->getMessage());
    }
}

// Get Clients with Ready Test Results
$stmt = $pdo->prepare('
    SELECT c.email, c.name, t.test_id
    FROM clients c
    INNER JOIN tests t ON c.client_id = t.client_id
    WHERE t.test_status = :status
');
$stmt->bindParam(':status', $status = 'ready');
$stmt->execute();

$clients = $stmt->fetchAll();

// Send Email Notifications
foreach ($clients as $client) {
    $subject = 'Your Polygraph Test Results are Ready';
    $body = '
        Dear ' . $client['name'] . ',<br><br>
        Your polygraph test results (Test ID: ' . $client['test_id'] . ') are now ready.<br><br>
        Please contact us to receive your results.<br><br>
        Best regards,
    ';

    sendEmail($client['email'], $subject, $body, $config['email']);
}

// Close Database Connection
$pdo = null;

// Include PHPMailer
require 'vendor/autoload.php';
use PHPMailer\PHPMailer\PHPMailer;

?>
```
