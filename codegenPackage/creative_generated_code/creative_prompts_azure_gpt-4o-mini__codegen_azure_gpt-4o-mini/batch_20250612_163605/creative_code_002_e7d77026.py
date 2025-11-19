"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aamctg.edu.bd
Prompt: Create a PHP code snippet that sends an email notification for the upcoming half-yearly exam schedule at Ashekane Aulia Fazil Madrasah.
Generated: DETERMINISTIC_e7d77026dc5ccf69
Batch ID: 20250612_163605
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
 * Sends an email notification for the upcoming half-yearly exam schedule.
 *
 * @param string $recipientEmail The email address of the recipient.
 * @param string $studentName The name of the student receiving the notification.
 * @param string $examDate The date of the upcoming exam.
 * @return bool Returns true on success, false on failure.
 */
function sendExamNotification($recipientEmail, $studentName, $examDate) {
    // Set the subject and message for the email
    $subject = "Upcoming Half-Yearly Exam Schedule";
    $message = "Dear $studentName,\n\n"
             . "This is a reminder that your half-yearly exams are scheduled for $examDate.\n"
             . "Please prepare accordingly.\n\n"
             . "Best regards,\n"
             . "Ashekane Aulia Fazil Madrasah";

    // Set the headers for the email
    $headers = "From: no-reply@ashekaneauliafazilmadrash.com\r\n" .
               "Reply-To: no-reply@ashekaneauliafazilmadrash.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Attempt to send the email
    if (mail($recipientEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log error for debugging purposes
        error_log("Failed to send email to $recipientEmail.");
        return false; // Email sending failed
    }
}

// Example usage
$recipientEmail = "student@example.com";
$studentName = "John Doe";
$examDate = "March 15, 2024";

if (sendExamNotification($recipientEmail, $studentName, $examDate)) {
    echo "Email notification sent successfully.";
} else {
    echo "There was an issue sending the email notification.";
}
?>
```
