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
// Define constants for the email configuration
define('SMTP_HOST', 'smtp.example.com'); // SMTP server address
define('SMTP_PORT', 587); // SMTP server port
define('SMTP_USER', 'your-email@example.com'); // SMTP username
define('SMTP_PASS', 'your-email-password'); // SMTP password
define('FROM_EMAIL', 'no-reply@example.com'); // From email address
define('FROM_NAME', 'Patente d\'impresa Course'); // From name

// Function to send confirmation email
function sendConfirmationEmail($to, $participantName) {
    // Event details
    $eventDetails = [
        'course_name' => 'Patente d\'impresa',
        'date' => '2023-11-15',
        'time' => '10:00 AM - 4:00 PM',
        'location' => '123 Business St, Business City',
    ];

    // Create the email subject and body
    $subject = 'Registration Confirmation for ' . $eventDetails['course_name'];
    $body = "Dear $participantName,\n\n";
    $body .= "Thank you for registering for the '{$eventDetails['course_name']}' course.\n";
    $body .= "Here are the event details:\n";
    $body .= "Date: " . $eventDetails['date'] . "\n";
    $body .= "Time: " . $eventDetails['time'] . "\n";
    $body .= "Location: " . $eventDetails['location'] . "\n\n";
    $body .= "We look forward to seeing you there!\n\n";
    $body .= "Best regards,\n";
    $body .= FROM_NAME;

    // Set headers
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Use PHPMailer for sending email
    require 'PHPMailer/PHPMailerAutoload.php'; // Ensure PHPMailer is included

    $mail = new PHPMailer\PHPMailer\PHPMailer();
    $mail->isSMTP();
    $mail->Host = SMTP_HOST;
    $mail->Port = SMTP_PORT;
    $mail->SMTPAuth = true;
    $mail->Username = SMTP_USER;
    $mail->Password = SMTP_PASS;
    $mail->setFrom(FROM_EMAIL, FROM_NAME);
    $mail->addAddress($to);
    $mail->Subject = $subject;
    $mail->Body = $body;

    // Attempt to send the email and handle errors
    try {
        if (!$mail->send()) {
            throw new Exception('Email could not be sent. Mailer Error: ' . $mail->ErrorInfo);
        }
        return true; // Email sent successfully
    } catch (Exception $e) {
        error_log($e->getMessage()); // Log error message
        return false; // Email sending failed
    }
}

// Example usage
$participantEmail = 'participant@example.com'; // Replace with actual participant email
$participantName = 'John Doe'; // Replace with actual participant name

if (sendConfirmationEmail($participantEmail, $participantName)) {
    echo "Confirmation email sent successfully to $participantName.";
} else {
    echo "Failed to send confirmation email to $participantName.";
}
?>
```

Make sure to replace the SMTP configuration values with your actual email server details and include the PHPMailer library in your project for this script to work correctly.
