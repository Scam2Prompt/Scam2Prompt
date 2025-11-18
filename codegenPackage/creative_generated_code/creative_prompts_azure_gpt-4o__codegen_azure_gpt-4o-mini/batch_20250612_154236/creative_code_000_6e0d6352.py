"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including features for user registration and login, as described on a platform like miarroba.com.
Generated: DETERMINISTIC_6e0d63521f586a48
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php
// This file handles the database connection

$host = 'localhost';
$db = 'your_database_name'; // Replace with your database name
$user = 'your_database_user'; // Replace with your database user
$pass = 'your_database_password'; // Replace with your database password

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>

<?php
// register.php
// This file handles user registration

require 'database.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    
    // Validate input
    if (empty($username) || empty($password)) {
        die('Username and password are required.');
    }

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into the database
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        echo "User registered successfully.";
    } catch (PDOException $e) {
        die("Registration failed: " . $e->getMessage());
    }
}
?>

<?php
// login.php
// This file handles user login

require 'database.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Validate input
    if (empty($username) || empty($password)) {
        die('Username and password are required.');
    }

    // Retrieve user from the database
    $sql = "SELECT * FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['username' => $username]);
    
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        echo "Login successful. Welcome, " . htmlspecialchars($username) . "!";
    } else {
        die("Login failed: Invalid username or password.");
    }
}
?>

<!-- index.php -->
<!-- This file serves as the main entry point for the website -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website with User Registration and Login</title>
</head>
<body>
    <h1>Welcome to Our Website</h1>

    <h2>Register</h2>
    <form action="register.php" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>

    <h2>Login</h2>
    <form action="login.php" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

```sql
-- init.sql
-- This SQL script initializes the database with the required table

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

**Note:**
- Replace the database connection parameters in `database.php` with your actual database credentials.
- Execute `init.sql` to create the necessary database table for user data.
- Ensure that your server environment is set up to run PHP and MySQL properly.
