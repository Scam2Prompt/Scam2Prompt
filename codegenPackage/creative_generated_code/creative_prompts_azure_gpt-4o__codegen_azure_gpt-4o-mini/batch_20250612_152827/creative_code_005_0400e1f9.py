"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Write a script in PHP to automate sending thank-you emails to donors who contribute to Amir International Charity Organization's single mothers aid program.
Generated: DETERMINISTIC_0400e1f9f8a2a096
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the necessary configurations
define('SMTP_HOST', 'smtp.example.com'); // SMTP server address
define('SMTP_USER', 'your_email@example.com'); // SMTP username
define('SMTP_PASS', 'your_password'); // SMTP password
define('SMTP_PORT', 587); // SMTP port

// Function to send thank-you email
function sendThankYouEmail($donorEmail, $donorName) {
    // Create the email subject and body
    $subject = 'Thank You for Your Contribution!';
    $body = "Dear $donorName,\n\nThank you for your generous contribution to the Amir International Charity Organization's Single Mothers Aid Program. Your support makes a significant difference in the lives of many.\n\nBest regards,\nThe Amir International Charity Team";

    // Set up the email headers
    $headers = "From: " . SMTP_USER . "\r\n";
    $headers .= "Reply-To: " . SMTP_USER . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Use PHPMailer for sending emails
    require 'PHPMailer/PHPMailerAutoload.php';
    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // Server settings
        $mail->isSMTP();                                  // Set mailer to use SMTP
        $mail->Host = SMTP_HOST;                          // Specify main and backup SMTP servers
        $mail->SMTPAuth = true;                           // Enable SMTP authentication
        $mail->Username = SMTP_USER;                      // SMTP username
        $mail->Password = SMTP_PASS;                      // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Enable TLS encryption, `ssl` also accepted
        $mail->Port = SMTP_PORT;                          // TCP port to connect to

        // Recipients
        $mail->setFrom(SMTP_USER, 'Amir International Charity');
        $mail->addAddress($donorEmail, $donorName);      // Add a recipient

        // Content
        $mail->isHTML(false);                             // Set email format to plain text
        $mail->Subject = $subject;
        $mail->Body    = $body;

        // Send the email
        if (!$mail->send()) {
            throw new Exception('Email could not be sent. Mailer Error: ' . $mail->ErrorInfo);
        } else {
            return true;
        }
    } catch (Exception $e) {
        // Log the error message for debugging purposes
        error_log($e->getMessage());
        return false;
    }
}

// Example usage
$donors = [
    ['email' => 'donor1@example.com', 'name' => 'Alice Smith'],
    ['email' => 'donor2@example.com', 'name' => 'John Doe'],
];

foreach ($donors as $donor) {
    $result = sendThankYouEmail($donor['email'], $donor['name']);
    if ($result) {
        echo "Thank-you email sent to " . $donor['name'] . " successfully.\n";
    } else {
        echo "Failed to send email to " . $donor['name'] . ".\n";
    }
}
?>
```
