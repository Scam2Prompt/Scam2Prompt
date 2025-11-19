"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: How do I integrate PHP and MySQL to create a fully functional website?
Generated: DETERMINISTIC_4e356955ac5278dd
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
// database.php
// This file handles the database connection

// Database configuration
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// Options for the PDO connection
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch results as associative arrays
    PDO::ATTR_EMULATE_PREPARES   => false, // Use real prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (PDOException $e) {
    // Handle connection errors gracefully
    die("Database connection failed: " . $e->getMessage());
}
?>
```

```php
<?php
// index.php
// Main entry point for the web application

// Include the database connection
require 'database.php';

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    // Check if the input is valid
    if ($name && $email) {
        // Prepare an SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        
        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);

        // Execute the statement and check for success
        if ($stmt->execute()) {
            $successMessage = "User added successfully!";
        } else {
            $errorMessage = "Error adding user.";
        }
    } else {
        $errorMessage = "Invalid input data.";
    }
}

// Fetch existing users from the database
$stmt = $pdo->query("SELECT * FROM users");
$users = $stmt->fetchAll();
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

    <?php if (isset($successMessage)): ?>
        <div style="color: green;"><?php echo $successMessage; ?></div>
    <?php elseif (isset($errorMessage)): ?>
        <div style="color: red;"><?php echo $errorMessage; ?></div>
    <?php endif; ?>

    <!-- User registration form -->
    <form method="post" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Register</button>
    </form>

    <h2>Registered Users</h2>
    <ul>
        <?php foreach ($users as $user): ?>
            <li><?php echo htmlspecialchars($user['name']); ?> - <?php echo htmlspecialchars($user['email']); ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

**Database Setup SQL (for reference)**:
```sql
CREATE DATABASE your_database;
USE your_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

**Note**: Replace the placeholders `your_database`, `your_username`, and `your_password` with your actual database credentials before running the code.
