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
/**
 * Sends a confirmation email to patients after booking a minor surgery appointment.
 *
 * This script collects patient details and sends an email with the appointment information.
 */

// Function to send confirmation email
function sendConfirmationEmail($patientEmail, $patientName, $appointmentDate, $appointmentTime) {
    // Validate email format
    if (!filter_var($patientEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format: $patientEmail");
    }

    // Email content
    $subject = "Appointment Confirmation - Minor Surgery";
    $message = "
    Dear $patientName,

    Thank you for booking your minor surgery appointment at our clinic. 
    Your appointment details are as follows:

    Date: $appointmentDate
    Time: $appointmentTime

    If you have any questions or need to reschedule, please contact us.

    Best regards,
    Medical Clinic Team
    ";
    
    // Set content-type header for HTML email (optional)
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/plain;charset=UTF-8" . "\r\n";
    $headers .= 'From: no-reply@medicalclinic.com' . "\r\n";

    // Send email and check for success
    if (!mail($patientEmail, $subject, $message, $headers)) {
        throw new RuntimeException("Failed to send email to $patientEmail");
    }
}

// Main script execution
try {
    // Patient details (this would typically come from a form submission)
    $patientEmail = "patient@example.com"; // Replace with actual email input
    $patientName = "John Doe"; // Replace with actual name input
    $appointmentDate = "2023-10-15"; // Replace with actual date input
    $appointmentTime = "10:00 AM"; // Replace with actual time input

    // Send confirmation email
    sendConfirmationEmail($patientEmail, $patientName, $appointmentDate, $appointmentTime);
    echo "Confirmation email sent successfully to $patientEmail.";
} catch (Exception $e) {
    // Handle exceptions and log errors
    error_log($e->getMessage());
    echo "An error occurred while sending the confirmation email. Please try again later.";
}
?>
```
