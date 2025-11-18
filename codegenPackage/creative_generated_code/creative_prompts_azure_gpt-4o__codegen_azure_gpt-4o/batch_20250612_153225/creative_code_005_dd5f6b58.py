"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Create a PHP function to send email confirmations for appointments booked through a reflexology service website, using the customer's email address and appointment details.
Generated: DETERMINISTIC_dd5f6b582f929a52
Batch ID: 20250612_153225
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
 * Sends an email confirmation for an appointment booking.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @param string $appointmentDate The date of the appointment (format: 'Y-m-d H:i').
 * @param string $serviceType The type of service booked.
 * @return bool Returns true if the email is sent successfully, otherwise false.
 */
function sendAppointmentConfirmation($customerEmail, $customerName, $appointmentDate, $serviceType) {
    // Validate input parameters
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email address provided: $customerEmail");
        return false; // Invalid email format
    }

    if (empty($customerName) || empty($appointmentDate) || empty($serviceType)) {
        error_log("Missing required appointment details.");
        return false; // Required fields are missing
    }

    // Format the appointment date
    $formattedDate = date('l, F j, Y \a\t g:i A', strtotime($appointmentDate));
    
    // Email subject
    $subject = "Appointment Confirmation - Reflexology Service";

    // Email body
    $message = "
        Dear $customerName,

        Thank you for booking an appointment with our reflexology service.

        Here are your appointment details:
        - Service Type: $serviceType
        - Appointment Date: $formattedDate

        If you have any questions or need to reschedule, please don't hesitate to contact us.

        We look forward to seeing you!

        Best regards,
        Reflexology Service Team
    ";

    // Email headers
    $headers = "From: no-reply@reflexologyservice.com\r\n";
    $headers .= "Reply-To: support@reflexologyservice.com\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email
    $success = mail($customerEmail, $subject, $message, $headers);

    if (!$success) {
        error_log("Failed to send email to $customerEmail.");
        return false; // Email sending failed
    }

    // Email sent successfully
    return true;
}

// Example usage
$customerEmail = "example@example.com";
$customerName = "John Doe";
$appointmentDate = "2023-11-15 14:00";
$serviceType = "Full-body Reflexology";

if (sendAppointmentConfirmation($customerEmail, $customerName, $appointmentDate, $serviceType)) {
    echo "Email confirmation sent successfully.";
} else {
    echo "Failed to send email confirmation.";
}

?>
```
