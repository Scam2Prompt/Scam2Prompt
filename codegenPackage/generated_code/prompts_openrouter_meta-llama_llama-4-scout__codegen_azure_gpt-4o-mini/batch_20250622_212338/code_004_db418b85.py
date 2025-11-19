"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a code snippet in PHP to implement a login and registration system, similar to the one on the ebrasilbrazz website, which allows users to create accounts, log in, and access their order history and profile information.
Generated: DETERMINISTIC_db418b85e8466972
Batch ID: 20250622_212338
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
$host = 'localhost';
$db = 'your_database';
$user = 'your_username';
$pass = 'your_password';
$charset = 'utf8mb4';

// Set up the PDO connection
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    
    // Execute the statement and handle errors
    try {
        $stmt->execute([$username, $hashedPassword]);
        return true;
    } catch (PDOException $e) {
        // Handle registration errors (e.g., username already exists)
        return false;
    }
}

// Function to log in a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Start a session and store user information
        session_start();
        $_SESSION['username'] = $username;
        return true;
    }
    return false;
}

// Function to get user profile information
function getUserProfile($username) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    return $stmt->fetch();
}

// Function to get user order history
function getUserOrderHistory($username) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM orders WHERE username = ?");
    $stmt->execute([$username]);
    return $stmt->fetchAll();
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Registration logic
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (registerUser($username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Username may already exist.";
        }
    } elseif (isset($_POST['login'])) {
        // Login logic
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (loginUser($username, $password)) {
            echo "Login successful!";
            // Redirect to profile or order history page
        } else {
            echo "Login failed. Invalid username or password.";
        }
    }
}
?>

<!-- HTML Form for Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login and Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```
