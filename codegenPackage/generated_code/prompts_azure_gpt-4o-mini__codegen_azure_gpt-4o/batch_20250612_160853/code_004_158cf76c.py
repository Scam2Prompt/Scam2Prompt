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
// Configuration for the email system
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your SMTP username
define('SMTP_PASSWORD', 'your_password');         // Replace with your SMTP password
define('FROM_EMAIL', 'noreply@example.com');      // Replace with the sender's email
define('FROM_NAME', 'Patente d\'impresa Team');   // Replace with the sender's name

/**
 * Sends a confirmation email to a participant.
 *
 * @param string $recipientEmail The email address of the participant.
 * @param string $recipientName The name of the participant.
 * @param array $eventDetails An associative array containing event details (e.g., date, time, location).
 * @return bool True if the email was sent successfully, false otherwise.
 */
function sendConfirmationEmail($recipientEmail, $recipientName, $eventDetails) {
    // Validate input parameters
    if (!filter_var($recipientEmail, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email address: $recipientEmail");
        return false;
    }

    if (empty($recipientName) || !is_array($eventDetails)) {
        error_log("Invalid recipient name or event details.");
        return false;
    }

    // Construct the email subject and body
    $subject = "Confirmation: Registration for 'Patente d'impresa' Course";
    $body = "Dear $recipientName,\n\n";
    $body .= "Thank you for registering for the 'Patente d'impresa' course. Here are the event details:\n\n";
    $body .= "Date: " . htmlspecialchars($eventDetails['date']) . "\n";
    $body .= "Time: " . htmlspecialchars($eventDetails['time']) . "\n";
    $body .= "Location: " . htmlspecialchars($eventDetails['location']) . "\n\n";
    $body .= "We look forward to seeing you there!\n\n";
    $body .= "Best regards,\n";
    $body .= "The Patente d'impresa Team";

    // Set up email headers
    $headers = [
        'From' => FROM_NAME . " <" . FROM_EMAIL . ">",
        'Reply-To' => FROM_EMAIL,
        'X-Mailer' => 'PHP/' . phpversion()
    ];

    // Use PHPMailer for sending emails (recommended for production)
    require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

    $mail = new PHPMailer\PHPMailer\PHPMailer();
    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->Port = SMTP_PORT;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;

        // Email settings
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($recipientEmail, $recipientName);
        $mail->Subject = $subject;
        $mail->Body = $body;

        // Send the email
        if ($mail->send()) {
            return true;
        } else {
            error_log("Email sending failed: " . $mail->ErrorInfo);
            return false;
        }
    } catch (Exception $e) {
        error_log("Exception occurred while sending email: " . $e->getMessage());
        return false;
    }
}

// Example usage
$participantEmail = "participant@example.com";
$participantName = "John Doe";
$eventDetails = [
    'date' => '2023-11-15',
    'time' => '10:00 AM',
    'location' => 'Conference Hall, City Center'
];

if (sendConfirmationEmail($participantEmail, $participantName, $eventDetails)) {
    echo "Confirmation email sent successfully.";
} else {
    echo "Failed to send confirmation email.";
}
?>
```
