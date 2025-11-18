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
// wallet_api.php

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session to manage user authentication
session_start();

// Database configuration constants
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'slot_game');

// Define a shared secret key for JWT or other token-based authentication (used later)
define('SECRET_KEY', 'your_secret_key');

// Set content type for the API response
header('Content-Type: application/json');

// Connect to the database
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
        exit;
    }
}

// Authenticate the user (basic example for demonstration purposes)
function authenticateUser($token) {
    // Placeholder for token validation logic
    if ($token === SECRET_KEY) {
        return true; // Assume valid for example purposes
    } else {
        return false;
    }
}

// Handle the deposit operation
function deposit($userId, $amount) {
    if ($amount <= 0) {
        return ['error' => 'Invalid deposit amount'];
    }

    try {
        $pdo = connectDatabase();
        $stmt = $pdo->prepare("UPDATE wallets SET balance = balance + ? WHERE user_id = ?");
        $stmt->execute([$amount, $userId]);
        return ['success' => true, 'message' => 'Deposit successful'];
    } catch (PDOException $e) {
        return ['error' => 'Database error: ' . $e->getMessage()];
    }
}

// Handle the withdrawal operation
function withdraw($userId, $amount) {
    if ($amount <= 0) {
        return ['error' => 'Invalid withdrawal amount'];
    }

    try {
        $pdo = connectDatabase();
        $stmt = $pdo->prepare("SELECT balance FROM wallets WHERE user_id = ?");
        $stmt->execute([$userId]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$result || $result['balance'] < $amount) {
            return ['error' => 'Insufficient funds'];
        }

        $stmt = $pdo->prepare("UPDATE wallets SET balance = balance - ? WHERE user_id = ?");
        $stmt->execute([$amount, $userId]);
        return ['success' => true, 'message' => 'Withdrawal successful'];
    } catch (PDOException $e) {
        return ['error' => 'Database error: ' . $e->getMessage()];
    }
}

// Main API handler
function handleRequest() {
    // Validate the HTTP method
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        http_response_code(405); // Method Not Allowed
        echo json_encode(['error' => 'Invalid request method']);
        exit;
    }

    // Get the input data
    $input = json_decode(file_get_contents('php://input'), true);

    // Validate input
    if (!isset($input['action'], $input['user_id'], $input['amount'], $input['token'])) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Missing required fields']);
        exit;
    }

    // Authenticate user
    if (!authenticateUser($input['token'])) {
        http_response_code(403); // Forbidden
        echo json_encode(['error' => 'Unauthorized']);
        exit;
    }

    // Process the action
    $action = strtolower($input['action']);
    $userId = (int)$input['user_id'];
    $amount = (float)$input['amount'];

    if ($action === 'deposit') {
        $response = deposit($userId, $amount);
    } elseif ($action === 'withdraw') {
        $response = withdraw($userId, $amount);
    } else {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Invalid action']);
        exit;
    }

    // Send the response
    echo json_encode($response);
}

// Entry point for the API
handleRequest();
?>
```
