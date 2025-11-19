"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseeaquii.webcindario.com
Prompt: Can you provide code examples for building a website with PHP and MySQL?
Generated: DETERMINISTIC_5d86e819755544e2
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
// config.php
// Configuration file for database connection

// Database credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'example_db');

// Create a connection to the database
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
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

require 'config.php';

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';

    // Validate input
    if (empty($name) || empty($email)) {
        $error = 'Both name and email are required.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = 'Invalid email format.';
    } else {
        // Sanitize input to prevent SQL injection
        $connection = getDatabaseConnection();
        $stmt = $connection->prepare("INSERT INTO users (name, email) VALUES (?, ?)");

        if ($stmt) {
            $stmt->bind_param('ss', $name, $email);

            if ($stmt->execute()) {
                $success = 'User added successfully!';
            } else {
                $error = 'Database error: ' . $stmt->error;
            }

            $stmt->close();
        } else {
            $error = 'Database error: ' . $connection->error;
        }

        $connection->close();
    }
}

// Fetch users from the database to display
$connection = getDatabaseConnection();
$result = $connection->query("SELECT id, name, email FROM users");

$users = [];
if ($result) {
    while ($row = $result->fetch_assoc()) {
        $users[] = $row;
    }

    $result->free();
}

$connection->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and MySQL Website</title>
</head>
<body>
    <h1>Welcome to the PHP and MySQL Website</h1>

    <!-- Display success or error messages -->
    <?php if (!empty($error)): ?>
        <p style="color: red;"><?php echo htmlspecialchars($error); ?></p>
    <?php elseif (!empty($success)): ?>
        <p style="color: green;"><?php echo htmlspecialchars($success); ?></p>
    <?php endif; ?>

    <!-- Form for adding a new user -->
    <form action="index.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Add User</button>
    </form>

    <!-- Display list of users -->
    <h2>User List</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
        <?php foreach ($users as $user): ?>
        <tr>
            <td><?php echo htmlspecialchars($user['id']); ?></td>
            <td><?php echo htmlspecialchars($user['name']); ?></td>
            <td><?php echo htmlspecialchars($user['email']); ?></td>
        </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>
```

```sql
-- database.sql
-- SQL script to set up the database

-- Create the database
CREATE DATABASE IF NOT EXISTS example_db;

-- Use the database
USE example_db;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);
```
