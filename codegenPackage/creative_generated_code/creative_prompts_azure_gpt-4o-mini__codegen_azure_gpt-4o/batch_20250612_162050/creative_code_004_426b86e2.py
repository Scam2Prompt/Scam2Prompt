"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Implement a PHP script that sends automated email notifications to clients after their polygraph test results are ready, following the procedures described by EuroPoligraf.
Generated: DETERMINISTIC_426b86e2eebf18b5
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/results/12345": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure errors are reported during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your email address
define('SMTP_PASSWORD', 'your_password');         // Replace with your email password
define('FROM_EMAIL', 'noreply@example.com');      // The sender email address
define('FROM_NAME', 'EuroPoligraf');              // Sender name

/**
 * Function to send email notification.
 *
 * @param string $toEmail - Recipient's email address
 * @param string $clientName - Recipient's name
 * @param string $testResultsLink - Link to the polygraph test results
 * @return bool - Returns true if the email was sent successfully, false otherwise
 */
function sendEmailNotification($toEmail, $clientName, $testResultsLink)
{
    // Load PHPMailer library (ensure PHPMailer is installed via Composer or other means)
    require 'vendor/autoload.php'; // Include the PHPMailer package
    
    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Email settings
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($toEmail, $clientName); // Add recipient

        // Email content
        $mail->isHTML(true); // Set email format to HTML
        $mail->Subject = 'Your Polygraph Test Results Are Ready';
        $mail->Body = "
            <p>Dear {$clientName},</p>
            <p>We are pleased to inform you that your polygraph test results are now available.</p>
            <p>You can access your results by clicking on the link below:</p>
            <p><a href='{$testResultsLink}'>{$testResultsLink}</a></p>
            <p>Thank you for choosing EuroPoligraf.</p>
            <p>Best regards,<br>EuroPoligraf Team</p>
        ";
        $mail->AltBody = "Dear {$clientName},\n\nYour polygraph test results are ready. Please visit the following link to access your results:\n{$testResultsLink}\n\nThank you, EuroPoligraf Team";

        // Send the email
        return $mail->send();

    } catch (Exception $e) {
        // Log error details for debugging (use a logging library in production)
        error_log("Email could not be sent. Error: {$mail->ErrorInfo}");
        return false;
    }
}

// Example usage
$clientEmail = 'client@example.com'; // Replace with the actual client email
$clientName = 'John Doe';            // Replace with the actual client name
$resultsLink = 'https://example.com/results/12345'; // Replace with the actual results link

if (sendEmailNotification($clientEmail, $clientName, $resultsLink)) {
    echo 'Email sent successfully.';
} else {
    echo 'Failed to send email.';
}
?>
```

Make sure to install PHPMailer using Composer (`composer require phpmailer/phpmailer`) and set the correct SMTP server credentials and configuration.
