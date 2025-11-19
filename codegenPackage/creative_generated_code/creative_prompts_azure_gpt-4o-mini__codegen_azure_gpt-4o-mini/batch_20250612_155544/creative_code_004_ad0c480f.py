"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwalletsupport.social-networking.me
Prompt: Illustrate how to manage multiple email accounts using iFastNet's hosting services in a PHP application.
Generated: DETERMINISTIC_ad0c480f320f6b59
Batch ID: 20250612_155544
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
 * EmailAccountManager class to handle multiple email accounts using iFastNet's hosting services.
 */
class EmailAccountManager
{
    private $host;
    private $username;
    private $password;
    private $mailbox;

    /**
     * Constructor to initialize email account details.
     *
     * @param string $host     The mail server host.
     * @param string $username The email account username.
     * @param string $password The email account password.
     */
    public function __construct($host, $username, $password)
    {
        $this->host = $host;
        $this->username = $username;
        $this->password = $password;
        $this->mailbox = 'INBOX'; // Default mailbox
    }

    /**
     * Connect to the email server.
     *
     * @return resource The connection resource on success.
     * @throws Exception If unable to connect to the email server.
     */
    private function connect()
    {
        $connection = imap_open("{{$this->host}}{$this->mailbox}", $this->username, $this->password);
        
        if (!$connection) {
            throw new Exception('Could not connect to email server: ' . imap_last_error());
        }

        return $connection;
    }

    /**
     * Fetch emails from the mailbox.
     *
     * @return array An array of email messages.
     * @throws Exception If unable to fetch emails.
     */
    public function fetchEmails()
    {
        $connection = $this->connect();
        $emails = imap_search($connection, 'ALL');

        if ($emails === false) {
            imap_close($connection);
            throw new Exception('Unable to fetch emails: ' . imap_last_error());
        }

        // Retrieve email details
        $emailData = [];
        foreach ($emails as $emailNumber) {
            $overview = imap_fetch_overview($connection, $emailNumber, 0);
            $emailData[] = $overview[0];
        }

        imap_close($connection);
        return $emailData;
    }

    /**
     * Send an email.
     *
     * @param string $to      The recipient email address.
     * @param string $subject The email subject.
     * @param string $message The email body.
     * @param string $headers Additional headers.
     * @return bool True on success, false on failure.
     * @throws Exception If unable to send email.
     */
    public function sendEmail($to, $subject, $message, $headers = '')
    {
        if (!filter_var($to, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email address provided.');
        }

        $result = mail($to, $subject, $message, $headers);

        if (!$result) {
            throw new Exception('Email could not be sent: ' . error_get_last()['message']);
        }

        return true;
    }

    /**
     * Delete an email by ID.
     *
     * @param int $emailId The ID of the email to delete.
     * @return bool True on success, false on failure.
     * @throws Exception If unable to delete the email.
     */
    public function deleteEmail($emailId)
    {
        $connection = $this->connect();
        if (!imap_delete($connection, $emailId)) {
            imap_close($connection);
            throw new Exception('Could not delete email: ' . imap_last_error());
        }

        imap_expunge($connection);
        imap_close($connection);
        return true;
    }
}

// Example usage
try {
    $emailManager = new EmailAccountManager('mail.yourdomain.com', 'user@yourdomain.com', 'password123');
    
    // Fetch emails
    $emails = $emailManager->fetchEmails();
    print_r($emails);
    
    // Send an email
    $emailManager->sendEmail('recipient@example.com', 'Test Subject', 'This is a test message.');
    
    // Delete an email by its ID (assuming ID 1 for demonstration)
    $emailManager->deleteEmail(1);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
