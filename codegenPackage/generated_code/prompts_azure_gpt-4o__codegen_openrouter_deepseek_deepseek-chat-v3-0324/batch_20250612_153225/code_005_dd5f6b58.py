"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Create a PHP function to send email confirmations for appointments booked through a reflexology service website, using the customer's email address and appointment details.
Generated: DETERMINISTIC_dd5f6b582f929a52
Batch ID: 20250612_153225
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
 * Sends an email confirmation for a reflexology appointment booking.
 *
 * @param string $customerEmail The customer's email address.
 * @param string $customerName The customer's name.
 * @param string $appointmentDate The appointment date and time.
 * @param string $appointmentType The type of reflexology service booked.
 * @param string $therapistName The name of the assigned therapist.
 * @return bool True if the email was sent successfully, false otherwise.
 * @throws Exception If email sending fails.
 */
function sendAppointmentConfirmation(
    string $customerEmail,
    string $customerName,
    string $appointmentDate,
    string $appointmentType,
    string $therapistName
): bool {
    // Validate email address
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address provided");
    }

    // Validate required fields
    $requiredFields = [$customerName, $appointmentDate, $appointmentType, $therapistName];
    foreach ($requiredFields as $field) {
        if (empty(trim($field))) {
            throw new InvalidArgumentException("All appointment details must be provided");
        }
    }

    // Email subject
    $subject = "Your Reflexology Appointment Confirmation";

    // Email body
    $body = "
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; }
            .header { color: #2c3e50; }
            .details { margin: 20px 0; }
            .footer { margin-top: 20px; font-size: 0.9em; color: #7f8c8d; }
        </style>
    </head>
    <body>
        <h2 class='header'>Appointment Confirmation</h2>
        <div class='details'>
            <p>Dear $customerName,</p>
            <p>Your reflexology appointment has been confirmed with the following details:</p>
            <p><strong>Service:</strong> $appointmentType</p>
            <p><strong>Date & Time:</strong> $appointmentDate</p>
            <p><strong>Therapist:</strong> $therapistName</p>
        </div>
        <div class='footer'>
            <p>Thank you for choosing our service. Please arrive 10 minutes before your appointment.</p>
            <p>If you need to reschedule or cancel, please contact us at least 24 hours in advance.</p>
        </div>
    </body>
    </html>
    ";

    // Email headers
    $headers = "MIME-Version: 1.0\r\n";
    $headers .= "Content-type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Reflexology Services <bookings@reflexology.example.com>\r\n";
    $headers .= "Reply-To: bookings@reflexology.example.com\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    try {
        // Send the email
        $mailSent = mail($customerEmail, $subject, $body, $headers);
        
        if (!$mailSent) {
            throw new Exception("Failed to send email. Mail server error.");
        }
        
        return true;
    } catch (Exception $e) {
        error_log("Email sending error: " . $e->getMessage());
        throw $e;
    }
}
?>
```
