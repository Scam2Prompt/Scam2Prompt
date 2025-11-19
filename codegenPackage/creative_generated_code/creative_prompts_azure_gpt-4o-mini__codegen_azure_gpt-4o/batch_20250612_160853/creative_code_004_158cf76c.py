"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Construct a PHP script that sends confirmation emails to participants who register for the "Patente d'impresa" course, including event details and a thank you message.
Generated: DETERMINISTIC_158cf76c1653b171
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port (e.g., 25, 465, or 587)
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your SMTP username
define('SMTP_PASSWORD', 'your_email_password');   // Replace with your SMTP password
define('FROM_EMAIL', 'no-reply@example.com');     // Replace with your sender email
define('FROM_NAME', 'Patente d\'impresa Team');   // Replace with your sender's name

// Include external dependencies (e.g., PHPMailer)
require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

/**
 * Function to send confirmation email to a participant.
 *
 * @param string $participantEmail Participant's email address.
 * @param string $participantName  Participant's name.
 * @param string $eventDate        Event date (e.g., "March 15th, 2024").
 * @return bool                    Returns true if the email is sent successfully, false otherwise.
 */
function sendConfirmationEmail($participantEmail, $participantName, $eventDate)
{
    // Initialize PHPMailer
    $mail = new PHPMailer(true);

    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host       = SMTP_HOST;
        $mail->Port       = SMTP_PORT;
        $mail->SMTPAuth   = true;
        $mail->Username   = SMTP_USERNAME;
        $mail->Password   = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Use STARTTLS for secure connection

        // Email headers
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($participantEmail, $participantName); // Recipient's email and name

        // Email content
        $mail->isHTML(true); // Set email format to HTML
        $mail->Subject = 'Registration Confirmation: Patente d\'impresa Course';
        
        // Compose the email body
        $emailBody = "
            <html>
            <body>
                <h1>Thank you for registering, $participantName!</h1>
                <p>We are thrilled to confirm your registration for the <strong>Patente d'impresa</strong> course.</p>
                <p><strong>Event Details:</strong></p>
                <ul>
                    <li>Date: $eventDate</li>
                    <li>Location: Online (details will be shared closer to the event date)</li>
                </ul>
                <p>Thank you for your interest and participation!</p>
                <p>Best regards,<br>The Patente d'impresa Team</p>
            </body>
            </html>
        ";

        $mail->Body = $emailBody;

        // Send the email
        $mail->send();
        return true; // Email sent successfully
    } catch (Exception $e) {
        // Log the error (optional)
        error_log("Email error: " . $mail->ErrorInfo);
        return false; // Email failed to send
    }
}

// Example usage
// Replace with actual participant details
$participantEmail = 'john.doe@example.com';
$participantName = 'John Doe';
$eventDate = 'March 15th, 2024';

// Send confirmation email
if (sendConfirmationEmail($participantEmail, $participantName, $eventDate)) {
    echo "Confirmation email sent successfully to $participantEmail.";
} else {
    echo "Failed to send confirmation email to $participantEmail.";
}
?>
```
