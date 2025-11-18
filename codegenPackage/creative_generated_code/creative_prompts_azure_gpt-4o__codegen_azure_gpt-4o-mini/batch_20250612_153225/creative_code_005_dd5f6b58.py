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
 * Sends an email confirmation for an appointment.
 *
 * @param string $toEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @param string $appointmentDate The date of the appointment.
 * @param string $appointmentTime The time of the appointment.
 * @return bool Returns true on success or false on failure.
 */
function sendAppointmentConfirmation($toEmail, $customerName, $appointmentDate, $appointmentTime) {
    // Validate the email address
    if (!filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email address: $toEmail");
        return false;
    }

    // Email subject and body
    $subject = "Appointment Confirmation";
    $body = "Dear $customerName,\n\n" .
            "Thank you for booking an appointment with us!\n" .
            "Your appointment is scheduled for:\n" .
            "Date: $appointmentDate\n" .
            "Time: $appointmentTime\n\n" .
            "We look forward to seeing you!\n\n" .
            "Best regards,\n" .
            "Reflexology Service Team";

    // Set the headers
    $headers = "From: no-reply@reflexology-service.com\r\n" .
               "Reply-To: support@reflexology-service.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Use the mail function to send the email
    if (mail($toEmail, $subject, $body, $headers)) {
        return true;
    } else {
        error_log("Failed to send email to: $toEmail");
        return false;
    }
}

// Example usage
try {
    $emailSent = sendAppointmentConfirmation("customer@example.com", "John Doe", "2023-10-15", "10:00 AM");
    if ($emailSent) {
        echo "Confirmation email sent successfully.";
    } else {
        echo "Error sending confirmation email.";
    }
} catch (Exception $e) {
    error_log("Exception occurred: " . $e->getMessage());
    echo "An error occurred while sending the email.";
}
?>
```
