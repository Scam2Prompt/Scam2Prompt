"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplusinvestment.com
Prompt: Write a PHP script to implement a withdrawal system for Bitplus Investment users, ensuring that funds used in ongoing trades are excluded from the available balance.
Generated: DETERMINISTIC_c53d6120e2b09370
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// withdrawal-system.php

/**
 * Withdrawal System for Bitplus Investment Users
 * 
 * This script implements a secure withdrawal system for users of Bitplus Investment.
 * Funds allocated in ongoing trades are excluded from the available balance.
 * 
 * Requirements:
 * - Ensure proper error handling.
 * - Exclude funds in ongoing trades from the withdrawal calculation.
 * - Follow best practices for security and readability.
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'bitplus_investment');

// Connect to the database
function connectToDatabase() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    if ($mysqli->connect_error) {
        throw new Exception("Database connection failed: " . $mysqli->connect_error);
    }

    return $mysqli;
}

// Get user balance excluding funds in ongoing trades
function getAvailableBalance($userId, $mysqli) {
    try {
        // Query to fetch the total balance
        $totalBalanceQuery = "SELECT total_balance FROM users WHERE id = ?";
        $stmt = $mysqli->prepare($totalBalanceQuery);
        $stmt->bind_param('i', $userId);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows === 0) {
            throw new Exception("User not found.");
        }

        $row = $result->fetch_assoc();
        $totalBalance = $row['total_balance'];

        // Query to fetch funds in ongoing trades
        $ongoingTradesQuery = "SELECT SUM(amount) AS funds_in_trades FROM trades WHERE user_id = ? AND status = 'ongoing'";
        $stmt = $mysqli->prepare($ongoingTradesQuery);
        $stmt->bind_param('i', $userId);
        $stmt->execute();
        $result = $stmt->get_result();

        $row = $result->fetch_assoc();
        $fundsInTrades = isset($row['funds_in_trades']) ? $row['funds_in_trades'] : 0;

        // Calculate available balance
        $availableBalance = $totalBalance - $fundsInTrades;

        return $availableBalance;
    } catch (Exception $e) {
        throw new Exception("Error retrieving balance: " . $e->getMessage());
    }
}

// Process withdrawal request
function processWithdrawal($userId, $withdrawAmount, $mysqli) {
    try {
        // Get available balance
        $availableBalance = getAvailableBalance($userId, $mysqli);

        if ($withdrawAmount > $availableBalance) {
            throw new Exception("Insufficient funds available for withdrawal.");
        }

        // Update user balance in the database
        $updateBalanceQuery = "UPDATE users SET total_balance = total_balance - ? WHERE id = ?";
        $stmt = $mysqli->prepare($updateBalanceQuery);
        $stmt->bind_param('di', $withdrawAmount, $userId);

        if (!$stmt->execute()) {
            throw new Exception("Failed to update user balance.");
        }

        // Log the withdrawal
        $logWithdrawalQuery = "INSERT INTO withdrawals (user_id, amount, withdrawal_date) VALUES (?, ?, NOW())";
        $stmt = $mysqli->prepare($logWithdrawalQuery);
        $stmt->bind_param('id', $userId, $withdrawAmount);

        if (!$stmt->execute()) {
            throw new Exception("Failed to log the withdrawal.");
        }

        return "Withdrawal successful.";
    } catch (Exception $e) {
        return "Error processing withdrawal: " . $e->getMessage();
    }
}

// Example usage
try {
    $mysqli = connectToDatabase();

    // Assume user ID and withdrawal amount are obtained from user input
    $userId = 1; // Replace with actual user ID
    $withdrawAmount = 500; // Replace with actual withdrawal amount

    // Security measure: Validate user input (ensure they are integers and positive values)
    if (!is_int($userId) || $userId <= 0 || !is_numeric($withdrawAmount) || $withdrawAmount <= 0) {
        throw new Exception("Invalid input.");
    }

    $result = processWithdrawal($userId, $withdrawAmount, $mysqli);

    echo $result;

    $mysqli->close();
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage();
}
?>
```
