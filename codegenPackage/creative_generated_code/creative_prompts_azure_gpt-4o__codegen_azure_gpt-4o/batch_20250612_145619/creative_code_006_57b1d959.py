"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Create a PHP script for a logistics and courier system with email notifications, referencing the "Helologistics Logistic PHP Script" from mstoolsnetshop.com.
Generated: DETERMINISTIC_57b1d9591ece0b7d
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// logistics_courier_system.php

// Enable error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Use Composer's autoloader (ensure Composer is installed and properly set up)
require __DIR__ . '/vendor/autoload.php';

// Use PHPMailer for email notifications
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Database configuration (Replace placeholders with actual credentials)
define('DB_HOST', 'localhost');
define('DB_NAME', 'logistics_db');
define('DB_USER', 'username');
define('DB_PASS', 'password');

try {
    // Establish a database connection using PDO
    $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    // Terminate script if database connection fails
    die("Database connection failed: " . $e->getMessage());
}

// Helper function to send email notifications
function sendEmailNotification($recipientEmail, $subject, $body)
{
    $mail = new PHPMailer(true);

    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = 'smtp.example.com'; // Replace with your SMTP host
        $mail->SMTPAuth = true;
        $mail->Username = 'youremail@example.com'; // SMTP username
        $mail->Password = 'yourpassword'; // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Recipients
        $mail->setFrom('youremail@example.com', 'Logistics System');
        $mail->addAddress($recipientEmail);

        // Content
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $body;

        $mail->send();
    } catch (Exception $e) {
        // Log email error for debugging (do not expose sensitive info in production)
        error_log("Email could not be sent. Error: {$mail->ErrorInfo}");
    }
}

// Example: Register a new package and notify the recipient
function registerPackage($pdo, $packageDetails)
{
    try {
        // Insert package details into the database
        $stmt = $pdo->prepare('INSERT INTO packages (tracking_number, sender_name, recipient_name, recipient_email, status, created_at) VALUES (?, ?, ?, ?, ?, NOW())');
        $stmt->execute([
            $packageDetails['tracking_number'],
            $packageDetails['sender_name'],
            $packageDetails['recipient_name'],
            $packageDetails['recipient_email'],
            'Pending',
        ]);

        // Notify the recipient via email
        $subject = "Your Package Has Been Registered";
        $body = "Dear {$packageDetails['recipient_name']},<br><br>Your package with tracking number <strong>{$packageDetails['tracking_number']}</strong> has been registered in our system. You will be notified about updates.<br><br>Thank you.";
        sendEmailNotification($packageDetails['recipient_email'], $subject, $body);

        return "Package successfully registered and email notification sent.";
    } catch (Exception $e) {
        // Log database error for debugging
        error_log("Package registration failed: " . $e->getMessage());
        return "An error occurred while registering the package.";
    }
}

// Example usage
$packageDetails = [
    'tracking_number' => 'LN123456789US',
    'sender_name' => 'John Doe',
    'recipient_name' => 'Jane Smith',
    'recipient_email' => 'jane.smith@example.com',
];

// Output the result of the package registration process
echo registerPackage($pdo, $packageDetails);
?>
```
