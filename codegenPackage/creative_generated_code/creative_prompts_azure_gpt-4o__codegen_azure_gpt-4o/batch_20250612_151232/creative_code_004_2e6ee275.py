"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingressa-dvipta.webcindario.com
Prompt: Write a PHP script to create a user registration system with MySQL for a free website hosted on platforms like "miarroba.com."
Generated: DETERMINISTIC_2e6ee275405f9784
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// User Registration System for a Free Website

// Database configuration
define("DB_HOST", "localhost"); // Change to your host address
define("DB_USER", "your_username"); // Change to your database username
define("DB_PASS", "your_password"); // Change to your database password
define("DB_NAME", "your_database"); // Change to your database name

/**
 * Establish database connection
 * Returns a PDO instance on success or exits on failure
 */
function getDatabaseConnection() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Handle user registration
 */
function registerUser($pdo, $username, $email, $password) {
    // Validate input
    if (empty($username) || empty($email) || empty($password)) {
        return "All fields are required.";
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return "Invalid email address.";
    }

    // Check if the username or email already exists
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username OR email = :email");
    $stmt->execute(['username' => $username, 'email' => $email]);
    if ($stmt->fetchColumn() > 0) {
        return "Username or email already exists.";
    }

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
    $stmt->execute(['username' => $username, 'email' => $email, 'password' => $hashedPassword]);
    return "Registration successful.";
}

// HTML form and submission handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $pdo = getDatabaseConnection();
    $username = htmlspecialchars($_POST['username']);
    $email = htmlspecialchars($_POST['email']);
    $password = $_POST['password'];

    // Register the user and display the response
    $response = registerUser($pdo, $username, $email, $password);
    echo "<p>$response</p>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>

<?php
// Ensure the "users" table exists (run this once manually or in a setup script)
// CREATE TABLE users (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     username VARCHAR(50) NOT NULL UNIQUE,
//     email VARCHAR(100) NOT NULL UNIQUE,
//     password VARCHAR(255) NOT NULL,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
