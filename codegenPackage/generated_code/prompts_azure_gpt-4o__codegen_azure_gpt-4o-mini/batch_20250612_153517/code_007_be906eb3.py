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
// Database configuration
$host = 'localhost'; // Database host
$db = 'slot_platform'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Minimum deposit constant
define('MIN_DEPOSIT', 20000);

// Function to connect to the database
function connectDatabase($host, $db, $user, $pass) {
    try {
        $dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        return new PDO($dsn, $user, $pass, $options);
    } catch (PDOException $e) {
        // Handle connection error
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to register a new user
function registerUser($pdo, $username, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare SQL statement
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);
    
    // Execute the statement and handle potential errors
    try {
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        return true;
    } catch (PDOException $e) {
        // Handle registration error
        echo "Registration failed: " . $e->getMessage();
        return false;
    }
}

// Function to handle deposits
function deposit($pdo, $userId, $amount) {
    // Check if the deposit amount meets the minimum requirement
    if ($amount < MIN_DEPOSIT) {
        echo "Deposit amount must be at least " . MIN_DEPOSIT . " IDR.";
        return false;
    }

    // Prepare SQL statement to update user balance
    $sql = "UPDATE users SET balance = balance + :amount WHERE id = :userId";
    $stmt = $pdo->prepare($sql);
    
    // Execute the statement and handle potential errors
    try {
        $stmt->execute(['amount' => $amount, 'userId' => $userId]);
        echo "Deposit successful. New balance updated.";
        return true;
    } catch (PDOException $e) {
        // Handle deposit error
        echo "Deposit failed: " . $e->getMessage();
        return false;
    }
}

// Main script execution
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Connect to the database
    $pdo = connectDatabase($host, $db, $user, $pass);
    
    // Check if the action is registration
    if (isset($_POST['action']) && $_POST['action'] === 'register') {
        $username = $_POST['username'];
        $password = $_POST['password'];
        
        // Register the user
        if (registerUser($pdo, $username, $password)) {
            echo "User registered successfully.";
        }
    }
    
    // Check if the action is deposit
    if (isset($_POST['action']) && $_POST['action'] === 'deposit') {
        $userId = $_POST['userId'];
        $amount = $_POST['amount'];
        
        // Handle the deposit
        deposit($pdo, $userId, $amount);
    }
}
?>

<!-- HTML Form for User Registration and Deposit -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Deposit</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <input type="hidden" name="action" value="register">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <button type="submit">Register</button>
    </form>

    <h1>Deposit</h1>
    <form method="POST">
        <input type="hidden" name="action" value="deposit">
        <label for="userId">User ID:</label>
        <input type="number" name="userId" required>
        <label for="amount">Deposit Amount (IDR):</label>
        <input type="number" name="amount" required>
        <button type="submit">Deposit</button>
    </form>
</body>
</html>
```
