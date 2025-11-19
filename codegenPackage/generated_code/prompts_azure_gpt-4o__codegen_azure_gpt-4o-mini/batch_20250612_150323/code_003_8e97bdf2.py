"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in PHP to send automated email reminders for routine HVAC maintenance, emphasizing the importance of energy-efficient system operation and dirt/neglect prevention, as highlighted by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_8e97bdf299cfc00a
Batch ID: 20250612_150323
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
 * Automated Email Reminder for HVAC Maintenance
 * 
 * This script sends automated email reminders for routine HVAC maintenance,
 * emphasizing the importance of energy-efficient system operation and dirt/neglect prevention.
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// Configuration for email
define('SMTP_SERVER', 'smtp.example.com'); // SMTP server address
define('SMTP_PORT', 587); // SMTP server port
define('SMTP_USER', 'your_email@example.com'); // SMTP username
define('SMTP_PASS', 'your_password'); // SMTP password
define('FROM_EMAIL', 'noreply@example.com'); // From email address
define('FROM_NAME', 'Quality Sheet Metal, Inc.'); // From name

/**
 * Sends an email reminder for HVAC maintenance.
 *
 * @param string $toEmail Recipient's email address
 * @param string $toName Recipient's name
 * @return bool True on success, false on failure
 */
function sendEmailReminder($toEmail, $toName) {
    // Create the email subject and body
    $subject = 'Reminder: Routine HVAC Maintenance';
    $body = "Dear $toName,\n\n" .
            "This is a friendly reminder from Quality Sheet Metal, Inc. to schedule your routine HVAC maintenance.\n" .
            "Regular maintenance is crucial for ensuring energy-efficient operation and preventing dirt and neglect that can lead to costly repairs.\n\n" .
            "Please contact us to schedule your maintenance appointment.\n\n" .
            "Best regards,\n" .
            "Quality Sheet Metal, Inc.";

    // Set headers
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Use PHPMailer for sending email
    require 'PHPMailer/PHPMailerAutoload.php'; // Ensure PHPMailer is included

    $mail = new PHPMailer\PHPMailer\PHPMailer();
    $mail->isSMTP();
    $mail->Host = SMTP_SERVER;
    $mail->Port = SMTP_PORT;
    $mail->SMTPAuth = true;
    $mail->Username = SMTP_USER;
    $mail->Password = SMTP_PASS;
    $mail->setFrom(FROM_EMAIL, FROM_NAME);
    $mail->addAddress($toEmail, $toName);
    $mail->Subject = $subject;
    $mail->Body = $body;

    // Attempt to send the email
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
$recipients = [
    ['email' => 'customer1@example.com', 'name' => 'Customer One'],
    ['email' => 'customer2@example.com', 'name' => 'Customer Two'],
];

foreach ($recipients as $recipient) {
    $result = sendEmailReminder($recipient['email'], $recipient['name']);
    if ($result) {
        echo "Reminder sent to " . $recipient['name'] . " (" . $recipient['email'] . ")\n";
    } else {
        echo "Failed to send reminder to " . $recipient['name'] . " (" . $recipient['email'] . ")\n";
    }
}
?>
```
