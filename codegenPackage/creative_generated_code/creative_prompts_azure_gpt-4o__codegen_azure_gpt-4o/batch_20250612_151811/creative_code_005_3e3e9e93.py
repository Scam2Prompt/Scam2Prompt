"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Write a script in PHP to send automated email notifications to KEK Insurance Brokers customers for claims updates or policy renewals, using the contact details format provided on their website.
Generated: DETERMINISTIC_3e3e9e93a3c5c39c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// KEK Insurance Brokers Automated Email Notification Script

/**
 * Configuration for email service
 */
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your email server port
define('SMTP_USERNAME', 'your-email@example.com'); // Replace with your SMTP username
define('SMTP_PASSWORD', 'your-email-password');   // Replace with your SMTP password
define('EMAIL_FROM', 'no-reply@kekinsurance.com'); // Replace with sender email
define('EMAIL_FROM_NAME', 'KEK Insurance Brokers');

/**
 * Simulated customer data as per the contact details format on KEK Insurance Brokers' website.
 * In production, replace this with a database query or API call to fetch real customer data.
 */
$customers = [
    ['name' => 'John Doe', 'email' => 'john.doe@example.com', 'notification_type' => 'policy_renewal', 'policy_number' => 'PN123456'],
    ['name' => 'Jane Smith', 'email' => 'jane.smith@example.com', 'notification_type' => 'claims_update', 'claim_number' => 'CL654321'],
    // Add more customers as needed
];

/**
 * Function to send an email notification
 *
 * @param string $toEmail The recipient's email address
 * @param string $toName The recipient's name
 * @param string $subject The email subject
 * @param string $body The email body
 * @return bool True if email sent successfully, False otherwise
 */
function sendEmailNotification($toEmail, $toName, $subject, $body)
{
    // Load the PHPMailer library
    require 'PHPMailer/PHPMailer.php';
    require 'PHPMailer/SMTP.php';
    require 'PHPMailer/Exception.php';

    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // Configure SMTP settings
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->Port = SMTP_PORT;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;

        // Configure email headers
        $mail->setFrom(EMAIL_FROM, EMAIL_FROM_NAME);
        $mail->addAddress($toEmail, $toName);
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->isHTML(true);

        // Send the email
        if (!$mail->send()) {
            // Log error for debugging
            error_log("Error sending email to $toEmail: " . $mail->ErrorInfo);
            return false;
        }

        return true;
    } catch (Exception $e) {
        // Log exception for debugging
        error_log("Exception while sending email to $toEmail: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to generate email content based on notification type
 *
 * @param array $customer The customer data
 * @return array Associative array containing 'subject' and 'body'
 */
function generateEmailContent($customer)
{
    switch ($customer['notification_type']) {
        case 'policy_renewal':
            $subject = "Policy Renewal Reminder for Policy #{$customer['policy_number']}";
            $body = "<p>Dear {$customer['name']},</p>
                     <p>This is a reminder that your policy #{$customer['policy_number']} is due for renewal soon. Please contact us at your earliest convenience to ensure continued coverage.</p>
                     <p>Sincerely,<br>KEK Insurance Brokers</p>";
            break;

        case 'claims_update':
            $subject = "Claims Update for Claim #{$customer['claim_number']}";
            $body = "<p>Dear {$customer['name']},</p>
                     <p>We have an update regarding your claim #{$customer['claim_number']}. Please log in to your account or contact us for more details.</p>
                     <p>Sincerely,<br>KEK Insurance Brokers</p>";
            break;

        default:
            $subject = "Notification from KEK Insurance Brokers";
            $body = "<p>Dear {$customer['name']},</p>
                     <p>We have an important update for you. Please contact us for more information.</p>
                     <p>Sincerely,<br>KEK Insurance Brokers</p>";
            break;
    }

    return ['subject' => $subject, 'body' => $body];
}

/**
 * Main script execution
 */
foreach ($customers as $customer) {
    $emailContent = generateEmailContent($customer);

    $emailSent = sendEmailNotification(
        $customer['email'],
        $customer['name'],
        $emailContent['subject'],
        $emailContent['body']
    );

    if ($emailSent) {
        echo "Email sent successfully to {$customer['name']} ({$customer['email']}).\n";
    } else {
        echo "Failed to send email to {$customer['name']} ({$customer['email']}).\n";
    }
}

?>
```
