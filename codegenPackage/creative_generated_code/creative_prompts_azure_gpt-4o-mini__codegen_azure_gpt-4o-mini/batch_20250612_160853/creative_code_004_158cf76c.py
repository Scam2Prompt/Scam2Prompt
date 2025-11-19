"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Construct a PHP script that sends confirmation emails to participants who register for the "Patente d'impresa" course, including event details and a thank you message.
Generated: DETERMINISTIC_158cf76c1653b171
Batch ID: 20250612_160853
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
 * Sends a confirmation email to participants who register for the "Patente d'impresa" course.
 * 
 * @param string $toEmail The recipient's email address.
 * @param string $participantName The name of the participant.
 * @param string $courseDetails Details about the course.
 * @param string $eventDate The date of the event.
 * @return bool True on success, false on failure.
 */
function sendConfirmationEmail($toEmail, $participantName, $courseDetails, $eventDate) {
    // Set the subject of the email
    $subject = "Confirmation of Your Registration for 'Patente d'impresa' Course";

    // Create the email body
    $body = "Dear $participantName,\n\n";
    $body .= "Thank you for registering for the 'Patente d'impresa' course. Here are the details of the event:\n\n";
    $body .= "Course Details: $courseDetails\n";
    $body .= "Event Date: $eventDate\n\n";
    $body .= "We look forward to seeing you there!\n\n";
    $body .= "Best Regards,\n";
    $body .= "The Course Team";

    // Set the headers
    $headers = "From: no-reply@courseprovider.com\r\n";
    $headers .= "Reply-To: support@courseprovider.com\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email and handle potential errors
    if (mail($toEmail, $subject, $body, $headers)) {
        return true; // Email sent successfully
    } else {
        error_log("Failed to send email to $toEmail"); // Log the error
        return false; // Email sending failed
    }
}

// Example usage
$participantEmail = 'participant@example.com';
$participantName = 'John Doe';
$courseDetails = 'Learn the essentials of business patenting and entrepreneurship.';
$eventDate = 'March 15, 2024';

if (sendConfirmationEmail($participantEmail, $participantName, $courseDetails, $eventDate)) {
    echo "Confirmation email sent to $participantEmail.";
} else {
    echo "There was a problem sending the confirmation email.";
}
?>
```
