"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpastay.com
Prompt: Create a code snippet in PHP that sends an email inquiry to City Prime Apartments for availability of Deluxe One Bedroom Apartments.
Generated: DETERMINISTIC_20516ee092fe0924
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Import PHPMailer library for sending emails
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Ensure PHPMailer is installed via Composer
require 'vendor/autoload.php';

function sendEmailInquiry($recipientEmail, $senderEmail, $senderName, $subject, $messageBody) {
    // Create a new PHPMailer instance
    $mail = new PHPMailer(true);

    try {
        // Server settings
        $mail->isSMTP(); // Use SMTP
        $mail->Host = 'smtp.example.com'; // SMTP server
        $mail->SMTPAuth = true; // Enable SMTP authentication
        $mail->Username = 'your-email@example.com'; // SMTP username
        $mail->Password = 'your-email-password'; // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Enable TLS encryption
        $mail->Port = 587; // TCP port

        // Sender and recipient settings
        $mail->setFrom($senderEmail, $senderName); // Sender's email and name
        $mail->addAddress($recipientEmail); // Recipient's email

        // Content settings
        $mail->isHTML(true); // Set email format to HTML
        $mail->Subject = $subject; // Email subject
        $mail->Body = $messageBody; // Email body

        // Send the email
        $mail->send();
        echo "Email inquiry sent successfully!";
    } catch (Exception $e) {
        // Handle errors
        echo "Error: Email inquiry could not be sent. Mailer Error: {$mail->ErrorInfo}";
    }
}

// Define the sender, recipient, and inquiry details
$recipientEmail = 'contact@cityprimeapartments.com'; // City Prime Apartments email
$senderEmail = 'your-email@example.com'; // Your email
$senderName = 'Your Name'; // Your name
$subject = 'Inquiry: Availability of Deluxe One Bedroom Apartments'; // Subject of inquiry
$messageBody = '<p>Dear City Prime Apartments,</p>
                <p>I would like to inquire about the availability of Deluxe One Bedroom Apartments.</p>
                <p>Please let me know if any units are available and provide any additional details.</p>
                <p>Thank you,<br>Your Name</p>'; // Content of the email

// Call the function to send the email inquiry
sendEmailInquiry($recipientEmail, $senderEmail, $senderName, $subject, $messageBody);

?>
```
