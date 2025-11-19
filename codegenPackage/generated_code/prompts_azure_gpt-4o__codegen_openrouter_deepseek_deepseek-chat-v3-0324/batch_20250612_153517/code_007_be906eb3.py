"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Develop a PHP script to handle user registration and deposit functionality for an online slot platform, with a minimum deposit of 20,000 IDR, as specified on ANGKA805.
Generated: DETERMINISTIC_be906eb3353c794a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * User Registration and Deposit Handler for Online Slot Platform
 * 
 * This script handles user registration and deposit functionality with a minimum deposit of 20,000 IDR.
 * It validates input, processes registration, and handles deposit transactions.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'slot_platform');
define('MIN_DEPOSIT', 20000); // Minimum deposit in IDR

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session
session_start();

// Create database connection
function getDBConnection() {
    try {
        $conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch(PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Validate input data
function validateInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Handle user registration
function registerUser($username, $email, $password) {
    try {
        $conn = getDBConnection();
        
        // Check if username or email already exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE username = :username OR email = :email");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        
        if ($stmt->rowCount() > 0) {
            return ['success' => false, 'message' => 'Username or email already exists'];
        }
        
        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        
        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (username, email, password, created_at) 
                               VALUES (:username, :email, :password, NOW())");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        
        $userId = $conn->lastInsertId();
        
        return ['success' => true, 'user_id' => $userId];
    } catch(PDOException $e) {
        return ['success' => false, 'message' => 'Registration failed: ' . $e->getMessage()];
    }
}

// Handle deposit transaction
function processDeposit($userId, $amount) {
    try {
        // Validate deposit amount
        if ($amount < MIN_DEPOSIT) {
            return ['success' => false, 'message' => 'Minimum deposit is ' . MIN_DEPOSIT . ' IDR'];
        }
        
        $conn = getDBConnection();
        
        // Start transaction
        $conn->beginTransaction();
        
        // Get current balance
        $stmt = $conn->prepare("SELECT balance FROM user_balances WHERE user_id = :user_id FOR UPDATE");
        $stmt->bindParam(':user_id', $userId);
        $stmt->execute();
        $currentBalance = $stmt->fetchColumn();
        
        // If no balance record exists, create one
        if ($currentBalance === false) {
            $stmt = $conn->prepare("INSERT INTO user_balances (user_id, balance) VALUES (:user_id, 0)");
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();
            $currentBalance = 0;
        }
        
        // Update balance
        $newBalance = $currentBalance + $amount;
        $stmt = $conn->prepare("UPDATE user_balances SET balance = :balance WHERE user_id = :user_id");
        $stmt->bindParam(':balance', $newBalance);
        $stmt->bindParam(':user_id', $userId);
        $stmt->execute();
        
        // Record transaction
        $stmt = $conn->prepare("INSERT INTO transactions (user_id, amount, type, status, created_at) 
                               VALUES (:user_id, :amount, 'deposit', 'completed', NOW())");
        $stmt->bindParam(':user_id', $userId);
        $stmt->bindParam(':amount', $amount);
        $stmt->execute();
        
        // Commit transaction
        $conn->commit();
        
        return ['success' => true, 'new_balance' => $newBalance];
    } catch(PDOException $e) {
        // Rollback transaction if error occurs
        if (isset($conn) && $conn->inTransaction()) {
            $conn->rollBack();
        }
        return ['success' => false, 'message' => 'Deposit failed: ' . $e->getMessage()];
    }
}

// Main request handler
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json');
    
    $response = [];
    
    // Handle registration
    if (isset($_POST['action']) && $_POST['action'] === 'register') {
        $username = validateInput($_POST['username'] ?? '');
        $email = validateInput($_POST['email'] ?? '');
        $password = validateInput($_POST['password'] ?? '');
        
        if (empty($username) || empty($email) || empty($password)) {
            $response = ['success' => false, 'message' => 'All fields are required'];
        } else {
            $response = registerUser($username, $email, $password);
            
            // If registration successful, store user ID in session
            if ($response['success']) {
                $_SESSION['user_id'] = $response['user_id'];
            }
        }
    }
    // Handle deposit
    elseif (isset($_POST['action']) && $_POST['action'] === 'deposit') {
        if (!isset($_SESSION['user_id'])) {
            $response = ['success' => false, 'message' => 'User not logged in'];
        } else {
            $amount = filter_input(INPUT_POST, 'amount', FILTER_VALIDATE_FLOAT);
            
            if ($amount === false || $amount <= 0) {
                $response = ['success' => false, 'message' => 'Invalid deposit amount'];
            } else {
                $response = processDeposit($_SESSION['user_id'], $amount);
            }
        }
    } else {
        $response = ['success' => false, 'message' => 'Invalid action'];
    }
    
    echo json_encode($response);
    exit;
}

// HTML form for registration and deposit (simplified for demonstration)
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ANGKA805 - Slot Platform</title>
    <style>
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; box-sizing: border-box; }
        button { padding: 10px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        .message { margin-top: 15px; padding: 10px; border-radius: 4px; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ANGKA805 Slot Platform</h1>
        
        <?php if (!isset($_SESSION['user_id'])): ?>
        <div id="registration-form">
            <h2>Register</h2>
            <form id="register-form" method="post">
                <input type="hidden" name="action" value="register">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Register</button>
            </form>
            <div id="register-message" class="message" style="display: none;"></div>
        </div>
        <?php else: ?>
        <div id="deposit-form">
            <h2>Make a Deposit</h2>
            <p>Minimum deposit: <?php echo number_format(MIN_DEPOSIT); ?> IDR</p
