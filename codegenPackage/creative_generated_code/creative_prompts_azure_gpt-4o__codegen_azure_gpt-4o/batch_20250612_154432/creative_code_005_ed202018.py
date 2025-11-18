"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Create a PHP script to send automated email confirmations to customers after they book plumbing services with Certified Plumbers Graham, TX, including details of the service and appointment time.
Generated: DETERMINISTIC_ed202018df628727
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php
// Configuration file to store SMTP details and other constants
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587); // Replace with your SMTP port
define('SMTP_USERNAME', 'your_email@example.com'); // Replace with your email
define('SMTP_PASSWORD', 'your_email_password'); // Replace with your email password
define('COMPANY_EMAIL', 'bookings@certifiedplumbersgrahamtx.com'); // Replace with company email
define('COMPANY_NAME', 'Certified Plumbers Graham, TX');

// emailConfirmation.php
// Main script for sending automated email confirmations

// Include PHPMailer library
require 'vendor/autoload.php'; // Ensure you have installed PHPMailer via Composer

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

/**
 * Sends an email confirmation to a customer.
 *
 * @param string $customerEmail Customer's email address
 * @param string $customerName Customer's full name
 * @param string $serviceDetails Details of the plumbing service booked
 * @param string $appointmentTime Scheduled time of the appointment
 * @return bool Returns true if email is sent successfully, false otherwise
 */
function sendEmailConfirmation($customerEmail, $customerName, $serviceDetails, $appointmentTime) {
    $mail = new PHPMailer(true);

    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Sender and recipient details
        $mail->setFrom(COMPANY_EMAIL, COMPANY_NAME);
        $mail->addAddress($customerEmail, $customerName);

        // Email content
        $mail->isHTML(true); // Set email format to HTML
        $mail->Subject = 'Your Plumbing Service Appointment Confirmation';
        $mail->Body = "
            <h1>Appointment Confirmation</h1>
            <p>Dear $customerName,</p>
            <p>Thank you for booking our plumbing services. Here are the details of your appointment:</p>
            <ul>
                <li><strong>Service:</strong> $serviceDetails</li>
                <li><strong>Appointment Time:</strong> $appointmentTime</li>
            </ul>
            <p>If you have any questions or need to reschedule, please contact us at " . COMPANY_EMAIL . ".</p>
            <p>Best regards,<br>" . COMPANY_NAME . "</p>
        ";

        // Send email
        $mail->send();
        return true;
    } catch (Exception $e) {
        // Log error message for debugging purposes
        error_log("Email could not be sent. Error: {$mail->ErrorInfo}");
        return false;
    }
}

// Example usage
// Replace these variables with actual data from your booking system
$customerEmail = 'customer@example.com';
$customerName = 'John Doe';
$serviceDetails = 'Pipe repair and maintenance';
$appointmentTime = '2023-10-15 14:00:00';

// Send email and check result
if (sendEmailConfirmation($customerEmail, $customerName, $serviceDetails, $appointmentTime)) {
    echo 'Email confirmation sent successfully!';
} else {
    echo 'Failed to send email confirmation.';
}
?>
```

Make sure you have installed PHPMailer via Composer with:
```
composer require phpmailer/phpmailer
```

Save the configuration settings in a separate file (`config.php`) for easy maintainability and security.
