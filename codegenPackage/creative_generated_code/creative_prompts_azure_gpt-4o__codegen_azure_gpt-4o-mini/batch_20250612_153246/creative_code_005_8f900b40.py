"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mywanderloop.com
Prompt: Write a script in PHP to manage user accounts and track promotional bonuses for online casinos, inspired by the features discussed on myWanderLoop.
Generated: DETERMINISTIC_8f900b401e1fe04a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'casino_db');
define('DB_USER', 'root');
define('DB_PASS', 'password');

/**
 * Class UserAccountManager
 * Handles user account management and promotional bonuses for an online casino.
 */
class UserAccountManager {
    private $pdo;

    // Constructor to initialize PDO
    public function __construct() {
        try {
            $this->pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            // Handle database connection error
            error_log("Database connection error: " . $e->getMessage());
            throw new Exception("Could not connect to the database.");
        }
    }

    /**
     * Create a new user account
     * 
     * @param string $username
     * @param string $password
     * @return bool
     */
    public function createUser($username, $password) {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        return $stmt->execute([':username' => $username, ':password' => $hashedPassword]);
    }

    /**
     * Get user information by username
     * 
     * @param string $username
     * @return array|null
     */
    public function getUser($username) {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute([':username' => $username]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    /**
     * Track promotional bonus for a user
     * 
     * @param string $username
     * @param float $amount
     * @return bool
     */
    public function trackBonus($username, $amount) {
        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("INSERT INTO bonuses (username, amount, date) VALUES (:username, :amount, NOW())");
        return $stmt->execute([':username' => $username, ':amount' => $amount]);
    }

    /**
     * Get all bonuses for a user
     * 
     * @param string $username
     * @return array
     */
    public function getBonuses($username) {
        $stmt = $this->pdo->prepare("SELECT * FROM bonuses WHERE username = :username");
        $stmt->execute([':username' => $username]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Destructor to close the database connection
    public function __destruct() {
        $this->pdo = null;
    }
}

// Example usage
try {
    $userManager = new UserAccountManager();
    
    // Create a new user
    if ($userManager->createUser('john_doe', 'securepassword')) {
        echo "User created successfully.\n";
    }

    // Track a bonus for the user
    if ($userManager->trackBonus('john_doe', 150.00)) {
        echo "Bonus tracked successfully.\n";
    }

    // Retrieve user bonuses
    $bonuses = $userManager->getBonuses('john_doe');
    print_r($bonuses);

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
