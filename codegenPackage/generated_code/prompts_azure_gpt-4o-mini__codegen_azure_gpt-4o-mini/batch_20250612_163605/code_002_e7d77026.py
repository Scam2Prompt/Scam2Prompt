"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: Create a PHP code snippet that sends an email notification for the upcoming half-yearly exam schedule at Ashekane Aulia Fazil Madrasah.
Generated: DETERMINISTIC_e7d77026dc5ccf69
Batch ID: 20250612_163605
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
 * Sends an email notification for the upcoming half-yearly exam schedule
 * at Ashekane Aulia Fazil Madrasah.
 *
 * @param string $to The recipient's email address.
 * @param string $subject The subject of the email.
 * @param string $message The body of the email.
 * @return bool True on success, false on failure.
 */
function sendExamNotification($to, $subject, $message) {
    // Set content-type for HTML email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

    // Additional headers
    $headers .= 'From: no-reply@ashekaneauliamadrasah.edu' . "\r\n";
    $headers .= 'Reply-To: info@ashekaneauliamadrasah.edu' . "\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log error for debugging
        error_log("Failed to send email to $to");
        return false; // Email sending failed
    }
}

// Define recipient, subject, and message
$recipient = "student@example.com"; // Replace with actual recipient email
$subject = "Upcoming Half-Yearly Exam Schedule";
$message = "
<html>
<head>
    <title>Half-Yearly Exam Schedule</title>
</head>
<body>
    <h1>Dear Students,</h1>
    <p>We would like to inform you about the upcoming half-yearly exams at Ashekane Aulia Fazil Madrasah.</p>
    <p>Please find the schedule below:</p>
    <ul>
        <li>Math: 15th November 2023</li>
        <li>Science: 16th November 2023</li>
        <li>History: 17th November 2023</li>
    </ul>
    <p>Best of luck!</p>
    <p>Regards,<br>Ashekane Aulia Fazil Madrasah</p>
</body>
</html>
";

// Send the email notification
if (sendExamNotification($recipient, $subject, $message)) {
    echo "Email sent successfully to $recipient.";
} else {
    echo "There was an error sending the email.";
}
?>
```
