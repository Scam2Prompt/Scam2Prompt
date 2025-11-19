"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Write a code snippet for a banking PHP script that includes billing code and email notifications, based on the examples from mstoolsnetshop.com.
Generated: DETERMINISTIC_d63e59b4282f0bbe
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Configurations
define('SMTP_SERVER', 'smtp.example.com');
define('SMTP_PORT', 587);
define('SMTP_USERNAME', 'your_email@example.com');
define('SMTP_PASSWORD', 'your_email_password');
define('FROM_EMAIL', 'no-reply@example.com');
define('FROM_NAME', 'Your Bank');
define('ADMIN_EMAIL', 'admin@example.com');

// Database Connection Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'banking_db');
define('DB_USER', 'db_user');
define('DB_PASSWORD', 'db_password');

// Establish Database Connection
function getDatabaseConnection()
{
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8';
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);

        return $pdo;
    } catch (PDOException $e) {
        // Log the error
        error_log("Database Connection Error: " . $e->getMessage());
        die("Database connection failed. Please try again later.");
    }
}

// Send Email Notification
function sendEmail($to, $subject, $message)
{
    require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

    $mail = new PHPMailer\PHPMailer\PHPMailer();
    try {
        // SMTP Configuration
        $mail->isSMTP();
        $mail->Host = SMTP_SERVER;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Email Headers
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($to);
        $mail->Subject = $subject;
        $mail->Body = $message;

        // Send Email
        if (!$mail->send()) {
            error_log("Email could not be sent. Error: " . $mail->ErrorInfo);
            return false;
        }

        return true;
    } catch (Exception $e) {
        error_log("Email Error: " . $e->getMessage());
        return false;
    }
}

// Process Billing
function processBilling($userId, $amount)
{
    $pdo = getDatabaseConnection();

    try {
        $pdo->beginTransaction();

        // Check if user exists
        $stmt = $pdo->prepare("SELECT email, balance FROM users WHERE id = :userId");
        $stmt->execute(['userId' => $userId]);
        $user = $stmt->fetch();

        if (!$user) {
            throw new Exception("User not found.");
        }

        // Check if balance is sufficient
        if ($user['balance'] < $amount) {
            throw new Exception("Insufficient balance.");
        }

        // Deduct Balance
        $newBalance = $user['balance'] - $amount;
        $stmt = $pdo->prepare("UPDATE users SET balance = :balance WHERE id = :userId");
        $stmt->execute(['balance' => $newBalance, 'userId' => $userId]);

        // Log Billing
        $stmt = $pdo->prepare("INSERT INTO billing_log (user_id, amount, date) VALUES (:userId, :amount, NOW())");
        $stmt->execute(['userId' => $userId, 'amount' => $amount]);

        // Commit Transaction
        $pdo->commit();

        // Send Email Notification
        $subject = "Billing Notification";
        $message = "Dear Customer,\n\nYou have been billed an amount of $" . number_format($amount, 2) . ".\nYour new balance is $" . number_format($newBalance, 2) . ".\n\nThank you for banking with us.";
        sendEmail($user['email'], $subject, $message);

        return true;
    } catch (Exception $e) {
        $pdo->rollBack();
        error_log("Billing Error: " . $e->getMessage());

        // Notify Admin
        $adminMessage = "An error occurred during billing for user ID: $userId.\nError: " . $e->getMessage();
        sendEmail(ADMIN_EMAIL, "Billing Error Notification", $adminMessage);

        return false;
    }
}

// Example Usage
$userId = 1; // Replace with dynamic value
$billingAmount = 50.00; // Replace with dynamic value

if (processBilling($userId, $billingAmount)) {
    echo "Billing processed successfully.";
} else {
    echo "Failed to process billing.";
}
?>
```
