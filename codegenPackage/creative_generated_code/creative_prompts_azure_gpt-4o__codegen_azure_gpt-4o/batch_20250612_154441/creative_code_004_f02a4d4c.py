"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethopt.io
Prompt: Write a PHP script for handling secure user authentication and account management on an online betting platform like 2QCOM.
Generated: DETERMINISTIC_f02a4d4c8cfea590
Batch ID: 20250612_154441
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
 * Secure User Authentication and Account Management Script for Betting Platform
 * Author: Professional Software Developer
 * Date: YYYY-MM-DD
 */

// Initialize session
session_start();

// Load configuration (DB credentials, etc.)
require_once 'config.php';

// Load helper functions (e.g., input sanitization, password hashing)
require_once 'helpers.php';

// Database connection setup
try {
    $pdo = new PDO($dsn, $db_user, $db_password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (Exception $e) {
    error_log('Database connection failed: ' . $e->getMessage());
    die('Database connection failed.');
}

// Function to register a new user
function registerUser($pdo, $username, $password, $email) {
    // Input validation
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid email address.'];
    }
    if (strlen($password) < 8) {
        return ['success' => false, 'message' => 'Password must be at least 8 characters long.'];
    }

    // Check if username or email already exists
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username OR email = :email");
    $stmt->execute(['username' => $username, 'email' => $email]);
    if ($stmt->fetchColumn() > 0) {
        return ['success' => false, 'message' => 'Username or email already exists.'];
    }

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert the user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email, created_at) VALUES (:username, :password, :email, NOW())");
    $stmt->execute(['username' => $username, 'password' => $hashedPassword, 'email' => $email]);

    return ['success' => true, 'message' => 'Registration successful.'];
}

// Function to authenticate a user
function authenticateUser($pdo, $username, $password) {
    // Fetch the user record by username
    $stmt = $pdo->prepare("SELECT id, password FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch();

    // Verify password
    if ($user && password_verify($password, $user['password'])) {
        // Log the user in (store user ID in session)
        $_SESSION['user_id'] = $user['id'];
        return ['success' => true, 'message' => 'Login successful.'];
    }

    return ['success' => false, 'message' => 'Invalid username or password.'];
}

// Function to log out a user
function logoutUser() {
    // Clear the session
    session_unset();
    session_destroy();
    return ['success' => true, 'message' => 'Logged out successfully.'];
}

// Function to manage user settings (e.g., change email or password)
function updateUserSettings($pdo, $userId, $newEmail = null, $newPassword = null) {
    // Validate inputs
    if ($newEmail && !filter_var($newEmail, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid email address.'];
    }
    if ($newPassword && strlen($newPassword) < 8) {
        return ['success' => false, 'message' => 'Password must be at least 8 characters long.'];
    }

    // Build the update query dynamically
    $updates = [];
    $params = ['user_id' => $userId];
    if ($newEmail) {
        $updates[] = 'email = :email';
        $params['email'] = $newEmail;
    }
    if ($newPassword) {
        $updates[] = 'password = :password';
        $params['password'] = password_hash($newPassword, PASSWORD_BCRYPT);
    }

    // Execute the update
    if (!empty($updates)) {
        $stmt = $pdo->prepare("UPDATE users SET " . implode(', ', $updates) . " WHERE id = :user_id");
        $stmt->execute($params);
        return ['success' => true, 'message' => 'Account settings updated successfully.'];
    }

    return ['success' => false, 'message' => 'No updates provided.'];
}

// Example usage of the functions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? null;

    switch ($action) {
        case 'register':
            $result = registerUser($pdo, $_POST['username'], $_POST['password'], $_POST['email']);
            break;
        case 'login':
            $result = authenticateUser($pdo, $_POST['username'], $_POST['password']);
            break;
        case 'logout':
            $result = logoutUser();
            break;
        case 'update_settings':
            $result = updateUserSettings($pdo, $_SESSION['user_id'], $_POST['email'] ?? null, $_POST['password'] ?? null);
            break;
        default:
            $result = ['success' => false, 'message' => 'Invalid action.'];
    }

    // Return the result as JSON
    header('Content-Type: application/json');
    echo json_encode($result);
    exit;
}
?>
```
