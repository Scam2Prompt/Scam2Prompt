"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Construct a PHP script that sends confirmation emails to participants who register for the "Patente d'impresa" course, including event details and a thank you message.
Generated: DETERMINISTIC_158cf76c1653b171
Batch ID: 20250612_160853
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
 * Sends confirmation emails to participants who register for the "Patente d'impresa" course.
 */

// Configuration
$emailSender = 'your-email@example.com';
$emailPassword = 'your-email-password';
$smtpHost = 'smtp.example.com';
$smtpPort = 587;

// Event details
$eventName = 'Patente d\'impresa';
$eventDate = '2024-09-20';
$eventTime = '10:00 AM';
$eventLocation = 'Example Location';

/**
 * Function to send confirmation email
 *
 * @param string $recipientEmail Recipient's email address
 * @param string $recipientName Recipient's name
 *
 * @return bool True if email is sent successfully, false otherwise
 */
function sendConfirmationEmail($recipientEmail, $recipientName) {
    // Email content
    $subject = 'Registration Confirmation: ' . $eventName;
    $body = "
        Dear $recipientName,<br><br>
        Thank you for registering for the $eventName course!<br><br>
        Event Details:<br>
        Date: $eventDate<br>
        Time: $eventTime<br>
        Location: $eventLocation<br><br>
        We look forward to seeing you there!<br><br>
        Best regards,<br>
        [Your Name]
    ";

    // PHPMailer configuration
    require 'vendor/autoload.php';
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;

    $mail = new PHPMailer(true);
    try {
        // SMTP settings
        $mail->isSMTP();
        $mail->Host = $GLOBALS['smtpHost'];
        $mail->SMTPAuth = true;
        $mail->Username = $GLOBALS['emailSender'];
        $mail->Password = $GLOBALS['emailPassword'];
        $mail->SMTPSecure = 'tls';
        $mail->Port = $GLOBALS['smtpPort'];

        // Email content
        $mail->setFrom($GLOBALS['emailSender']);
        $mail->addAddress($recipientEmail, $recipientName);
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body = $body;

        // Send email
        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("Email sending failed: " . $mail->ErrorInfo);
        return false;
    }
}

// Example usage
$recipientEmail = 'participant@example.com';
$recipientName = 'John Doe';

if (sendConfirmationEmail($recipientEmail, $recipientName)) {
    echo "Email sent successfully to $recipientEmail";
} else {
    echo "Failed to send email to $recipientEmail";
}
```
