"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_163828
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
    <title>Free Website with PHP and MySQL</title>
    <link rel="stylesheet" href="style.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>Welcome to My Free Website</h1>
    
    <?php if (!empty($error)): ?>
        <div class="error"><?= htmlspecialchars($error); ?></div>
    <?php endif; ?>
    
    <?php if (!empty($success)): ?>
        <div class="success"><?= htmlspecialchars($success); ?></div>
    <?php endif; ?>

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

```php
<?php
// db.php - Database connection file

// Database configuration
$host = 'localhost';
$db = 'my_database'; // Change to your database name
$user = 'root'; // Change to your database user
$pass = ''; // Change to your database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}
?>
```

```sql
-- create_users_table.sql - SQL to create users table

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```css
/* style.css - Basic styling for the website */

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
}

h1, h2 {
    color: #333;
}

form {
    margin-bottom: 20px;
}

input {
    display: block;
    margin: 10px 0;
    padding: 10px;
    width: 200px;
}

button {
    padding: 10px;
    color: #fff;
    background-color: #007BFF;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error {
    color: red;
}

.success {
    color: green;
}
```

### Important Notes:
1. **Database Configuration**: Update the database credentials in `db.php` to match your environment.
2. **Create Users Table**: Run the SQL script `create_users_table.sql` in your MySQL database to set up the users table.
3. **Custom Domain**: To use a custom domain, you will need to purchase a domain from a registrar and point it to your server's IP address. Ensure the server has PHP and MySQL installed.
