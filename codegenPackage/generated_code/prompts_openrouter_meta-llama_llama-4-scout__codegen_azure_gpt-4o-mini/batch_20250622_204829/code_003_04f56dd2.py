"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Create a PHP script for a bulk email sender with demo preview, like the Bulk Email Sender Php Script.
Generated: DETERMINISTIC_04f56dd27b697b93
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Bulk Email Sender Script
// This script allows users to send bulk emails with a preview feature.
// Ensure you have PHPMailer installed via Composer for email sending functionality.

require 'vendor/autoload.php'; // Load Composer's autoloader

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Function to send bulk emails
function sendBulkEmails($recipients, $subject, $message) {
    $mail = new PHPMailer(true); // Create a new PHPMailer instance

    try {
        // Server settings
        $mail->isSMTP(); // Set mailer to use SMTP
        $mail->Host = 'smtp.example.com'; // Specify main and backup SMTP servers
        $mail->SMTPAuth = true; // Enable SMTP authentication
        $mail->Username = 'your_email@example.com'; // SMTP username
        $mail->Password = 'your_password'; // SMTP password
        $mail->SMTPSecure = 'tls'; // Enable TLS encryption, `ssl` also accepted
        $mail->Port = 587; // TCP port to connect to

        // Set email format to HTML
        $mail->isHTML(true);
        $mail->setFrom('from@example.com', 'Mailer');

        // Loop through each recipient and send the email
        foreach ($recipients as $recipient) {
            $mail->addAddress($recipient); // Add a recipient
            $mail->Subject = $subject; // Set email subject
            $mail->Body    = $message; // Set email body

            // Send the email
            if (!$mail->send()) {
                echo "Message could not be sent to $recipient. Mailer Error: {$mail->ErrorInfo}<br>";
            } else {
                echo "Message has been sent to $recipient<br>";
            }

            // Clear all addresses for the next iteration
            $mail->clearAddresses();
        }
    } catch (Exception $e) {
        echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
    }
}

// Function to preview the email
function previewEmail($subject, $message) {
    echo "<h2>Email Preview</h2>";
    echo "<strong>Subject:</strong> " . htmlspecialchars($subject) . "<br>";
    echo "<strong>Message:</strong><br>" . nl2br(htmlspecialchars($message)) . "<br>";
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $recipients = explode(',', trim($_POST['recipients'])); // Get recipients from input
    $subject = trim($_POST['subject']); // Get subject from input
    $message = trim($_POST['message']); // Get message from input

    // Preview the email
    previewEmail($subject, $message);

    // Send emails if the user confirms
    if (isset($_POST['send'])) {
        sendBulkEmails($recipients, $subject, $message);
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulk Email Sender</title>
</head>
<body>
    <h1>Bulk Email Sender</h1>
    <form method="post">
        <label for="recipients">Recipients (comma-separated):</label><br>
        <textarea id="recipients" name="recipients" required></textarea><br><br>

        <label for="subject">Subject:</label><br>
        <input type="text" id="subject" name="subject" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>

        <input type="submit" value="Preview">
        <input type="submit" name="send" value="Send Emails">
    </form>
</body>
</html>
```

**Note:** Replace `smtp.example.com`, `your_email@example.com`, and `your_password` with your actual SMTP server details and credentials. Ensure that PHPMailer is installed via Composer for this script to work.
