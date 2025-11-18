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
// Helologistics Logistic PHP Script
// This script handles logistics operations and email notifications for courier management.

// Include necessary libraries
require 'vendor/autoload.php'; // Composer autoload for external libraries

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Configuration settings
define('EMAIL_HOST', 'smtp.example.com');
define('EMAIL_USERNAME', 'your-email@example.com');
define('EMAIL_PASSWORD', 'your-email-password');
define('EMAIL_PORT', 587);
define('EMAIL_FROM', 'no-reply@example.com');
define('EMAIL_FROM_NAME', 'Helologistics');

// Function to send email notifications
function sendEmailNotification($to, $subject, $body) {
    $mail = new PHPMailer(true);
    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = EMAIL_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = EMAIL_USERNAME;
        $mail->Password = EMAIL_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = EMAIL_PORT;

        // Recipients
        $mail->setFrom(EMAIL_FROM, EMAIL_FROM_NAME);
        $mail->addAddress($to);

        // Content
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $body;

        // Send email
        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("Email could not be sent. Mailer Error: {$mail->ErrorInfo}");
        return false;
    }
}

// Function to create a new shipment
function createShipment($recipientName, $recipientEmail, $address, $weight) {
    // Basic validation
    if (empty($recipientName) || empty($recipientEmail) || empty($address) || empty($weight)) {
        throw new InvalidArgumentException('All shipment fields are required.');
    }

    // Simulate shipment creation (e.g., saving to a database)
    // ...

    // Notify the recipient
    $subject = 'Your Shipment is Created!';
    $body = "Hello $recipientName,<br>Your shipment has been created successfully. Details:<br>Address: $address<br>Weight: $weight kg";

    if (sendEmailNotification($recipientEmail, $subject, $body)) {
        return "Shipment created and notification sent to $recipientEmail.";
    } else {
        return "Shipment created but notification failed.";
    }
}

// Example usage
try {
    $message = createShipment('John Doe', 'johndoe@example.com', '123 Main St, City, Country', 2.5);
    echo $message;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```

Make sure to replace the SMTP configuration constants with your actual email server settings to ensure email notifications work correctly.
