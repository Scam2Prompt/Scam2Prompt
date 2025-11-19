"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliens143.webcindario.com
Prompt: Can you provide code examples for building a website with PHP and MySQL?
Generated: DETERMINISTIC_5d86e819755544e2
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php
// Configuration file for database connection

// Database credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'example_db');

// Establish database connection
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}
?>
```

```php
<?php
// index.php
// Main entry point for the website

// Include database configuration
require 'config.php';

// Handle user input safely
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

// Fetch all records from a sample table
function fetchRecords() {
    $connection = getDatabaseConnection();

    $sql = "SELECT id, name, email FROM users";
    $result = $connection->query($sql);

    $records = [];
    if ($result && $result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $records[] = $row;
        }
    }

    // Close connection
    $connection->close();

    return $records;
}

// Process form submission to add a new user
function addUser($name, $email) {
    $connection = getDatabaseConnection();

    // Prepared statement to prevent SQL injection
    $stmt = $connection->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    if (!$stmt) {
        die("Failed to prepare statement: " . $connection->error);
    }

    $stmt->bind_param("ss", $name, $email);
    if (!$stmt->execute()) {
        die("Failed to execute query: " . $stmt->error);
    }

    // Close statement and connection
    $stmt->close();
    $connection->close();
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');

    if (!empty($name) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        addUser($name, $email);
        header('Location: index.php');
        exit;
    } else {
        $error = "Invalid input. Please provide a valid name and email address.";
    }
}

// Fetch existing users to display
$users = fetchRecords();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and MySQL Example</title>
</head>
<body>
    <h1>PHP and MySQL Example Website</h1>

    <!-- Display error message if any -->
    <?php if (!empty($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>

    <!-- Form to add a new user -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Add User</button>
    </form>

    <h2>Existing Users</h2>
    <ul>
        <?php foreach ($users as $user): ?>
            <li><?php echo htmlspecialchars($user['name']) . " (" . htmlspecialchars($user['email']) . ")"; ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```sql
-- database.sql
-- SQL script to set up the database and a sample table

-- Create database
CREATE DATABASE IF NOT EXISTS example_db;

-- Use the database
USE example_db;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);
```
