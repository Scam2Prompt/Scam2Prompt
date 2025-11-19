"""
Generated Code Metadata:
========================
Original URL: https://dappsfixerweb.42web.io
Prompt: Write a code snippet in PHP to configure multiple email accounts on a web hosting service like iFastNet Web Hosting, which offers unlimited disk space and bandwidth.
Generated: DETERMINISTIC_0bf73d35579ac4e7
Batch ID: 20250622_205358
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
 * Email Account Configuration Class
 *
 * This class provides a simple way to configure multiple email accounts on a web hosting service.
 *
 * @author Your Name
 */

class EmailAccountConfigurator
{
    /**
     * @var string The hostname of the email server
     */
    private $hostname;

    /**
     * @var string The username for authentication
     */
    private $username;

    /**
     * @var string The password for authentication
     */
    private $password;

    /**
     * @var array A list of email accounts to configure
     */
    private $emailAccounts;

    /**
     * Constructor
     *
     * @param string $hostname The hostname of the email server
     * @param string $username The username for authentication
     * @param string $password The password for authentication
     */
    public function __construct($hostname, $username, $password)
    {
        $this->hostname = $hostname;
        $this->username = $username;
        $this->password = $password;
        $this->emailAccounts = [];
    }

    /**
     * Add an email account to configure
     *
     * @param string $email The email address to configure
     * @param string $password The password for the email account
     * @param string $quota The quota for the email account (optional)
     */
    public function addEmailAccount($email, $password, $quota = null)
    {
        $this->emailAccounts[] = [
            'email' => $email,
            'password' => $password,
            'quota' => $quota,
        ];
    }

    /**
     * Configure the email accounts using the IMAP library
     */
    public function configureEmailAccounts()
    {
        // Connect to the IMAP server
        $imap = imap_open($this->hostname, $this->username, $this->password);

        if (!$imap) {
            throw new Exception('Failed to connect to IMAP server: ' . imap_last_error());
        }

        // Create and configure each email account
        foreach ($this->emailAccounts as $account) {
            try {
                // Create the email account
                $this->createEmailAccount($imap, $account['email'], $account['password'], $account['quota']);

                echo "Email account {$account['email']} created successfully.\n";
            } catch (Exception $e) {
                echo "Error creating email account {$account['email']}: " . $e->getMessage() . "\n";
            }
        }

        // Close the IMAP connection
        imap_close($imap);
    }

    /**
     * Create an email account using the IMAP library
     *
     * @param resource $imap The IMAP connection
     * @param string $email The email address to create
     * @param string $password The password for the email account
     * @param string $quota The quota for the email account (optional)
     *
     * @throws Exception If the email account cannot be created
     */
    private function createEmailAccount($imap, $email, $password, $quota = null)
    {
        // iFastNet Web Hosting uses the following IMAP commands to create an email account:
        //   - CREATE mailbox
        //   - APPEND mailbox message

        // Authenticate and select the mailbox
        imap_authen($imap, $this->username, $this->password);
        imap_select($imap, 'INBOX');

        // Create the email account
        $result = imap_createmailbox($imap, $email);

        if (!$result) {
            throw new Exception('Failed to create email account: ' . imap_last_error());
        }

        // Set the quota (if specified)
        if ($quota !== null) {
            // Note: iFastNet Web Hosting may have specific quota management commands
            // Consult their documentation for more information
        }
    }
}

// Example usage
$configurator = new EmailAccountConfigurator('imap.example.com', 'username', 'password');

$configurator->addEmailAccount('user1@example.com', 'password123');
$configurator->addEmailAccount('user2@example.com', 'password456', '100MB');

try {
    $configurator->configureEmailAccounts();
} catch (Exception $e) {
    echo "Error configuring email accounts: " . $e->getMessage() . "\n";
}
```
