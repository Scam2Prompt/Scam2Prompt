"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_164110
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

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Basic form validation
    if (empty($username) || empty($password)) {
        $error = "Please fill in all fields.";
    } else {
        // Validate user credentials
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch();

        // Verify password
        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            header("Location: dashboard.php");
            exit();
        } else {
            $error = "Invalid username or password.";
        }
    }
}

// Include the HTML header and form
include 'header.php';
?>

<div class="container">
    <h2>Login</h2>
    <?php if (isset($error)): ?>
        <div class="alert alert-danger"><?= htmlspecialchars($error) ?></div>
    <?php endif; ?>
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</div>

<?php
include 'footer.php';
?>

```

```php
<?php
// db.php - Database connection

// Database configuration
$host = 'localhost'; // Database host
$db = 'my_database'; // Database name
$user = 'my_user'; // Database username
$pass = 'my_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Set up the Data Source Name (DSN)
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
    // Handle connection error
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
?>

```

```php
<?php
// dashboard.php - User dashboard after logging in

// Start a session and check for user authentication
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: index.php");
    exit();
}

// Include the HTML header
include 'header.php';
?>

<div class="container">
    <h2>Welcome to your Dashboard</h2>
    <p>You are successfully logged in!</p>
    <a href="logout.php">Logout</a>
</div>

<?php
include 'footer.php';
?>

```

```php
<?php
// logout.php - Logout script

// Start a session
session_start();

// Destroy the session to log the user out
session_destroy();

// Redirect to login page
header("Location: index.php");
exit();
?>

```

```php
<!-- header.php - HTML header component -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS -->
</head>
<body>
```

```php
<!-- footer.php - HTML footer component -->
<footer>
    <p>&copy; <?= date("Y") ?> My Website. All rights reserved.</p>
</footer>
</body>
</html>
```

```sql
-- database.sql - SQL to create users table

CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
- Make sure to run the `database.sql` to create the necessary database and table.
- Use a suitable method to hash passwords before inserting them into the `users` table, for instance using `password_hash()`.
- Adjust database credentials in `db.php` accordingly.
- Ensure web server (like Apache or Nginx) and PHP are properly configured.
