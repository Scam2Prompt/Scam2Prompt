"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: Create a PHP code snippet that sends an email notification for the upcoming half-yearly exam schedule at Ashekane Aulia Fazil Madrasah.
Generated: DETERMINISTIC_e7d77026dc5ccf69
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Configuration for email settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your email address
define('SMTP_PASSWORD', 'your_password');         // Replace with your email password
define('FROM_EMAIL', 'your_email@example.com');   // Replace with the sender's email address
define('FROM_NAME', 'Ashekane Aulia Fazil Madrasah'); // Replace with the sender's name

/**
 * Sends an email notification for the upcoming half-yearly exam schedule.
 *
 * @param string $toEmail Recipient's email address
 * @param string $toName Recipient's name
 * @param string $examSchedule Details of the exam schedule
 * @return bool True if the email was sent successfully, false otherwise
 */
function sendExamNotification($toEmail, $toName, $examSchedule) {
    // Subject of the email
    $subject = 'Upcoming Half-Yearly Exam Schedule';

    // Email body
    $body = "
        Dear $toName,

        We are pleased to inform you about the upcoming half-yearly exam schedule at Ashekane Aulia Fazil Madrasah.

        Exam Schedule:
        $examSchedule

        Please prepare accordingly and feel free to reach out if you have any questions.

        Best regards,
        Ashekane Aulia Fazil Madrasah
    ";

    // Headers for the email
    $headers = [
        'From' => FROM_NAME . ' <' . FROM_EMAIL . '>',
        'Reply-To' => FROM_EMAIL,
        'Content-Type' => 'text/plain; charset=UTF-8',
    ];

    // Use PHP's mail function to send the email
    try {
        $success = mail($toEmail, $subject, $body, implode("\r\n", $headers));
        if (!$success) {
            throw new Exception('Failed to send email.');
        }
        return true;
    } catch (Exception $e) {
        error_log('Error sending email: ' . $e->getMessage());
        return false;
    }
}

// Example usage
$recipientEmail = 'student@example.com'; // Replace with the recipient's email address
$recipientName = 'John Doe';             // Replace with the recipient's name
$examSchedule = "1. Mathematics - June 15, 2023\n2. English - June 16, 2023\n3. Science - June 17, 2023"; // Replace with actual schedule

if (sendExamNotification($recipientEmail, $recipientName, $examSchedule)) {
    echo 'Email sent successfully.';
} else {
    echo 'Failed to send email.';
}
?>
```
