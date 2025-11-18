"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Write PHP code for a login and registration system that mimics the "DUGEMSLOT LOGIN" and "DUGEMSLOT DAFTAR" functionalities.
Generated: DETERMINISTIC_84970239591aaa33
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost';
$db = 'dugem_slot';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

// Set up the connection using PDO
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

// Create a new PDO instance
try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to register a new user
function register($pdo, $username, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare and execute the insert query
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    if ($stmt->execute([$username, $hashedPassword])) {
        return true; // Registration successful
    } else {
        return false; // Registration failed
    }
}

// Function to log in a user
function login($pdo, $username, $password) {
    // Prepare and execute the select query
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    // Verify the password using password_verify
    if ($user && password_verify($password, $user['password'])) {
        // Start session and store user data
        session_start();
        $_SESSION['username'] = $username;
        return true; // Login successful
    } else {
        return false; // Login failed
    }
}

// Registration handler
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['register'])) {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Basic validation
    if (empty($username) || empty($password)) {
        echo "Username and password are required.";
    } else {
        if (register($pdo, $username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Username may already exist.";
        }
    }
}

// Login handler
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Basic validation
    if (empty($username) || empty($password)) {
        echo "Username and password are required.";
    } else {
        if (login($pdo, $username, $password)) {
            echo "Login successful! Welcome, $username.";
        } else {
            echo "Login failed. Invalid username or password.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DUGEMSLOT Login & Registration</title>
</head>
<body>
    <h1>DUGEMSLOT Login</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>

    <h1>DUGEMSLOT Registration</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>
</body>
</html>
```

**Note**: Ensure to create a database named `dugem_slot` and a `users` table with columns `id`, `username`, and `password` for this code to work correctly. The `id` column should be an auto-incrementing primary key.
