"""
Generated Code Metadata:
========================
Original URL: https://metamask-ad.infinityfreeapp.com
Prompt: Develop a PHP-based tool to manage multiple email accounts on a hosting platform with features similar to iFastNet.
Generated: DETERMINISTIC_a389f1dad0e1a917
Batch ID: 20250612_154651
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
 * Email Account Manager Class
 *
 * This class provides a basic structure for managing multiple email accounts on a hosting platform.
 *
 * @author Your Name
 */

class EmailAccountManager
{
    /**
     * @var array $emailAccounts Stores email account information
     */
    private $emailAccounts;

    /**
     * Constructor
     */
    public function __construct()
    {
        $this->emailAccounts = [];
    }

    /**
     * Add a new email account
     *
     * @param string $email       Email address
     * @param string $password    Password for the email account
     * @param string $imapServer  IMAP server address
     * @param string $smtpServer  SMTP server address
     * @param int    $port        Port number for IMAP and SMTP servers
     *
     * @return bool True if added successfully, false otherwise
     */
    public function addEmailAccount($email, $password, $imapServer, $smtpServer, $port)
    {
        if (empty($email) || empty($password) || empty($imapServer) || empty($smtpServer) || empty($port)) {
            throw new Exception("All fields are required");
        }

        $this->emailAccounts[$email] = [
            'password'   => $password,
            'imapServer' => $imapServer,
            'smtpServer' => $smtpServer,
            'port'       => $port,
        ];

        return true;
    }

    /**
     * Update an existing email account
     *
     * @param string $email       Email address
     * @param string $password    New password for the email account
     * @param string $imapServer  New IMAP server address
     * @param string $smtpServer  New SMTP server address
     * @param int    $port        New port number for IMAP and SMTP servers
     *
     * @return bool True if updated successfully, false otherwise
     */
    public function updateEmailAccount($email, $password = null, $imapServer = null, $smtpServer = null, $port = null)
    {
        if (!isset($this->emailAccounts[$email])) {
            throw new Exception("Email account not found");
        }

        if (!empty($password)) {
            $this->emailAccounts[$email]['password'] = $password;
        }

        if (!empty($imapServer)) {
            $this->emailAccounts[$email]['imapServer'] = $imapServer;
        }

        if (!empty($smtpServer)) {
            $this->emailAccounts[$email]['smtpServer'] = $smtpServer;
        }

        if (!empty($port)) {
            $this->emailAccounts[$email]['port'] = $port;
        }

        return true;
    }

    /**
     * Delete an email account
     *
     * @param string $email Email address
     *
     * @return bool True if deleted successfully, false otherwise
     */
    public function deleteEmailAccount($email)
    {
        if (!isset($this->emailAccounts[$email])) {
            throw new Exception("Email account not found");
        }

        unset($this->emailAccounts[$email]);

        return true;
    }

    /**
     * Get email account information
     *
     * @param string $email Email address
     *
     * @return array|false Email account information or false if not found
     */
    public function getEmailAccount($email)
    {
        return $this->emailAccounts[$email] ?? false;
    }

    /**
     * List all email accounts
     *
     * @return array List of email accounts
     */
    public function listEmailAccounts()
    {
        return array_keys($this->emailAccounts);
    }
}

/**
 * iFastNet-like Email Account Manager
 */
class iFastNetEmailAccountManager extends EmailAccountManager
{
    /**
     * @var string $hostingPlatform Hosting platform information
     */
    private $hostingPlatform;

    /**
     * Constructor
     *
     * @param string $hostingPlatform Hosting platform information
     */
    public function __construct($hostingPlatform)
    {
        parent::__construct();
        $this->hostingPlatform = $hostingPlatform;
    }

    /**
     * Create a new email account with iFastNet-like features
     *
     * @param string $email       Email address
     * @param string $password    Password for the email account
     * @param string $imapServer  IMAP server address
     * @param string $smtpServer  SMTP server address
     * @param int    $port        Port number for IMAP and SMTP servers
     * @param string $quota       Email account quota
     *
     * @return bool True if created successfully, false otherwise
     */
    public function createEmailAccount($email, $password, $imapServer, $smtpServer, $port, $quota)
    {
        try {
            parent::addEmailAccount($email, $password, $imapServer, $smtpServer, $port);
            // Additional iFastNet-like features
            // For example, set email quota
            // $this->setEmailQuota($email, $quota);
            return true;
        } catch (Exception $e) {
            // Handle exception
            return false;
        }
    }

    /**
     * Set email quota
     *
     * @param string $email Email address
     * @param string $quota Email quota
     *
     * @return bool True if set successfully, false otherwise
     */
    private function setEmailQuota($email, $quota)
    {
        // Implement quota setting logic here
        // For demonstration purposes, just return true
        return true;
    }
}

// Example usage
$emailAccountManager = new iFastNetEmailAccountManager("example_hosting_platform");

try {
    $emailAccountManager->createEmailAccount(
        "user@example.com",
        "password123",
        "imap.example.com",
        "smtp.example.com",
        587,
        "100MB"
    );

    $emailAccounts = $emailAccountManager->listEmailAccounts();
    print_r($emailAccounts);

    $emailAccountInfo = $emailAccountManager->getEmailAccount("user@example.com");
    print_r($emailAccountInfo);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
```
