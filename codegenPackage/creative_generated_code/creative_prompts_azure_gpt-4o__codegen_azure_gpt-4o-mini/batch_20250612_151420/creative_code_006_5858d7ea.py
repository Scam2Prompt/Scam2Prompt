"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Create a PHP-based API for handling wallet deposits and withdrawals in online slot games, ensuring secure and fast transactions as described on "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_5858d7ea3d55bd3d
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// wallets_api.php

// Enable error reporting for development (disable in production)
// error_reporting(E_ALL);
// ini_set('display_errors', 1);

// Load required libraries (e.g., for database connection)
// include 'db_connection.php';

// Set headers for JSON response
header('Content-Type: application/json');

// Database connection configuration
$host = 'localhost';
$db = 'online_slots';
$user = 'root';
$pass = '';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Return error response in JSON format
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit();
}

/**
 * Function to handle wallet deposits
 *
 * @param int $userId The user ID making the deposit
 * @param float $amount The amount to be deposited
 * @return array Response message
 */
function deposit($userId, $amount) {
    global $pdo;

    // Validate input
    if ($amount <= 0) {
        return ['error' => 'Deposit amount must be positive.'];
    }

    try {
        // Begin a transaction
        $pdo->beginTransaction();

        // Update wallet balance in the database
        $stmt = $pdo->prepare("UPDATE wallets SET balance = balance + :amount WHERE user_id = :user_id");
        $stmt->execute(['amount' => $amount, 'user_id' => $userId]);

        // Commit the transaction
        $pdo->commit();

        return ['success' => 'Deposit successful.', 'new_balance' => getBalance($userId)];
    } catch (Exception $e) {
        // Rollback the transaction in case of error
        $pdo->rollBack();
        return ['error' => 'Deposit failed: ' . $e->getMessage()];
    }
}

/**
 * Function to handle wallet withdrawals
 *
 * @param int $userId The user ID making the withdrawal
 * @param float $amount The amount to be withdrawn
 * @return array Response message
 */
function withdraw($userId, $amount) {
    global $pdo;

    // Validate input
    if ($amount <= 0) {
        return ['error' => 'Withdrawal amount must be positive.'];
    }

    // Check current balance
    $currentBalance = getBalance($userId);
    if ($currentBalance < $amount) {
        return ['error' => 'Insufficient balance.'];
    }

    try {
        // Begin a transaction
        $pdo->beginTransaction();

        // Update wallet balance in the database
        $stmt = $pdo->prepare("UPDATE wallets SET balance = balance - :amount WHERE user_id = :user_id");
        $stmt->execute(['amount' => $amount, 'user_id' => $userId]);

        // Commit the transaction
        $pdo->commit();

        return ['success' => 'Withdrawal successful.', 'new_balance' => getBalance($userId)];
    } catch (Exception $e) {
        // Rollback the transaction in case of error
        $pdo->rollBack();
        return ['error' => 'Withdrawal failed: ' . $e->getMessage()];
    }
}

/**
 * Function to get the current balance of a user
 *
 * @param int $userId The user ID for balance inquiry
 * @return float Current balance of the user
 */
function getBalance($userId) {
    global $pdo;

    $stmt = $pdo->prepare("SELECT balance FROM wallets WHERE user_id = :user_id");
    $stmt->execute(['user_id' => $userId]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    return $result ? (float)$result['balance'] : 0.0;
}

// API Endpoint Handling
$requestMethod = $_SERVER['REQUEST_METHOD'];
$body = json_decode(file_get_contents('php://input'), true);

switch ($requestMethod) {
    case 'POST':
        // Determine if it's a deposit or withdrawal
        $action = isset($body['action']) ? $body['action'] : null;
        $userId = isset($body['user_id']) ? $body['user_id'] : null;
        $amount = isset($body['amount']) ? $body['amount'] : null;

        if ($action === 'deposit') {
            $response = deposit($userId, $amount);
        } elseif ($action === 'withdraw') {
            $response = withdraw($userId, $amount);
        } else {
            $response = ['error' => 'Invalid action specified.'];
        }
        break;

    default:
        $response = ['error' => 'Method not allowed.'];
        break;
}

// Send JSON response
echo json_encode($response);
?>
```
