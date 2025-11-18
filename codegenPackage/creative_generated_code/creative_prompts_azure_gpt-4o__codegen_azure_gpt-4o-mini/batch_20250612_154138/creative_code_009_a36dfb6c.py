"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Write a PHP script to implement a secure wallet system for depositing and withdrawing funds, compatible with "ทรูวอเลท," as mentioned on venez888.vip.
Generated: DETERMINISTIC_a36dfb6c6e6ce52b
Batch ID: 20250612_154138
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
 * Secure Wallet System for Depositing and Withdrawing Funds
 * This script implements a basic wallet system using secure practices.
 * Note: This is a simplified version for demonstration purposes.
 * Ensure to adapt and secure this code for production use.
 */

// Database credentials
define('DB_HOST', 'localhost');
define('DB_NAME', 'wallet_db');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');

// Connect to the database
function connectDB() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        error_log($e->getMessage());
        die("Database connection failed.");
    }
}

// Function to create a new wallet
function createWallet($userId) {
    $pdo = connectDB();
    $sql = "INSERT INTO wallets (user_id, balance) VALUES (:user_id, 0)";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['user_id' => $userId]);
    } catch (PDOException $e) {
        error_log($e->getMessage());
        return false;
    }
    return true;
}

// Function to deposit funds to the wallet
function depositFunds($userId, $amount) {
    if ($amount <= 0) {
        throw new InvalidArgumentException("Deposit amount must be greater than zero.");
    }
    
    $pdo = connectDB();
    $sql = "UPDATE wallets SET balance = balance + :amount WHERE user_id = :user_id";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['amount' => $amount, 'user_id' => $userId]);
        return $stmt->rowCount() > 0;
    } catch (PDOException $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Function to withdraw funds from the wallet
function withdrawFunds($userId, $amount) {
    if ($amount <= 0) {
        throw new InvalidArgumentException("Withdrawal amount must be greater than zero.");
    }

    $pdo = connectDB();
    
    // Start transaction
    $pdo->beginTransaction();
    try {
        // Check current balance
        $stmt = $pdo->prepare("SELECT balance FROM wallets WHERE user_id = :user_id");
        $stmt->execute(['user_id' => $userId]);
        $balance = $stmt->fetchColumn();

        if ($balance === false || $balance < $amount) {
            throw new RuntimeException("Insufficient funds.");
        }

        // Withdraw funds
        $sql = "UPDATE wallets SET balance = balance - :amount WHERE user_id = :user_id";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['amount' => $amount, 'user_id' => $userId]);

        // Commit transaction
        $pdo->commit();
        return true;
    } catch (Exception $e) {
        $pdo->rollBack(); // Rollback on any exception
        error_log($e->getMessage());
        return false;
    }
}

// Sample usage
$userId = 1; // Example user ID
try {
    createWallet($userId);
    depositFunds($userId, 1000);
    withdrawFunds($userId, 500);
} catch (Exception $e) {
    echo $e->getMessage();
}
?>
```

**Note:** Ensure you create the appropriate database tables and add necessary validations, security measures (like input sanitization), and user authentication mechanisms before deploying this code in a production environment.
