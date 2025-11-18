"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Write PHP code to create a simple website with a MySQL database connection, including user authentication functionality.
Generated: DETERMINISTIC_4355629f549f5a21
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// settings.php
// Configuration file for database connection
define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASS", "password");
define("DB_NAME", "example_db");

function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}
?>
```

```php
<?php
// create_tables.php
// Script to create required database tables
require 'settings.php';

$conn = getDbConnection();

// Create users table if it doesn't exist
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
)";
if (!$conn->query($sql)) {
    die("Error creating table: " . $conn->error);
}
$conn->close();

echo "Tables created successfully.";
?>
```

```php
<?php
// register.php
// User registration script
require 'settings.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    if (!isset($_POST['username']) || !isset($_POST['password'])) {
        die("Incomplete form data.");
    }

    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Hash password for secure storage
    $password_hash = password_hash($password, PASSWORD_DEFAULT);

    $conn = getDbConnection();

    // Prepare and execute query
    $stmt = $conn->prepare("INSERT INTO users (username, password_hash) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $password_hash);

    if ($stmt->execute()) {
        echo "User registered successfully.";
    } else {
        echo "Error: " . $conn->error;
    }

    $stmt->close();
    $conn->close();
} else {
    header("HTTP/1.1 405 Method Not Allowed");
    echo "Invalid request method.";
}
?>
```

```php
<?php
// login.php
// User login script
require 'settings.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    if (!isset($_POST['username']) || !isset($_POST['password'])) {
        die("Incomplete form data.");
    }

    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    $conn = getDbConnection();

    // Prepare and execute query
    $stmt = $conn->prepare("SELECT password_hash FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 1) {
        $row = $result->fetch_assoc();
        // Verify password
        if (password_verify($password, $row['password_hash'])) {
            $_SESSION['username'] = $username;
            echo "Login successful.";
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "No user found.";
    }

    $stmt->close();
    $conn->close();
} else {
    header("HTTP/1.1 405 Method Not Allowed");
    echo "Invalid request method.";
}
?>
```

```php
<?php
// index.php
// Main webpage
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Website</title>
</head>
<body>
    <h1>Welcome to the Simple Website</h1>
    <?php if (isset($_SESSION['username'])): ?>
        <p>Hello, <?php echo htmlspecialchars($_SESSION['username']); ?>!</p>
        <a href="logout.php">Logout</a>
    <?php else: ?>
        <form action="login.php" method="POST">
            <h2>Login</h2>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit">Login</button>
        </form>

        <form action="register.php" method="POST">
            <h2>Register</h2>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit">Register</button>
        </form>
    <?php endif; ?>
</body>
</html>
```

```php
<?php
// logout.php
// Logout functionality
session_start();
session_unset();
session_destroy();
header("Location: index.php");
exit();
?>
```
