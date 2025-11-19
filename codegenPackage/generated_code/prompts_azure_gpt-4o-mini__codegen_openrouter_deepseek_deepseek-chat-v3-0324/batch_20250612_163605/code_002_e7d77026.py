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
 * Sends email notifications for upcoming half-yearly exam schedule.
 * 
 * @param array $recipients List of recipient email addresses
 * @param string $scheduleDetails Exam schedule details
 * @param string $fromEmail Sender email address
 * @param string $fromName Sender name
 * @return array Associative array with 'success' and 'message' keys
 */
function sendExamNotification(
    array $recipients,
    string $scheduleDetails,
    string $fromEmail = 'exams@ashekaneauliafazil.edu',
    string $fromName = 'Ashekane Aulia Fazil Madrasah'
): array {
    // Validate required parameters
    if (empty($recipients)) {
        return ['success' => false, 'message' => 'No recipients specified'];
    }
    
    if (empty($scheduleDetails)) {
        return ['success' => false, 'message' => 'No schedule details provided'];
    }

    if (!filter_var($fromEmail, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid sender email address'];
    }

    // Set email headers
    $headers = [
        'From' => "$fromName <$fromEmail>",
        'Reply-To' => $fromEmail,
        'MIME-Version' => '1.0',
        'Content-type' => 'text/html; charset=utf-8',
        'X-Mailer' => 'PHP/' . phpversion()
    ];

    // Prepare email subject and body
    $subject = 'Upcoming Half-Yearly Exam Schedule - Ashekane Aulia Fazil Madrasah';
    
    $body = "
        <html>
        <head>
            <title>Exam Schedule Notification</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; }
                .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                .header { background-color: #f8f9fa; padding: 15px; text-align: center; }
                .content { padding: 20px; }
                .footer { margin-top: 20px; font-size: 0.9em; color: #666; }
            </style>
        </head>
        <body>
            <div class='container'>
                <div class='header'>
                    <h2>Half-Yearly Exam Schedule</h2>
                </div>
                <div class='content'>
                    <p>Dear Student/Guardian,</p>
                    <p>Please be informed about the upcoming half-yearly examination schedule:</p>
                    <div>$scheduleDetails</div>
                    <p>Best of luck with your preparations!</p>
                </div>
                <div class='footer'>
                    <p>Ashekane Aulia Fazil Madrasah<br>Exam Committee</p>
                </div>
            </div>
        </body>
        </html>
    ";

    // Process recipients and send emails
    $successCount = 0;
    $failedRecipients = [];
    $headerString = '';
    
    // Convert headers array to string
    foreach ($headers as $key => $value) {
        $headerString .= "$key: $value\r\n";
    }

    // Send email to each recipient
    foreach ($recipients as $recipient) {
        if (!filter_var($recipient, FILTER_VALIDATE_EMAIL)) {
            $failedRecipients[] = $recipient;
            continue;
        }

        if (mail($recipient, $subject, $body, $headerString)) {
            $successCount++;
        } else {
            $failedRecipients[] = $recipient;
        }
    }

    // Prepare result message
    if ($successCount === count($recipients)) {
        return ['success' => true, 'message' => 'All notifications sent successfully'];
    } elseif ($successCount > 0) {
        $message = "Notifications sent to $successCount recipients. Failed for: " . 
                  implode(', ', $failedRecipients);
        return ['success' => true, 'message' => $message];
    } else {
        return ['success' => false, 'message' => 'Failed to send to any recipients: ' . 
                                               implode(', ', $failedRecipients)];
    }
}

// Example usage:
/*
$recipients = [
    'student1@example.com',
    'student2@example.com',
    'parent1@example.com'
];

$scheduleDetails = "
    <ul>
        <li>Date: June 15-20, 2023</li>
        <li>Subjects: Arabic, English, Mathematics, Islamic Studies</li>
        <li>Reporting Time: 8:30 AM</li>
    </ul>
";

$result = sendExamNotification($recipients, $scheduleDetails);
print_r($result);
*/
?>
```
