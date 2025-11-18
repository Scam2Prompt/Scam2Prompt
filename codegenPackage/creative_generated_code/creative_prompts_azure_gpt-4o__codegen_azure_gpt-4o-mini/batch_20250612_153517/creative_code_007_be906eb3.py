"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Develop a PHP script to handle user registration and deposit functionality for an online slot platform, with a minimum deposit of 20,000 IDR, as specified on ANGKA805.
Generated: DETERMINISTIC_be906eb3353c794a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include database configuration
require_once 'config.php';

/**
 * Class User
 * Handles user registration and deposit functionalities.
 */
class User {
    private $db;

    // Constructor to initialize database connection
    public function __construct($database) {
        $this->db = $database;
    }

    /**
     * Registers a new user in the database.
     *
     * @param string $username The username of the user.
     * @param string $password The password of the user.
     * @return bool True on success, false on failure.
     */
    public function register($username, $password) {
        // Check if username already exists
        if ($this->usernameExists($username)) {
            throw new Exception("Username already exists.");
        }

        // Hash password for security
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Prepare SQL statement
        $stmt = $this->db->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);

        // Execute the statement and check for success
        return $stmt->execute();
    }

    /**
     * Deposits an amount to the user's account.
     *
     * @param string $username The username of the user.
     * @param float $amount The deposit amount.
     * @return bool True on success, false on failure.
     * @throws Exception if deposit amount is less than minimum deposit.
     */
    public function deposit($username, $amount) {
        // Define minimum deposit
        $minimumDeposit = 20000;

        // Validate deposit amount
        if ($amount < $minimumDeposit) {
            throw new Exception("Deposit amount must be at least {$minimumDeposit} IDR.");
        }

        // Prepare SQL statement
        $stmt = $this->db->prepare("UPDATE users SET balance = balance + :amount WHERE username = :username");

        // Bind parameters
        $stmt->bindParam(':amount', $amount);
        $stmt->bindParam(':username', $username);

        // Execute the statement and check for success
        return $stmt->execute();
    }

    /**
     * Checks if the username already exists in the database.
     *
     * @param string $username The username to check.
     * @return bool True if exists, false otherwise.
     */
    private function usernameExists($username) {
        // Prepare SQL statement
        $stmt = $this->db->prepare("SELECT COUNT(*) FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        
        // Fetch the count
        return $stmt->fetchColumn() > 0;
    }
}

// Handle POST requests for registration and deposit
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
        // Create a new instance of User class
        $user = new User($db); // $db is assumed to be the PDO instance from config.php

        // Check if action is registration
        if (isset($_POST['action']) && $_POST['action'] === 'register') {
            $username = $_POST['username'];
            $password = $_POST['password'];

            // Register user
            if ($user->register($username, $password)) {
                echo "Registration successful.";
            }
        }

        // Check if action is deposit
        if (isset($_POST['action']) && $_POST['action'] === 'deposit') {
            $username = $_POST['username'];
            $amount = floatval($_POST['amount']);

            // Deposit amount
            if ($user->deposit($username, $amount)) {
                echo "Deposit successful.";
            }
        }
    } catch (Exception $e) {
        // Handle exceptions and display error message
        echo "Error: " . $e->getMessage();
    }
}
?>
```
