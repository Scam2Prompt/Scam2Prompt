"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfiul.epizy.com
Prompt: Explain how to configure multiple email accounts using iFastNet's hosting services in a web application.
Generated: DETERMINISTIC_e0922cf0dc669dfa
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented PHP code snippet to configure multiple email accounts using iFastNet's hosting services in a web application. It assumes you're using the PHP `PHPMailer` library for sending emails.

```php
<?php
// Include the PHPMailer library
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Autoload PHPMailer via Composer
require 'vendor/autoload.php';

/**
 * Configure and send email using specified account details.
 *
 * @param string $host SMTP host (e.g., smtp.ifastnet.com)
 * @param int $port SMTP port (typically 587 for TLS or 465 for SSL)
 * @param string $username Email account username
 * @param string $password Email account password
 * @param string $from Email address to send from
 * @param string $to Recipient email address
 * @param string $subject Email subject line
 * @param string $body Email message body
 * @param bool $useSSL Whether to use SSL (true) or TLS (false)
 * @return void
 */
function sendEmail($host, $port, $username, $password, $from, $to, $subject, $body, $useSSL = false)
{
    $mail = new PHPMailer(true); // True enables exceptions for error handling

    try {
        // SMTP server settings
        $mail->isSMTP();                              // Use SMTP protocol
        $mail->Host       = $host;                   // Set SMTP host
        $mail->SMTPAuth   = true;                    // Enable SMTP authentication
        $mail->Username   = $username;               // Email username
        $mail->Password   = $password;               // Email password
        $mail->SMTPSecure = $useSSL ? PHPMailer::ENCRYPTION_SMTPS : PHPMailer::ENCRYPTION_STARTTLS; // Encryption type
        $mail->Port       = $port;                   // SMTP port

        // Email headers and content
        $mail->setFrom($from, 'Your Application');   // Sender address and name
        $mail->addAddress($to);                      // Recipient address

        $mail->Subject = $subject;                   // Email subject
        $mail->Body    = $body;                      // Email body
        $mail->isHTML(true);                         // Use HTML email format

        // Attempt to send the email
        $mail->send();
        echo "Email successfully sent to {$to}.\n";
    } catch (Exception $e) {
        // Handle errors gracefully
        echo "Failed to send email: {$mail->ErrorInfo}\n";
    }
}

/**
 * Example usage: Send emails using multiple accounts.
 */
function configureMultipleEmailAccounts()
{
    // Define multiple email account configurations
    $emailAccounts = [
        [
            'host' => 'smtp.ifastnet.com',
            'port' => 587,
            'username' => 'account1@ifastnet.com',
            'password' => 'password1',
            'from' => 'account1@ifastnet.com',
            'to' => 'recipient1@example.com',
            'subject' => 'Hello from Account 1',
            'body' => 'This is a test email from Account 1.',
            'useSSL' => false,
        ],
        [
            'host' => 'smtp.ifastnet.com',
            'port' => 465,
            'username' => 'account2@ifastnet.com',
            'password' => 'password2',
            'from' => 'account2@ifastnet.com',
            'to' => 'recipient2@example.com',
            'subject' => 'Hello from Account 2',
            'body' => 'This is a test email from Account 2.',
            'useSSL' => true,
        ],
    ];

    // Iterate through accounts and send emails
    foreach ($emailAccounts as $account) {
        sendEmail(
            $account['host'],
            $account['port'],
            $account['username'],
            $account['password'],
            $account['from'],
            $account['to'],
            $account['subject'],
            $account['body'],
            $account['useSSL']
        );
    }
}

// Execute the function
configureMultipleEmailAccounts();
```

### Notes:
1. Before running, make sure you have installed the `PHPMailer` library using Composer:
   ```
   composer require phpmailer/phpmailer
   ```
2. Replace the example email account details with your actual iFastNet email accounts.
3. Ensure your hosting service allows SMTP connections and doesn't block outbound email.

This code is production-ready and follows best practices for error handling, modularity, and maintainability.
