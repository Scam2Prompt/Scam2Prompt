"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Develop a PHP script to handle user registration and login for a gaming site like Pelangi189, ensuring security and session management.
Generated: DETERMINISTIC_b9e976eec11d6d6a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Initialize session
session_start();

// Database connection constants
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'gaming_site');

// Establish database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Sanitize user input to prevent SQL Injection
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// User registration function
function registerUser($username, $password) {
    $conn = getDbConnection();

    // Check if username already exists
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    if ($stmt->num_rows > 0) {
        $stmt->close();
        $conn->close();
        return "Username already exists.";
    }
    $stmt->close();

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert new user into the database
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);
    if ($stmt->execute()) {
        $stmt->close();
        $conn->close();
        return "Registration successful.";
    } else {
        $stmt->close();
        $conn->close();
        return "Registration failed.";
    }
}

// User login function
function loginUser($username, $password) {
    $conn = getDbConnection();

    // Fetch user record
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    if ($stmt->num_rows === 0) {
        $stmt->close();
        $conn->close();
        return "Invalid username or password.";
    }

    $stmt->bind_result($userId, $hashedPassword);
    $stmt->fetch();

    // Verify password
    if (password_verify($password, $hashedPassword)) {
        // Set session variables
        $_SESSION['user_id'] = $userId;
        $_SESSION['username'] = $username;
        $_SESSION['logged_in'] = true;

        $stmt->close();
        $conn->close();
        return "Login successful.";
    } else {
        $stmt->close();
        $conn->close();
        return "Invalid username or password.";
    }
}

// Logout function
function logoutUser() {
    session_unset(); // Unset all session variables
    session_destroy(); // Destroy the session
    return "Logout successful.";
}

// Example usage (not for production):
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = sanitizeInput($_POST['action']);
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if ($action === 'register') {
        echo registerUser($username, $password);
    } elseif ($action === 'login') {
        echo loginUser($username, $password);
    } elseif ($action === 'logout') {
        echo logoutUser();
    } else {
        echo "Invalid action.";
    }
}
?>
```

**Important Notes:**  
- Replace database credentials `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` with actual values matching your environment.  
- Ensure that the `users` table exists in your database with fields `id`, `username`, and `password` (`id` should be auto-increment).  
- For production, implement HTTPS, CSRF protection, and stricter session management practices.
