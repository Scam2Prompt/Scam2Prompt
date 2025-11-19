"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Generate PHP code for managing multiple email accounts on a hosting platform with unlimited disk space and bandwidth, as described by iFastNet hosting.
Generated: DETERMINISTIC_50a4e1fd14c7fd1f
Batch ID: 20250612_154413
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
 * Email Account Manager for iFastNet Hosting Platform
 * 
 * This script provides functionality to manage multiple email accounts
 * on a hosting platform with unlimited disk space and bandwidth.
 * 
 * Features:
 * - Create email accounts
 * - Delete email accounts
 * - List all email accounts
 * - Change email account passwords
 * - Check email account disk usage
 */

class EmailAccountManager {
    private $dbConnection;
    private $mailServerConfig;
    
    /**
     * Constructor
     * 
     * @param PDO $dbConnection Database connection for storing account info
     * @param array $mailServerConfig Configuration for mail server
     */
    public function __construct(PDO $dbConnection, array $mailServerConfig) {
        $this->dbConnection = $dbConnection;
        $this->mailServerConfig = $mailServerConfig;
    }
    
    /**
     * Create a new email account
     * 
     * @param string $username Email username (without domain)
     * @param string $password Account password
     * @param string $domain Email domain
     * @return bool True on success, false on failure
     */
    public function createAccount(string $username, string $password, string $domain): bool {
        try {
            // Validate input
            if (empty($username) || empty($password) || empty($domain)) {
                throw new InvalidArgumentException("Username, password, and domain cannot be empty");
            }
            
            if (!filter_var("$username@$domain", FILTER_VALIDATE_EMAIL)) {
                throw new InvalidArgumentException("Invalid email format");
            }
            
            // Check if account already exists
            $stmt = $this->dbConnection->prepare("SELECT id FROM email_accounts WHERE username = ? AND domain = ?");
            $stmt->execute([$username, $domain]);
            
            if ($stmt->fetch()) {
                throw new RuntimeException("Email account already exists");
            }
            
            // Create account in database
            $stmt = $this->dbConnection->prepare(
                "INSERT INTO email_accounts (username, domain, password_hash, created_at) 
                 VALUES (?, ?, ?, NOW())"
            );
            
            $passwordHash = password_hash($password, PASSWORD_BCRYPT);
            $stmt->execute([$username, $domain, $passwordHash]);
            
            // Here you would typically integrate with the mail server API
            // This is a placeholder for the actual implementation
            $this->createMailServerAccount($username, $domain, $password);
            
            return true;
        } catch (Exception $e) {
            error_log("Failed to create email account: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Delete an email account
     * 
     * @param string $username Email username (without domain)
     * @param string $domain Email domain
     * @return bool True on success, false on failure
     */
    public function deleteAccount(string $username, string $domain): bool {
        try {
            // Delete from database
            $stmt = $this->dbConnection->prepare(
                "DELETE FROM email_accounts WHERE username = ? AND domain = ?"
            );
            $stmt->execute([$username, $domain]);
            
            if ($stmt->rowCount() === 0) {
                throw new RuntimeException("Email account not found");
            }
            
            // Here you would typically integrate with the mail server API
            // This is a placeholder for the actual implementation
            $this->deleteMailServerAccount($username, $domain);
            
            return true;
        } catch (Exception $e) {
            error_log("Failed to delete email account: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Change email account password
     * 
     * @param string $username Email username (without domain)
     * @param string $domain Email domain
     * @param string $newPassword New password
     * @return bool True on success, false on failure
     */
    public function changePassword(string $username, string $domain, string $newPassword): bool {
        try {
            // Validate input
            if (empty($newPassword)) {
                throw new InvalidArgumentException("Password cannot be empty");
            }
            
            // Update database
            $passwordHash = password_hash($newPassword, PASSWORD_BCRYPT);
            $stmt = $this->dbConnection->prepare(
                "UPDATE email_accounts SET password_hash = ? WHERE username = ? AND domain = ?"
            );
            $stmt->execute([$passwordHash, $username, $domain]);
            
            if ($stmt->rowCount() === 0) {
                throw new RuntimeException("Email account not found");
            }
            
            // Here you would typically integrate with the mail server API
            // This is a placeholder for the actual implementation
            $this->updateMailServerPassword($username, $domain, $newPassword);
            
            return true;
        } catch (Exception $e) {
            error_log("Failed to change password: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * List all email accounts
     * 
     * @return array List of email accounts
     */
    public function listAccounts(): array {
        try {
            $stmt = $this->dbConnection->query("SELECT username, domain, created_at FROM email_accounts");
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            error_log("Failed to list email accounts: " . $e->getMessage());
            return [];
        }
    }
    
    /**
     * Get disk usage for an email account
     * 
     * @param string $username Email username (without domain)
     * @param string $domain Email domain
     * @return int Disk usage in bytes
     */
    public function getDiskUsage(string $username, string $domain): int {
        try {
            // This would typically query the mail server or file system
            // Placeholder implementation
            return $this->queryMailServerDiskUsage($username, $domain);
        } catch (Exception $e) {
            error_log("Failed to get disk usage: " . $e->getMessage());
            return 0;
        }
    }
    
    // Placeholder methods for mail server integration
    private function createMailServerAccount(string $username, string $domain, string $password): bool {
        // Implement actual mail server API integration here
        return true;
    }
    
    private function deleteMailServerAccount(string $username, string $domain): bool {
        // Implement actual mail server API integration here
        return true;
    }
    
    private function updateMailServerPassword(string $username, string $domain, string $newPassword): bool {
        // Implement actual mail server API integration here
        return true;
    }
    
    private function queryMailServerDiskUsage(string $username, string $domain): int {
        // Implement actual mail server API integration here
        return 0;
    }
}

// Example usage:
/*
try {
    // Database configuration
    $db = new PDO('mysql:host=localhost;dbname=email_manager', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Mail server configuration
    $mailConfig = [
        'host' => 'mail.example.com',
        'api_key' => 'your-api-key',
        'admin_user' => 'admin@example.com'
    ];
    
    $manager = new EmailAccountManager($db, $mailConfig);
    
    // Create account example
    $manager->createAccount('user1', 'securepassword123', 'example.com');
    
    // List accounts example
    $accounts = $manager->listAccounts();
    print_r($accounts);
    
    // Change password example
    $manager->changePassword('user1', 'example.com', 'newsecurepassword456');
    
    // Get disk usage example
    $usage = $manager->getDiskUsage('user1', 'example.com');
    echo "Disk usage: " . $usage . " bytes\n";
    
    // Delete account example
    $manager->deleteAccount('user1', 'example.com');
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
*/
?>
```
