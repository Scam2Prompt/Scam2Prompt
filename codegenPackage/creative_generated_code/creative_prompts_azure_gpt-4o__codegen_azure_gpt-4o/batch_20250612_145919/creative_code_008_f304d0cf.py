"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Write a code snippet in PHP for securely handling user registration and login processes, including bonus allocation upon signup, as described on BaxBet.
Generated: DETERMINISTIC_f304d0cf3ddbde09
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Enable error reporting for development; disable in production
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session
session_start();

// Database connection settings
define("DB_HOST", "localhost");
define("DB_USER", "your_db_user");
define("DB_PASSWORD", "your_db_password");
define("DB_NAME", "your_db_name");

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log the error and exit
    error_log("Database connection error: " . $e->getMessage());
    die("Error connecting to the database.");
}

// User registration function
function registerUser($username, $email, $password) {
    global $pdo;
    
    try {
        // Validate input
        if (empty($username) || empty($email) || empty($password)) {
            throw new Exception("All fields are required.");
        }
        
        // Check if the user already exists
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
        $stmt->execute(['email' => $email]);
        if ($stmt->rowCount() > 0) {
            throw new Exception("Email is already registered.");
        }
        
        // Hash the password securely
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        
        // Insert the user into the database
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password, bonus_balance) VALUES (:username, :email, :password, :bonus_balance)");
        $stmt->execute([
            'username' => $username,
            'email' => $email,
            'password' => $hashedPassword,
            'bonus_balance' => 100 // Allocate bonus points on signup
        ]);
        
        return "User registered successfully!";
    } catch (Exception $e) {
        return "Error: " . $e->getMessage();
    }
}

// User login function
function loginUser($email, $password) {
    global $pdo;
    
    try {
        // Validate input
        if (empty($email) || empty($password)) {
            throw new Exception("All fields are required.");
        }
        
        // Fetch the user record
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        if (!$user) {
            throw new Exception("Invalid email or password.");
        }
        
        // Verify the password
        if (!password_verify($password, $user['password'])) {
            throw new Exception("Invalid email or password.");
        }
        
        // Set session variables
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        $_SESSION['bonus_balance'] = $user['bonus_balance'];
        
        return "Login successful!";
    } catch (Exception $e) {
        return "Error: " . $e->getMessage();
    }
}

// Example usage (comment out in production)
// echo registerUser('JohnDoe', 'john@example.com', 'password123');
// echo loginUser('john@example.com', 'password123');

?>
```
