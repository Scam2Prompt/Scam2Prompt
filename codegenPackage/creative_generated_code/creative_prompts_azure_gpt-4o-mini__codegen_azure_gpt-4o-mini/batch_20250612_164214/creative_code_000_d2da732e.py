"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Main entry point of the website

// Start a session for user management
session_start();

// Include database connection
require 'db.php';

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    // Validate and sanitize user input
    $username = filter_var(trim($_POST['username']), FILTER_SANITIZE_STRING);
    $password = password_hash(trim($_POST['password']), PASSWORD_DEFAULT); // Hash the password

    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Prepare an SQL statement for safe execution
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        if ($stmt->execute([$username, $password])) {
            $success = "User registered successfully!";
        } else {
            $error = "Error during registration. Please try again.";
        }
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = filter_var(trim($_POST['username']), FILTER_SANITIZE_STRING);
    $password = trim($_POST['password']);

    // Retrieve user data for verification
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        header("Location: dashboard.php");
        exit;
    } else {
        $error = "Invalid username or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Free Website</h1>

    <!-- Display registration form -->
    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <!-- Display login form -->
    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>

    <!-- Show error or success message -->
    <?php if (!empty($error)) : ?>
        <p style="color:red;"><?php echo $error; ?></p>
    <?php elseif (!empty($success)) : ?>
        <p style="color:green;"><?php echo $success; ?></p>
    <?php endif; ?>
</body>
</html>
```

```php
<?php
// db.php - Database connection file

// Database configuration
$host = 'localhost';
$db   = 'my_database'; // Replace with your database name
$user = 'my_user'; // Replace with your database username
$pass = 'my_password'; // Replace with your database password
$charset = 'utf8mb4';

// Set up the DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection errors
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
?>
```

```sql
-- install.sql - SQL script to create the database and table

-- Create the database
CREATE DATABASE my_database;

-- Use the created database
USE my_database;

-- Create a users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Note:
1. Replace placeholder values in the `db.php` file with your actual database credentials.
2. Run the `install.sql` script to set up the database and the `users` table.
3. Create a `styles.css` file for styling as per your requirement.
4. This is a basic implementation; further features and security measures are recommended for a production-ready system.
