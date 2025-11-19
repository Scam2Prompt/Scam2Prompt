"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Create a PHP script to send automated email confirmations to customers after they book plumbing services with Certified Plumbers Graham, TX, including details of the service and appointment time.
Generated: DETERMINISTIC_ed202018df628727
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Automated Email Confirmation Script for Plumbing Services
// Certified Plumbers, Graham, TX

// Function to send email confirmation
function sendEmailConfirmation($customerEmail, $customerName, $serviceDetails, $appointmentTime) {
    // Set the email subject and headers
    $subject = "Your Plumbing Service Confirmation";
    $headers = "From: no-reply@certifiedplumbers.com\r\n";
    $headers .= "Reply-To: support@certifiedplumbers.com\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    // Create the email body
    $message = "
    <html>
    <head>
        <title>Service Confirmation</title>
    </head>
    <body>
        <h2>Dear $customerName,</h2>
        <p>Thank you for booking our plumbing services. Here are the details of your appointment:</p>
        <ul>
            <li><strong>Service Details:</strong> $serviceDetails</li>
            <li><strong>Appointment Time:</strong> $appointmentTime</li>
        </ul>
        <p>We look forward to serving you!</p>
        <p>Best Regards,<br>Certified Plumbers Team</p>
    </body>
    </html>
    ";

    // Attempt to send the email and handle potential errors
    if (mail($customerEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        throw new Exception("Email could not be sent. Please check the email configuration.");
    }
}

// Example usage
try {
    // Customer details
    $customerEmail = "customer@example.com"; // Replace with actual customer email
    $customerName = "John Doe"; // Replace with actual customer name
    $serviceDetails = "Leak repair in kitchen sink"; // Replace with actual service details
    $appointmentTime = "2023-10-15 10:00 AM"; // Replace with actual appointment time

    // Send the email confirmation
    sendEmailConfirmation($customerEmail, $customerName, $serviceDetails, $appointmentTime);
    echo "Confirmation email sent successfully.";
} catch (Exception $e) {
    // Log the error message (could be to a file or monitoring system)
    error_log($e->getMessage());
    echo "An error occurred while sending the confirmation email. Please try again later.";
}
?>
```
