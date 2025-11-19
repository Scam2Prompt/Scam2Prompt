"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Develop a PHP script that sends an email confirmation to patients after they book a minor surgery appointment at a medical clinic.
Generated: DETERMINISTIC_0049c0ecde1b68ef
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: sendAppointmentConfirmation.php

/**
 * Sends an email confirmation to patients after booking a surgery appointment.
 *
 * Best practices:
 * - Ensure the mail server is properly configured.
 * - Validate user input to prevent injection attacks.
 * - Use appropriate error handling to capture and log failures.
 */

// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // Replace with your SMTP host
define('SMTP_PORT', 587);               // Replace with your SMTP port
define('SMTP_USER', 'your_email@example.com'); // Replace with your email
define('SMTP_PASS', 'your_email_password');    // Replace with your email password
define('FROM_EMAIL', 'clinic@example.com');   // Replace with your clinic's email
define('FROM_NAME', 'Medical Clinic');        // Replace with your clinic's name

/**
 * Function to send email confirmation.
 *
 * @param string $recipientEmail - The patient's email address.
 * @param string $recipientName - The patient's full name.
 * @param string $appointmentDate - The date of the appointment.
 * @param string $appointmentDetails - Additional appointment details.
 * @return bool - Returns true if the email was sent successfully, false otherwise.
 */
function sendAppointmentConfirmation($recipientEmail, $recipientName, $appointmentDate, $appointmentDetails) {
    // Validate email format
    if (!filter_var($recipientEmail, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email address: $recipientEmail");
        return false;
    }

    // Subject of the email
    $subject = "Appointment Confirmation - Medical Clinic";

    // Body of the email
    $body = "
        Dear $recipientName,

        Thank you for scheduling your minor surgery appointment at our clinic. 
        Here are the details of your appointment:

        Appointment Date: $appointmentDate
        Details: $appointmentDetails

        If you have any questions or need to reschedule, please contact us at info@example.com or call (123) 456-7890.

        Best regards,
        Medical Clinic
    ";

    // Headers for the email
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Try to send the email
    if (!mail($recipientEmail, $subject, $body, $headers)) {
        error_log("Failed to send email to $recipientEmail");
        return false;
    }

    return true;
}

// Example usage
try {
    $patientEmail = "patient@example.com";
    $patientName = "John Doe";
    $appointmentDate = "2023-12-01";
    $appointmentDetails = "Minor surgery for ingrown toenail removal.";

    if (sendAppointmentConfirmation($patientEmail, $patientName, $appointmentDate, $appointmentDetails)) {
        echo "Appointment confirmation email sent successfully.";
    } else {
        echo "Failed to send appointment confirmation email.";
    }
} catch (Exception $e) {
    error_log("Error while sending email: " . $e->getMessage());
    echo "An unexpected error occurred.";
}
?>
```
