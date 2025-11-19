"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osmokro.org
Prompt: Create a PHP code snippet to send an email notification to parents about upcoming events at Основна школа "Мокро", including details from the "Родитељи" section.
Generated: DETERMINISTIC_f60be9b1465e3b8d
Batch ID: 20250612_135754
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
 * Script to send email notifications to parents about upcoming events
 * at Основна школа "Мокро".
 */

// Configuration Settings
$mailHost = 'smtp.example.com';       // SMTP server address
$mailPort = 587;                     // SMTP port
$mailUsername = 'your_email@example.com'; // SMTP username
$mailPassword = 'your_password';     // SMTP password
$mailFrom = 'no-reply@mokro-school.com'; // Sender's email address
$mailFromName = 'Основна школа "Мокро"'; // Sender's name

// Function to send email
function sendEmailNotification($toEmail, $subject, $message) {
    // Validate email address
    if (!filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address: $toEmail");
    }

    // Use PHPMailer for email sending
    require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // SMTP Configuration
        $mail->isSMTP();
        $mail->Host = $GLOBALS['mailHost'];
        $mail->Port = $GLOBALS['mailPort'];
        $mail->SMTPAuth = true;
        $mail->Username = $GLOBALS['mailUsername'];
        $mail->Password = $GLOBALS['mailPassword'];
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;

        // Email Headers
        $mail->setFrom($GLOBALS['mailFrom'], $GLOBALS['mailFromName']);
        $mail->addAddress($toEmail);
        $mail->Subject = $subject;

        // Email Content
        $mail->isHTML(true);
        $mail->Body = $message;

        // Send the email
        if ($mail->send()) {
            return true;
        } else {
            throw new Exception('Mailer Error: ' . $mail->ErrorInfo);
        }
    } catch (Exception $e) {
        error_log('Error sending email: ' . $e->getMessage());
        return false;
    }
}

// Fetch upcoming events and parents' contact information
function getEventDetails() {
    // Example Data: Replace this with a database query
    return [
        'event_title' => 'Родитељски састанак',
        'event_date' => '2023-11-15',
        'event_location' => 'Основна школа "Мокро"',
        'event_description' => 'Састанак са родитељима ученика ради договора о активностима за следећу годину.',
    ];
}

function getParentsContactList() {
    // Example Data: Replace this with a database query
    return [
        ['name' => 'Иван Ивановић', 'email' => 'ivan@example.com'],
        ['name' => 'Милица Петровић', 'email' => 'milica@example.com'],
        ['name' => 'Јован Јовановић', 'email' => 'jovan@example.com'],
    ];
}

// Main Logic: Prepare email content and send notifications
try {
    $eventDetails = getEventDetails();
    $parentsContactList = getParentsContactList();

    $subject = 'Обавештење: ' . $eventDetails['event_title'];
    $message = '<h1>' . htmlspecialchars($eventDetails['event_title']) . '</h1>'
        . '<p><strong>Датум:</strong> ' . htmlspecialchars($eventDetails['event_date']) . '</p>'
        . '<p><strong>Локација:</strong> ' . htmlspecialchars($eventDetails['event_location']) . '</p>'
        . '<p>' . nl2br(htmlspecialchars($eventDetails['event_description'])) . '</p>'
        . '<p>Срдачно,<br>Основна школа "Мокро"</p>';

    foreach ($parentsContactList as $parent) {
        $success = sendEmailNotification($parent['email'], $subject, $message);

        if ($success) {
            echo "Email sent successfully to " . $parent['name'] . " (" . $parent['email'] . ").<br>";
        } else {
            echo "Failed to send email to " . $parent['name'] . " (" . $parent['email'] . ").<br>";
        }
    }
} catch (Exception $e) {
    // Log error details
    error_log('Error: ' . $e->getMessage());
    echo "An error occurred while sending notifications. Please check the logs.";
}
?>
```
