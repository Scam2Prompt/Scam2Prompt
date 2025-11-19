"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://best-crypto-wallet.yivesites.com
Prompt: Create a code snippet in PHP that validates user registration on the APELBET site, including error handling for existing accounts.
Generated: DETERMINISTIC_59819adc89c8ec87
Batch ID: 20250612_135906
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
 * APELBET User Registration Validator
 * This script validates user registration, including error handling for existing accounts.
 * Best practices, clean code, and proper error handling are implemented.
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'apelbet');
define('DB_USER', 'root');
define('DB_PASS', '');

// Function to connect to the database
function connectToDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log and display error (generic message for security reasons)
        error_log($e->getMessage());
        die("Database connection failed.");
    }
}

// Function to validate user registration
function validateRegistration($username, $email, $password) {
    // Input validation
    if (empty($username) || empty($email) || empty($password)) {
        return ["success" => false, "message" => "All fields are required."];
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ["success" => false, "message" => "Invalid email format."];
    }
    if (strlen($password) < 8) {
        return ["success" => false, "message" => "Password must be at least 8 characters long."];
    }

    try {
        $pdo = connectToDatabase();
        
        // Check if username or email already exists
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username OR email = :email");
        $stmt->execute(['username' => $username, 'email' => $email]);
        $count = $stmt->fetchColumn();

        if ($count > 0) {
            return ["success" => false, "message" => "Username or email already exists."];
        }

        // Insert new user into the database
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->execute(['username' => $username, 'email' => $email, 'password' => $hashedPassword]);

        return ["success" => true, "message" => "Registration successful."];

    } catch (PDOException $e) {
        // Log and display error (generic message for security reasons)
        error_log($e->getMessage());
        return ["success" => false, "message" => "An error occurred during registration."];
    }
}

// Sample usage (replace with actual form data in production)
$username = "exampleUser";
$email = "example@example.com";
$password = "examplePassword";

$result = validateRegistration($username, $email, $password);
echo json_encode($result); // Output JSON response

?>
```
