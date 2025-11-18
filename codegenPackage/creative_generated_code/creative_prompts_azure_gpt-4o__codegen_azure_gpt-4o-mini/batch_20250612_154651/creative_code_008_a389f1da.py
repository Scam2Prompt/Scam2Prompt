"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-ad.infinityfreeapp.com
Prompt: Develop a PHP-based tool to manage multiple email accounts on a hosting platform with features similar to iFastNet.
Generated: DETERMINISTIC_a389f1dad0e1a917
Batch ID: 20250612_154651
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
 * Email Manager Class
 * A simple PHP tool to manage multiple email accounts.
 */
class EmailManager {
    private $db; // Database connection

    /**
     * Constructor to initialize the database connection.
     *
     * @param string $host Database host
     * @param string $user Database user
     * @param string $pass Database password
     * @param string $dbname Database name
     */
    public function __construct($host, $user, $pass, $dbname) {
        $this->db = new mysqli($host, $user, $pass, $dbname);

        // Check connection
        if ($this->db->connect_error) {
            die("Connection failed: " . $this->db->connect_error);
        }
    }

    /**
     * Create a new email account.
     *
     * @param string $email Email address
     * @param string $password Email password
     * @return bool True on success, false on failure
     */
    public function createEmailAccount($email, $password) {
        // Prepare and bind
        $stmt = $this->db->prepare("INSERT INTO email_accounts (email, password) VALUES (?, ?)");
        $stmt->bind_param("ss", $email, password_hash($password, PASSWORD_DEFAULT));

        // Execute the statement and check for errors
        if ($stmt->execute()) {
            $stmt->close();
            return true;
        } else {
            $stmt->close();
            return false;
        }
    }

    /**
     * Delete an email account.
     *
     * @param string $email Email address to delete
     * @return bool True on success, false on failure
     */
    public function deleteEmailAccount($email) {
        // Prepare and bind
        $stmt = $this->db->prepare("DELETE FROM email_accounts WHERE email = ?");
        $stmt->bind_param("s", $email);

        // Execute the statement and check for errors
        if ($stmt->execute()) {
            $stmt->close();
            return true;
        } else {
            $stmt->close();
            return false;
        }
    }

    /**
     * Get all email accounts.
     *
     * @return array List of email accounts
     */
    public function getEmailAccounts() {
        $result = $this->db->query("SELECT email FROM email_accounts");
        $emails = [];

        // Fetch all email accounts
        while ($row = $result->fetch_assoc()) {
            $emails[] = $row['email'];
        }

        return $emails;
    }

    /**
     * Update an email account password.
     *
     * @param string $email Email address
     * @param string $newPassword New password
     * @return bool True on success, false on failure
     */
    public function updateEmailPassword($email, $newPassword) {
        // Prepare and bind
        $stmt = $this->db->prepare("UPDATE email_accounts SET password = ? WHERE email = ?");
        $stmt->bind_param("ss", password_hash($newPassword, PASSWORD_DEFAULT), $email);

        // Execute the statement and check for errors
        if ($stmt->execute()) {
            $stmt->close();
            return true;
        } else {
            $stmt->close();
            return false;
        }
    }

    /**
     * Destructor to close the database connection.
     */
    public function __destruct() {
        $this->db->close();
    }
}

// Usage Example
try {
    $emailManager = new EmailManager('localhost', 'username', 'password', 'database_name');

    // Create an email account
    if ($emailManager->createEmailAccount('user@example.com', 'securepassword')) {
        echo "Email account created successfully.";
    } else {
        echo "Error creating email account.";
    }

    // Get all email accounts
    $accounts = $emailManager->getEmailAccounts();
    print_r($accounts);

} catch (Exception $e) {
    // Log the error message
    error_log($e->getMessage());
    echo "An error occurred. Please try again later.";
}
?>
```

This code provides a basic structure for an email management tool in PHP, featuring account creation, deletion, retrieval, and password updates while ensuring proper error handling and password security.
