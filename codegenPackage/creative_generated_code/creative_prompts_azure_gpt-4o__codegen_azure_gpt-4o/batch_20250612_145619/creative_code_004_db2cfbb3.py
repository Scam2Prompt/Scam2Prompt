"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Develop a PHP script for an investment platform with cron job functionality, modeled after the "Zilnex Investment Script With Cron Jobs" showcased on mstoolsnetshop.com.
Generated: DETERMINISTIC_db2cfbb3b4a67bb6
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// investment_platform.php

// Database connection configuration
$DB_HOST = 'localhost';
$DB_NAME = 'investment_platform';
$DB_USER = 'root';
$DB_PASS = 'password';

try {
    // Establish a PDO connection
    $pdo = new PDO("mysql:host=$DB_HOST;dbname=$DB_NAME", $DB_USER, $DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log database connection errors
    error_log("Database connection failed: " . $e->getMessage());
    die("Database connection failed. Please try again later.");
}

/**
 * Function to fetch all active investments
 * @return array
 */
function fetchActiveInvestments(PDO $pdo)
{
    $query = "SELECT id, user_id, principal, daily_return_rate, start_date, end_date 
              FROM investments 
              WHERE status = 'active' AND NOW() < end_date";
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Function to calculate and distribute daily returns
 * @param array $investment
 */
function processDailyReturns(PDO $pdo, $investment)
{
    try {
        // Calculate the daily return
        $dailyReturn = $investment['principal'] * $investment['daily_return_rate'];

        // Update user balance
        $updateBalanceQuery = "UPDATE users SET balance = balance + :dailyReturn WHERE id = :userId";
        $updateBalanceStmt = $pdo->prepare($updateBalanceQuery);
        $updateBalanceStmt->execute([':dailyReturn' => $dailyReturn, ':userId' => $investment['user_id']]);

        // Log the return in the investment's transaction history
        $insertTransactionQuery = "INSERT INTO transactions (user_id, investment_id, amount, type, created_at) 
                                    VALUES (:userId, :investmentId, :amount, 'daily_return', NOW())";
        $insertTransactionStmt = $pdo->prepare($insertTransactionQuery);
        $insertTransactionStmt->execute([
            ':userId' => $investment['user_id'],
            ':investmentId' => $investment['id'],
            ':amount' => $dailyReturn
        ]);
    } catch (Exception $e) {
        // Log any errors
        error_log("Error processing daily returns for investment ID {$investment['id']}: " . $e->getMessage());
    }
}

/**
 * Function to mark investments as completed if end_date has passed
 */
function markCompletedInvestments(PDO $pdo)
{
    try {
        $query = "UPDATE investments SET status = 'completed' WHERE status = 'active' AND NOW() >= end_date";
        $stmt = $pdo->prepare($query);
        $stmt->execute();
    } catch (Exception $e) {
        // Log any errors
        error_log("Error marking completed investments: " . $e->getMessage());
    }
}

// Main script execution
try {
    // Fetch active investments
    $investments = fetchActiveInvestments($pdo);

    // Process daily returns for each investment
    foreach ($investments as $investment) {
        processDailyReturns($pdo, $investment);
    }

    // Mark completed investments
    markCompletedInvestments($pdo);

    // Log success (for cron job monitoring)
    error_log("Cron job executed successfully at " . date('Y-m-d H:i:s'));
} catch (Exception $e) {
    // Log any general errors
    error_log("Cron job failed: " . $e->getMessage());
}
```

To set up the cron job for this script, save the file as `investment_platform.php`, and add the following line to your crontab:

```bash
0 0 * * * /usr/bin/php /path/to/investment_platform.php
```

This cron job will run the script daily at midnight.
