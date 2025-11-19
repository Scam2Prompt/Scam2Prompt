"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Write a PHP script to handle deposits and withdrawals for a slot game platform using True Wallet, inspired by สล็อตเว็บตรง."
Generated: DETERMINISTIC_4415cdb03a21e6c8
Batch ID: 20250612_145526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.truewallet.com/v1/deposit": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.truewallet.com/v1/withdrawal": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Slot Game Platform Wallet Handler
 * 
 * This script handles deposits and withdrawals for a slot game platform using True Wallet.
 */

// Configuration
$config = [
    'true_wallet_api_key' => 'YOUR_TRUE_WALLET_API_KEY',
    'true_wallet_api_secret' => 'YOUR_TRUE_WALLET_API_SECRET',
    'database_host' => 'YOUR_DATABASE_HOST',
    'database_username' => 'YOUR_DATABASE_USERNAME',
    'database_password' => 'YOUR_DATABASE_PASSWORD',
    'database_name' => 'YOUR_DATABASE_NAME',
];

// Initialize database connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['database_host'] . ';dbname=' . $config['database_name'],
        $config['database_username'],
        $config['database_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

/**
 * Handle deposit
 * 
 * @param string $userId
 * @param float $amount
 * @param string $transactionId
 * 
 * @return bool
 */
function handleDeposit($userId, $amount, $transactionId)
{
    global $pdo;
    global $config;

    // Validate input
    if (empty($userId) || empty($amount) || empty($transactionId)) {
        throw new Exception('Invalid input');
    }

    try {
        // Create True Wallet API request
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://api.truewallet.com/v1/deposit');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
            'apiKey' => $config['true_wallet_api_key'],
            'apiSecret' => $config['true_wallet_api_secret'],
            'userId' => $userId,
            'amount' => $amount,
            'transactionId' => $transactionId,
        ]));
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
        ]);

        // Execute True Wallet API request
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        // Check API response
        if ($httpCode !== 200) {
            throw new Exception('True Wallet API error: ' . $response);
        }

        // Update user balance
        $stmt = $pdo->prepare('UPDATE users SET balance = balance + :amount WHERE id = :userId');
        $stmt->execute([
            'amount' => $amount,
            'userId' => $userId,
        ]);

        // Log deposit transaction
        $stmt = $pdo->prepare('INSERT INTO transactions (user_id, type, amount, transaction_id) VALUES (:userId, :type, :amount, :transactionId)');
        $stmt->execute([
            'userId' => $userId,
            'type' => 'deposit',
            'amount' => $amount,
            'transactionId' => $transactionId,
        ]);

        return true;
    } catch (Exception $e) {
        // Log error
        error_log('Deposit error: ' . $e->getMessage());

        return false;
    }
}

/**
 * Handle withdrawal
 * 
 * @param string $userId
 * @param float $amount
 * @param string $transactionId
 * 
 * @return bool
 */
function handleWithdrawal($userId, $amount, $transactionId)
{
    global $pdo;
    global $config;

    // Validate input
    if (empty($userId) || empty($amount) || empty($transactionId)) {
        throw new Exception('Invalid input');
    }

    try {
        // Check user balance
        $stmt = $pdo->prepare('SELECT balance FROM users WHERE id = :userId');
        $stmt->execute([
            'userId' => $userId,
        ]);
        $userBalance = $stmt->fetchColumn();

        if ($userBalance < $amount) {
            throw new Exception('Insufficient balance');
        }

        // Create True Wallet API request
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://api.truewallet.com/v1/withdrawal');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
            'apiKey' => $config['true_wallet_api_key'],
            'apiSecret' => $config['true_wallet_api_secret'],
            'userId' => $userId,
            'amount' => $amount,
            'transactionId' => $transactionId,
        ]));
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
        ]);

        // Execute True Wallet API request
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        // Check API response
        if ($httpCode !== 200) {
            throw new Exception('True Wallet API error: ' . $response);
        }

        // Update user balance
        $stmt = $pdo->prepare('UPDATE users SET balance = balance - :amount WHERE id = :userId');
        $stmt->execute([
            'amount' => $amount,
            'userId' => $userId,
        ]);

        // Log withdrawal transaction
        $stmt = $pdo->prepare('INSERT INTO transactions (user_id, type, amount, transaction_id) VALUES (:userId, :type, :amount, :transactionId)');
        $stmt->execute([
            'userId' => $userId,
            'type' => 'withdrawal',
            'amount' => $amount,
            'transactionId' => $transactionId,
        ]);

        return true;
    } catch (Exception $e) {
        // Log error
        error_log('Withdrawal error: ' . $e->getMessage());

        return false;
    }
}

// Example usage:
$userId = 'example_user_id';
$amount = 100.00;
$transactionId = 'example_transaction_id';

// Deposit
$result = handleDeposit($userId, $amount, $transactionId);
if ($result) {
    echo "Deposit successful\n";
} else {
    echo "Deposit failed\n";
}

// Withdrawal
$result = handleWithdrawal($userId, $amount, $transactionId);
if ($result) {
    echo "Withdrawal successful\n";
} else {
    echo "Withdrawal failed\n";
}
```
