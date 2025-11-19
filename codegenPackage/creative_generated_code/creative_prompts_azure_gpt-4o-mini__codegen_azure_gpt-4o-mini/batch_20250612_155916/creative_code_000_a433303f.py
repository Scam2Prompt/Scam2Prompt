"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giacotex.cl
Prompt: Generate a PHP script for a web application hosted on Linux using the specifications from giacotex.cl.
Generated: DETERMINISTIC_a433303fcea43801
Batch ID: 20250612_155916
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
 * Simple PHP Web Application Script
 * This script serves as a basic web application for giacotex.cl
 * It demonstrates user registration and login functionalities.
 * 
 * Ensure you have the required environment set up:
 * - PHP >= 7.4
 * - MySQL database
 * 
 * Author: Your Name
 * Date: 2023-10-07
 */

// Enable error reporting for development (disable in production)
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_db_username');
define('DB_PASSWORD', 'your_db_password');
define('DB_DATABASE', 'your_db_name');

/**
 * Connect to the database using PDO
 *
 * @return PDO
 * @throws Exception
 */
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_SERVER . ";dbname=" . DB_DATABASE, DB_USERNAME, DB_PASSWORD);
        // Set the PDO error mode to exception
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection error
        die("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Register a new user
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function registerUser($username, $password) {
    $pdo = connectDatabase();
    try {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT); // Hash password
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        return $stmt->execute(); // Execute the statement
    } catch (PDOException $e) {
        // Handle registration error
        error_log("Registration error: " . $e->getMessage());
        return false;
    }
}

/**
 * Authenticate a user
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function loginUser($username, $password) {
    $pdo = connectDatabase();
    try {
        $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC); // Fetch user data

        if ($user && password_verify($password, $user['password'])) {
            // Password is correct
            return true;
        }
        return false; // Invalid credentials
    } catch (PDOException $e) {
        // Handle login error
        error_log("Login error: " . $e->getMessage());
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // User registration
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (registerUser($username, $password)) {
            echo "User registered successfully!";
        } else {
            echo "Registration failed.";
        }
    }

    if (isset($_POST['login'])) {
        // User login
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (loginUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }
}

// HTML Form for registration and login
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giacotex User Management</title>
</head>
<body>

<h2>User Registration</h2>
<form method="POST">
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit" name="register">Register</button>
</form>

<h2>User Login</h2>
<form method="POST">
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit" name="login">Login</button>
</form>

</body>
</html>
```
