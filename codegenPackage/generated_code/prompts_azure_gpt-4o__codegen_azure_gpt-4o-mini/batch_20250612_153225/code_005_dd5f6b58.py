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
 * Sends an email confirmation for an appointment.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $appointmentDate The date of the appointment.
 * @param string $appointmentTime The time of the appointment.
 * @param string $serviceType The type of reflexology service booked.
 * @return bool Returns true if the email was sent successfully, false otherwise.
 */
function sendAppointmentConfirmation($customerEmail, $appointmentDate, $appointmentTime, $serviceType) {
    // Validate email address
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address provided.");
    }

    // Prepare email subject and message
    $subject = "Appointment Confirmation for Your Reflexology Service";
    $message = "Dear Customer,\n\n";
    $message .= "Thank you for booking an appointment with us.\n";
    $message .= "Here are your appointment details:\n";
    $message .= "Service Type: $serviceType\n";
    $message .= "Date: $appointmentDate\n";
    $message .= "Time: $appointmentTime\n\n";
    $message .= "We look forward to seeing you!\n";
    $message .= "Best regards,\n";
    $message .= "Reflexology Service Team";

    // Set headers
    $headers = "From: no-reply@reflexologyservice.com\r\n";
    $headers .= "Reply-To: support@reflexologyservice.com\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email
    if (mail($customerEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log error or handle failure
        error_log("Failed to send email to $customerEmail");
        return false; // Email sending failed
    }
}

// Example usage
try {
    $emailSent = sendAppointmentConfirmation("customer@example.com", "2023-10-15", "14:00", "Full Body Reflexology");
    if ($emailSent) {
        echo "Confirmation email sent successfully.";
    } else {
        echo "Failed to send confirmation email.";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
