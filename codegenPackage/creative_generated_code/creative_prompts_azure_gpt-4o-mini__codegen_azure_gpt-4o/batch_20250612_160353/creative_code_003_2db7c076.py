"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinv.com
Prompt: Develop a PHP script that automates the sign-up process for new investors on Global Arbitrage Investments, ensuring to include necessary security measures mentioned on the site.
Generated: DETERMINISTIC_2db7c076fcae17eb
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// investor_signup.php

// Database connection credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'global_arbitrage');

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to establish a secure database connection
function getDbConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_EMULATE_PREPARES => false
        ]);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and return a generic message
        error_log($e->getMessage());
        die('Database connection failed.');
    }
}

// Function to validate and sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Function to generate a secure hashed password
function hashPassword($password) {
    return password_hash($password, PASSWORD_BCRYPT);
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture and sanitize user input
    $fullName = sanitizeInput($_POST['full_name'] ?? '');
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'] ?? '';
    $confirmPassword = $_POST['confirm_password'] ?? '';

    // Validate inputs
    if (empty($fullName) || empty($email) || empty($password) || empty($confirmPassword)) {
        die('All fields are required.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Invalid email format.');
    }

    if ($password !== $confirmPassword) {
        die('Passwords do not match.');
    }

    try {
        // Establish database connection
        $pdo = getDbConnection();

        // Check if the email already exists
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM investors WHERE email = :email");
        $stmt->execute(['email' => $email]);
        if ($stmt->fetchColumn() > 0) {
            die('Email already registered.');
        }

        // Insert new investor record
        $hashedPassword = hashPassword($password);
        $stmt = $pdo->prepare("INSERT INTO investors (full_name, email, password, created_at) VALUES (:full_name, :email, :password, NOW())");
        $stmt->execute([
            'full_name' => $fullName,
            'email' => $email,
            'password' => $hashedPassword
        ]);

        echo 'Investor account successfully created.';
    } catch (Exception $e) {
        // Log error and display a generic message
        error_log($e->getMessage());
        die('An error occurred. Please try again later.');
    }
} else {
    // If not a POST request, show an error message
    die('Invalid request method.');
}
?>
```
