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
// Configuration settings for email
$senderEmail = "noreply@auliafazilmadrasah.com"; // Sender's email address
$senderName = "Ashekane Aulia Fazil Madrasah";   // Sender's name
$recipientEmail = "student@example.com";        // Recipient's email address
$subject = "Upcoming Half-Yearly Exam Schedule"; // Email subject

// Exam schedule details
$examDate = "YYYY-MM-DD"; // Replace with the actual date
$examTime = "10:00 AM";   // Replace with the actual time
$examVenue = "Madrasah Main Hall"; // Replace with the actual venue

// Compose the email message
$message = "
Dear Student,

We hope this message finds you well. This is a reminder about the upcoming Half-Yearly Exam at Ashekane Aulia Fazil Madrasah. 
Please find the details below:

Date: $examDate
Time: $examTime
Venue: $examVenue

Please ensure you arrive on time and bring all necessary items.

Best regards,
$senderName
";

// Email headers
$headers = "From: $senderName <$senderEmail>\r\n";
$headers .= "Reply-To: $senderEmail\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

try {
    // Send the email using PHP's mail() function
    if (mail($recipientEmail, $subject, $message, $headers)) {
        echo "Email sent successfully.";
    } else {
        throw new Exception("Failed to send the email.");
    }
} catch (Exception $e) {
    // Handle any errors that occur during email sending
    error_log($e->getMessage(), 0); // Log the error message
    echo "An error occurred while sending the email notification. Please try again later.";
}
?>
```
