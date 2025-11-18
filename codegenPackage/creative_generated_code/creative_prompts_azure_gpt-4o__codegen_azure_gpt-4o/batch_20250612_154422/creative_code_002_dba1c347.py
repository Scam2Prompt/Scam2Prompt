"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahorat.webcindario.com
Prompt: Generate a PHP script to create a user registration system using MySQL, optimized for deployment on free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_dba1c34708a0283e
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * User Registration System
 * Author: Expert Programmer
 * Description: A secure and production-ready PHP script for user registration
 * optimized for free hosting platforms. Uses MySQL with error handling and security best practices.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Change 'localhost' as needed
define('DB_NAME', 'your_database_name'); // Update with your database name
define('DB_USER', 'your_username'); // Update with your MySQL username
define('DB_PASSWORD', 'your_password'); // Update with your MySQL password

// Establish connection to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize inputs
    $username = sanitizeInput($_POST['username'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $password = sanitizeInput($_POST['password'] ?? '');
    $confirmPassword = sanitizeInput($_POST['confirm_password'] ?? '');

    // Check required fields
    if (empty($username) || empty($email) || empty($password) || empty($confirmPassword)) {
        $error = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } elseif ($password !== $confirmPassword) {
        $error = "Passwords do not match.";
    } elseif (strlen($password) < 6) {
        $error = "Password must be at least 6 characters long.";
    } else {
        // Check if username or email already exists
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username OR email = :email");
        $stmt->execute(['username' => $username, 'email' => $email]);
        $exists = $stmt->fetchColumn();

        if ($exists > 0) {
            $error = "Username or email already exists.";
        } else {
            // Hash the password
            $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

            // Insert new user into the database
            try {
                $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
                $stmt->execute([
                    'username' => $username,
                    'email' => $email,
                    'password' => $hashedPassword
                ]);
                $success = "Registration successful!";
            } catch (PDOException $e) {
                $error = "Failed to register user: " . $e->getMessage();
            }
        }
    }
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
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <?php if (isset($success)): ?>
        <p style="color: green;"><?php echo $success; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>

<?php
// Ensure the 'users' table exists. Run this query in your database manually:
// CREATE TABLE users (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     username VARCHAR(50) NOT NULL UNIQUE,
//     email VARCHAR(100) NOT NULL UNIQUE,
//     password VARCHAR(255) NOT NULL,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
