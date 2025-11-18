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
// Define necessary configurations
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_USER', 'your-email@example.com'); // Replace with your email
define('SMTP_PASS', 'your-email-password'); // Replace with your email password
define('SMTP_PORT', 587); // Use 465 for SSL, 587 for TLS
define('FROM_EMAIL', 'no-reply@example.com'); // Replace with the email you want to send from
define('FROM_NAME', 'Certified Plumbers'); // Name that appears in the "from" field

/**
 * Sends a confirmation email to the customer after a plumbing service booking.
 *
 * @param string $customerEmail The customer's email address.
 * @param string $serviceDetails Details of the plumbing service booked.
 * @param string $appointmentTime The time of the appointment.
 * @return void
 */
function sendConfirmationEmail($customerEmail, $serviceDetails, $appointmentTime)
{
    // Create the email subject and message
    $subject = 'Your Plumbing Service Confirmation';
    $message = "
    <html>
    <head>
        <title>Plumbing Service Confirmation</title>
    </head>
    <body>
        <h2>Thank you for booking with us!</h2>
        <p>You have successfully scheduled the following plumbing service:</p>
        <p><strong>Service Details:</strong> $serviceDetails</p>
        <p><strong>Appointment Time:</strong> $appointmentTime</p>
        <p>We look forward to serving you!</p>
        <p>Best regards,<br/>Certified Plumbers</p>
    </body>
    </html>
    ";

    // Set content-type header for HTML email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: " . FROM_NAME . " <" . FROM_EMAIL . ">" . "\r\n";

    // Attempt to send the email
    try {
        if (!mail($customerEmail, $subject, $message, $headers)) {
            throw new Exception('Email could not be sent. Please check the email configuration.');
        }
        echo "Confirmation email sent successfully to $customerEmail.";
    } catch (Exception $e) {
        // Log the error for debugging
        error_log($e->getMessage());
        echo "Failed to send confirmation email. Please try again later.";
    }
}

// Example usage (replace with actual data)
// sendConfirmationEmail('customer@example.com', 'Leak Repair in Kitchen', '2023-10-25 14:00:00');
?>
```

**Note:** Make sure to replace SMTP configuration values and the example usage data with actual values in a production environment.
