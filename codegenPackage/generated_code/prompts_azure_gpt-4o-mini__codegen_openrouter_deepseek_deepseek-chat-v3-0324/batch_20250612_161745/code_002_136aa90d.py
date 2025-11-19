"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a code snippet in PHP that handles user registration and login for an e-commerce website, inspired by the user account features on ebrasilbrazz.
Generated: DETERMINISTIC_136aa90d957f8942
Batch ID: 20250612_161745
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
 * User Authentication Handler for E-commerce Website
 * 
 * Handles user registration and login functionality with secure password hashing.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'ecommerce_db');

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session
session_start();

// Database connection
function getDBConnection() {
    try {
        $conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch(PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// User registration
function registerUser($username, $email, $password) {
    $conn = getDBConnection();
    
    try {
        // Check if user already exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE email = :email OR username = :username");
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        
        if ($stmt->rowCount() > 0) {
            return ['success' => false, 'message' => 'Username or email already exists'];
        }
        
        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
        
        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (username, email, password, created_at) 
                               VALUES (:username, :email, :password, NOW())");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        
        return ['success' => true, 'message' => 'Registration successful'];
    } catch(PDOException $e) {
        return ['success' => false, 'message' => 'Registration failed: ' . $e->getMessage()];
    }
}

// User login
function loginUser($email, $password) {
    $conn = getDBConnection();
    
    try {
        // Get user by email
        $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE email = :email");
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        
        if ($stmt->rowCount() == 1) {
            $user = $stmt->fetch(PDO::FETCH_ASSOC);
            
            // Verify password
            if (password_verify($password, $user['password'])) {
                // Set session variables
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $user['username'];
                $_SESSION['logged_in'] = true;
                
                return ['success' => true, 'message' => 'Login successful'];
            }
        }
        
        return ['success' => false, 'message' => 'Invalid email or password'];
    } catch(PDOException $e) {
        return ['success' => false, 'message' => 'Login failed: ' . $e->getMessage()];
    }
}

// User logout
function logoutUser() {
    session_unset();
    session_destroy();
    return ['success' => true, 'message' => 'Logged out successfully'];
}

// Check if user is logged in
function isLoggedIn() {
    return isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true;
}

// Example usage (would typically be in separate files)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        $response = [];
        
        switch ($_POST['action']) {
            case 'register':
                if (isset($_POST['username'], $_POST['email'], $_POST['password'])) {
                    $response = registerUser(
                        trim($_POST['username']),
                        trim($_POST['email']),
                        $_POST['password']
                    );
                }
                break;
                
            case 'login':
                if (isset($_POST['email'], $_POST['password'])) {
                    $response = loginUser(
                        trim($_POST['email']),
                        $_POST['password']
                    );
                }
                break;
                
            case 'logout':
                $response = logoutUser();
                break;
        }
        
        header('Content-Type: application/json');
        echo json_encode($response);
        exit();
    }
}
?>
```
