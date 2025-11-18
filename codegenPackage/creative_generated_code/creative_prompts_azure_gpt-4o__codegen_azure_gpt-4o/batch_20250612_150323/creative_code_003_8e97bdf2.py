"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in PHP to send automated email reminders for routine HVAC maintenance, emphasizing the importance of energy-efficient system operation and dirt/neglect prevention, as highlighted by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_8e97bdf299cfc00a
Batch ID: 20250612_150323
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
 * Automated HVAC Maintenance Reminder Email System
 * 
 * Sends automated email reminders to customers emphasizing the importance
 * of routine HVAC maintenance, energy efficiency, and dirt/neglect prevention.
 * 
 * @package HVACMaintenanceReminder
 * @author Quality Sheet Metal, Inc.
 * @version 1.0
 */

// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_PORT', 587);               // Replace with your SMTP port (e.g., 587 for TLS)
define('SMTP_USERNAME', 'your-email@example.com'); // Replace with your email
define('SMTP_PASSWORD', 'your-password');         // Replace with your email password
define('FROM_EMAIL', 'no-reply@qualitysheetmetal.com'); // Sender email
define('FROM_NAME', 'Quality Sheet Metal, Inc.');       // Sender name

// Load PHPMailer library (Composer installation is recommended)
// Command to install: composer require phpmailer/phpmailer
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Include PHPMailer classes
require 'vendor/autoload.php';

/**
 * Sends an email with the HVAC maintenance reminder.
 * 
 * @param string $toEmail Recipient's email
 * @param string $toName Recipient's name
 * 
 * @return bool True if the email was sent successfully, false otherwise.
 */
function sendMaintenanceReminder($toEmail, $toName) {
    $mail = new PHPMailer(true);
    
    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Use TLS
        $mail->Port = SMTP_PORT;

        // Sender information
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($toEmail, $toName); // Recipient
        
        // Email content
        $mail->isHTML(true);
        $mail->Subject = 'HVAC Maintenance Reminder';
        $mail->Body = "
            <p>Dear {$toName},</p>
            <p>We hope this email finds you well. At Quality Sheet Metal, Inc., we emphasize the 
            importance of routine <strong>HVAC maintenance</strong> to ensure optimal energy-efficient 
            operation and to prevent dirt and neglect from impacting your system's performance.</p>
            <p>Regular maintenance helps:</p>
            <ul>
                <li>Improve energy efficiency and save on utility costs.</li>
                <li>Extend the life of your HVAC system.</li>
                <li>Prevent unexpected breakdowns and costly repairs.</li>
            </ul>
            <p>Contact us today to schedule your maintenance appointment!</p>
            <p>Best regards,<br>Quality Sheet Metal, Inc.</p>
        ";
        $mail->AltBody = "Dear {$toName},\n\nWe emphasize the importance of routine HVAC maintenance to ensure optimal energy-efficient operation and to prevent dirt and neglect from impacting your system. Contact us today to schedule your maintenance appointment!\n\nBest regards,\nQuality Sheet Metal, Inc.";

        // Send email
        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("Mailer Error: " . $mail->ErrorInfo); // Log error details
        return false;
    }
}

// Example usage: Provide recipient details
$recipients = [
    ['email' => 'customer1@example.com', 'name' => 'John Doe'],
    ['email' => 'customer2@example.com', 'name' => 'Jane Smith'],
];

// Loop through recipients and send reminders
foreach ($recipients as $recipient) {
    $success = sendMaintenanceReminder($recipient['email'], $recipient['name']);
    if ($success) {
        echo "Maintenance reminder sent to {$recipient['name']} ({$recipient['email']}).\n";
    } else {
        echo "Failed to send reminder to {$recipient['name']} ({$recipient['email']}).\n";
    }
}
?>
```
