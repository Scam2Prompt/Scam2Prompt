"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a PHP script to send automated email notifications to prospective students about ISIV's open enrollment for 2025, referencing specific programs like "Administración de Empresas" and "Análisis de Sistemas."
Generated: DETERMINISTIC_19a40cef23b06dc3
Batch ID: 20250612_154209
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
 * ISIV Enrollment Notification Script
 * 
 * This script sends automated email notifications to prospective students 
 * regarding ISIV's open enrollment for 2025. It highlights programs such 
 * as "Administración de Empresas" and "Análisis de Sistemas".
 * 
 * Author: Professional Software Developer
 * Date: YYYY-MM-DD
 */

// Load dependencies
require 'PHPMailer.php';
require 'SMTP.php';
require 'Exception.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Define constants
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);                // Replace with your SMTP port
define('SMTP_USERNAME', 'your-email@example.com'); // Replace with your email
define('SMTP_PASSWORD', 'your-email-password');   // Replace with your email password
define('FROM_EMAIL', 'your-email@example.com');   // Replace with your sender email
define('FROM_NAME', 'ISIV Admissions');          // Replace with your sender name

/**
 * Sends an email to notify prospective students about ISIV's open enrollment.
 * 
 * @param string $recipientEmail The email address of the recipient.
 * @param string $recipientName  The name of the recipient.
 * @return bool True if the email was sent successfully, false otherwise.
 */
function sendEnrollmentNotification($recipientEmail, $recipientName) {
    try {
        // Initialize PHPMailer instance
        $mail = new PHPMailer(true);

        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Sender information
        $mail->setFrom(FROM_EMAIL, FROM_NAME);

        // Recipient information
        $mail->addAddress($recipientEmail, $recipientName);

        // Email content
        $mail->isHTML(true);
        $mail->Subject = 'ISIV Open Enrollment 2025 - Programs Highlight';
        $mail->Body = "
            <h1>Welcome to ISIV's Open Enrollment for 2025!</h1>
            <p>Dear $recipientName,</p>
            <p>We are excited to announce that enrollment for the year 2025 is now open at ISIV. 
            Explore our exceptional programs, including:</p>
            <ul>
                <li><strong>Administración de Empresas</strong></li>
                <li><strong>Análisis de Sistemas</strong></li>
            </ul>
            <p>Don't miss this opportunity to advance your education and career. 
            Visit our website or contact us for more details.</p>
            <p>Best regards,<br>The ISIV Admissions Team</p>
        ";

        // Send email
        $mail->send();

        return true;
    } catch (Exception $e) {
        // Log error for debugging
        error_log("Email error: " . $mail->ErrorInfo);
        return false;
    }
}

// List of prospective students (example data)
$students = [
    ['email' => 'student1@example.com', 'name' => 'John Doe'],
    ['email' => 'student2@example.com', 'name' => 'Jane Smith'],
    ['email' => 'student3@example.com', 'name' => 'Carlos Pérez']
];

// Send notifications to all students
foreach ($students as $student) {
    $success = sendEnrollmentNotification($student['email'], $student['name']);
    if ($success) {
        echo "Notification sent to {$student['name']} ({$student['email']}).\n";
    } else {
        echo "Failed to send notification to {$student['name']} ({$student['email']}).\n";
    }
}
?>
```

This PHP script uses the PHPMailer library for sending emails. Ensure you have properly installed PHPMailer and configured your SMTP settings. Adjust the `SMTP_HOST`, `SMTP_USERNAME`, and `SMTP_PASSWORD` constants to match your email server credentials.
