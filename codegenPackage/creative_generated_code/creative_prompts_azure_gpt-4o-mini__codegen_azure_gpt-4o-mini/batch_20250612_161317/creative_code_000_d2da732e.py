"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2acnmzzlink.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_161317
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
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Basic form validation
    if (empty($username) || empty($password)) {
        $error = "Please fill in all fields.";
    } else {
        // Check credentials against the database
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch();

        // Verify password
        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            header("Location: dashboard.php");
            exit;
        } else {
            $error = "Invalid username or password.";
        }
    }
}

// Function to render the login form
function renderLoginForm($error = '') {
    return <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <input type="submit" value="Login">
    </form>
    <p style="color:red;">$error</p>
</body>
</html>
HTML;
}

// Render the login form or display an error
echo renderLoginForm($error ?? '');
?>
```

```php
<?php
// db.php - Database connection file

// Database credentials
$host = 'localhost';
$db = 'my_database';
$user = 'my_user';
$pass = 'my_password';
$charset = 'utf8mb4';

// Set up the Data Source Name (DSN)
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
-- create_tables.sql - SQL script to set up the necessary database table

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a sample user (password is 'password' hashed)
INSERT INTO users (username, password) VALUES
('testuser', '$2y$10$e0MYkHs8M.5h/c0T5I6D.eHnZiw3GEXQZBF8DUZ3s2klE4l9XoQ1G');
```

### Deployment Instructions
1. **Database Setup**: Run `create_tables.sql` to create the database schema.
2. **Configuration**: Update `db.php` with your database credentials.
3. **Server Setup**: Ensure PHP and MySQL are properly configured on your server.
4. **Custom Domain**: Point your domain to your server's IP address.
5. **Access the Site**: Open your browser and navigate to your domain to access the login page.
