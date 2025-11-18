"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Create a script in PHP to send automated email responses to customers inquiring about machinery parts and services, using the contact details provided on Track Diesel Peru's website.
Generated: DETERMINISTIC_58e328949fde2edf
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Script: Automated Email Response System
 * Purpose: Automatically send email responses to customers inquiring about machinery parts and services.
 * Author: Professional Software Developer
 * Last Updated: YYYY-MM-DD
 */

// Configuration for email settings
define('SMTP_HOST', 'smtp.your-email-provider.com'); // Replace with your SMTP host
define('SMTP_PORT', 587); // Usually 587 for TLS or 465 for SSL
define('SMTP_USERNAME', 'your-email@example.com'); // Replace with your SMTP username
define('SMTP_PASSWORD', 'your-email-password'); // Replace with your SMTP password
define('FROM_EMAIL', 'info@trackdieselperu.com'); // The "From" email address
define('FROM_NAME', 'Track Diesel Peru'); // The "From" name
define('SUBJECT', 'Thank you for your inquiry!'); // The email subject

// Function to send an automated email response
function sendAutomatedResponse($toEmail, $toName) {
    // Validate input parameters
    if (empty($toEmail) || empty($toName) || !filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email address or name provided.');
    }

    // Email content
    $message = <<<EOD
Dear $toName,

Thank you for reaching out to Track Diesel Peru. We have received your inquiry regarding machinery parts and services. Our team will review your message and get back to you shortly.

If you have any urgent questions, feel free to call us at +51 (Your Phone Number) or reply to this email.

Best regards,
Track Diesel Peru Team
EOD;

    // Using PHPMailer for email handling
    require 'PHPMailer/PHPMailer.php';
    require 'PHPMailer/SMTP.php';
    require 'PHPMailer/Exception.php';

    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->Port = SMTP_PORT;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS; // Use TLS encryption

        // Sender and recipient details
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($toEmail, $toName);

        // Email content
        $mail->Subject = SUBJECT;
        $mail->Body = $message;

        // Send the email
        if ($mail->send()) {
            return "Email successfully sent to $toName ($toEmail).";
        } else {
            throw new Exception("Failed to send email. Error: " . $mail->ErrorInfo);
        }
    } catch (Exception $e) {
        // Handle errors gracefully
        error_log("Email error: " . $e->getMessage());
        return "An error occurred while sending the email. Please try again.";
    }
}

// Example usage
try {
    // Replace with actual contact details retrieved from the website
    $customerEmail = 'customer@example.com';
    $customerName = 'John Doe';

    // Send the email
    $result = sendAutomatedResponse($customerEmail, $customerName);
    echo $result;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
