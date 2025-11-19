"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rotary-bastogne.be
Prompt: Create a PHP code snippet that sends an email notification about the "Concert de Nouvel An 2025" event listed on the Rotary Bastogne site.
Generated: DETERMINISTIC_9bc7bcd0662a4790
Batch ID: 20250612_140024
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
 * Sends an email notification for the "Concert de Nouvel An 2025" event.
 *
 * @param string $toEmail Recipient's email address.
 * @param string $eventName Name of the event.
 * @param string $eventDate Date of the event.
 * @param string $eventLocation Location of the event.
 * @return bool Returns true on success, false on failure.
 */
function sendEventNotification($toEmail, $eventName, $eventDate, $eventLocation) {
    // Set the email subject
    $subject = "Notification: $eventName";

    // Construct the email body
    $message = "
    <html>
    <head>
        <title>$eventName</title>
    </head>
    <body>
        <h1>$eventName</h1>
        <p>We are excited to inform you about the upcoming event:</p>
        <p><strong>Date:</strong> $eventDate</p>
        <p><strong>Location:</strong> $eventLocation</p>
        <p>We hope to see you there!</p>
        <p>Best regards,<br>Rotary Bastogne Team</p>
    </body>
    </html>
    ";

    // Set content-type for HTML email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

    // Additional headers
    $headers .= "From: noreply@rotarybastogne.com" . "\r\n";

    // Attempt to send the email
    if (mail($toEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log the error for debugging (consider using a logger in production)
        error_log("Failed to send email to $toEmail for event: $eventName");
        return false; // Email sending failed
    }
}

// Example usage
$recipientEmail = "user@example.com"; // Replace with the actual recipient's email
$eventName = "Concert de Nouvel An 2025";
$eventDate = "January 1, 2025";
$eventLocation = "Bastogne, Belgium";

// Send the notification
if (sendEventNotification($recipientEmail, $eventName, $eventDate, $eventLocation)) {
    echo "Email sent successfully.";
} else {
    echo "Failed to send email.";
}
?>
```
