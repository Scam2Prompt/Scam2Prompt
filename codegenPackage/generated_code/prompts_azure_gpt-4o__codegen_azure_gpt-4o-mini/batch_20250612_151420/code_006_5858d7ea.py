"""
Generated Code Metadata:
========================
Original URL: https://buylibracoins.com
Prompt: Create a PHP-based API for handling wallet deposits and withdrawals in online slot games, ensuring secure and fast transactions as described on "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_5858d7ea3d55bd3d
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// wallet_api.php

// Enable error reporting for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Include necessary files for database connection
require 'database.php'; // Ensure this file contains the database connection logic

class WalletAPI {
    private $db;

    public function __construct($dbConnection) {
        $this->db = $dbConnection;
    }

    // Method to handle wallet deposits
    public function deposit($userId, $amount) {
        // Validate input
        if ($amount <= 0) {
            throw new InvalidArgumentException("Deposit amount must be greater than zero.");
        }

        // Start a transaction
        $this->db->beginTransaction();
        try {
            // Update user's wallet balance
            $stmt = $this->db->prepare("UPDATE users SET wallet_balance = wallet_balance + :amount WHERE id = :userId");
            $stmt->bindParam(':amount', $amount);
            $stmt->bindParam(':userId', $userId);
            $stmt->execute();

            // Log the transaction
            $this->logTransaction($userId, $amount, 'deposit');

            // Commit the transaction
            $this->db->commit();
            return ['status' => 'success', 'message' => 'Deposit successful.'];
        } catch (Exception $e) {
            // Rollback the transaction in case of error
            $this->db->rollBack();
            return ['status' => 'error', 'message' => 'Deposit failed: ' . $e->getMessage()];
        }
    }

    // Method to handle wallet withdrawals
    public function withdraw($userId, $amount) {
        // Validate input
        if ($amount <= 0) {
            throw new InvalidArgumentException("Withdrawal amount must be greater than zero.");
        }

        // Start a transaction
        $this->db->beginTransaction();
        try {
            // Check if user has sufficient balance
            $stmt = $this->db->prepare("SELECT wallet_balance FROM users WHERE id = :userId");
            $stmt->bindParam(':userId', $userId);
            $stmt->execute();
            $balance = $stmt->fetchColumn();

            if ($balance < $amount) {
                throw new RuntimeException("Insufficient balance for withdrawal.");
            }

            // Update user's wallet balance
            $stmt = $this->db->prepare("UPDATE users SET wallet_balance = wallet_balance - :amount WHERE id = :userId");
            $stmt->bindParam(':amount', $amount);
            $stmt->bindParam(':userId', $userId);
            $stmt->execute();

            // Log the transaction
            $this->logTransaction($userId, $amount, 'withdraw');

            // Commit the transaction
            $this->db->commit();
            return ['status' => 'success', 'message' => 'Withdrawal successful.'];
        } catch (Exception $e) {
            // Rollback the transaction in case of error
            $this->db->rollBack();
            return ['status' => 'error', 'message' => 'Withdrawal failed: ' . $e->getMessage()];
        }
    }

    // Method to log transactions
    private function logTransaction($userId, $amount, $type) {
        $stmt = $this->db->prepare("INSERT INTO transactions (user_id, amount, type, created_at) VALUES (:userId, :amount, :type, NOW())");
        $stmt->bindParam(':userId', $userId);
        $stmt->bindParam(':amount', $amount);
        $stmt->bindParam(':type', $type);
        $stmt->execute();
    }
}

// Example usage
try {
    $dbConnection = new PDO('mysql:host=localhost;dbname=your_database', 'username', 'password');
    $dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $walletAPI = new WalletAPI($dbConnection);

    // Handle deposit request
    $response = $walletAPI->deposit(1, 100); // Example user ID and amount
    echo json_encode($response);

    // Handle withdrawal request
    $response = $walletAPI->withdraw(1, 50); // Example user ID and amount
    echo json_encode($response);
} catch (Exception $e) {
    echo json_encode(['status' => 'error', 'message' => 'Database connection failed: ' . $e->getMessage()]);
}
?>
```

**Note:** Ensure to replace `'your_database'`, `'username'`, and `'password'` with your actual database credentials. The `database.php` file should contain the logic for establishing a database connection.
