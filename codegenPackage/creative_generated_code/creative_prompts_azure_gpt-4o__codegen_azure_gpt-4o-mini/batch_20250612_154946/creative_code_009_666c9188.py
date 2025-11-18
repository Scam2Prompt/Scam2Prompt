"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Create a PHP script to log and analyze declined transactions from The Prepper Codex, including reasons provided by the user's bank.
Generated: DETERMINISTIC_666c9188af0878a2
Batch ID: 20250612_154946
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
 * Declined Transaction Logger and Analyzer
 * This script logs declined transactions and analyzes the reasons provided by the user's bank.
 * It stores the data in a MySQL database for future analysis.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'transactions_db');
define('DB_USER', 'username');
define('DB_PASS', 'password');

/**
 * Connect to the MySQL database
 * 
 * @return PDO
 * @throws Exception if the connection fails
 */
function connectToDatabase() {
    try {
        $pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Log a declined transaction
 * 
 * @param string $transactionId The ID of the transaction
 * @param string $reason The reason for the decline
 * @param PDO $pdo The PDO database connection
 * @throws Exception if the insert fails
 */
function logDeclinedTransaction($transactionId, $reason, $pdo) {
    $sql = "INSERT INTO declined_transactions (transaction_id, decline_reason, created_at) VALUES (:transaction_id, :reason, NOW())";
    
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':transaction_id', $transactionId);
    $stmt->bindParam(':reason', $reason);

    if (!$stmt->execute()) {
        throw new Exception("Failed to log declined transaction: " . implode(", ", $stmt->errorInfo()));
    }
}

/**
 * Analyze declined transactions
 * 
 * @param PDO $pdo The PDO database connection
 * @return array Statistics of declined transactions
 */
function analyzeDeclinedTransactions($pdo) {
    $sql = "SELECT decline_reason, COUNT(*) as count FROM declined_transactions GROUP BY decline_reason";
    $stmt = $pdo->query($sql);
    
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

try {
    // Connecting to the database
    $pdo = connectToDatabase();

    // Example data - these would typically come from an API or user input
    $declinedTransactions = [
        ['transaction_id' => 'TX123456', 'reason' => 'Insufficient Funds'],
        ['transaction_id' => 'TX123457', 'reason' => 'Account Closed'],
        ['transaction_id' => 'TX123458', 'reason' => 'Fraud Suspicion'],
    ];

    // Logging each declined transaction
    foreach ($declinedTransactions as $transaction) {
        logDeclinedTransaction($transaction['transaction_id'], $transaction['reason'], $pdo);
    }

    // Analyzing declined transactions
    $analysis = analyzeDeclinedTransactions($pdo);

    // Outputting the analysis
    echo json_encode($analysis, JSON_PRETTY_PRINT);

} catch (Exception $e) {
    // Handle any errors gracefully
    error_log($e->getMessage());
    echo json_encode(['error' => 'An error occurred while processing transactions.']);
}
?>
```
