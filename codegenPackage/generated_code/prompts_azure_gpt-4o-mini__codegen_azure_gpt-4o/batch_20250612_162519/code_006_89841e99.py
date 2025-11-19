"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: Develop a simple web application using PHP and MySQL that can be hosted on IDN Hosting's SSD shared hosting platform.
Generated: DETERMINISTIC_89841e993bcfe155
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// config.php
// Database configuration file

// Database connection settings
define('DB_HOST', 'localhost'); // Change this if your hosting uses a different host
define('DB_NAME', 'your_database_name'); // Replace with your database name
define('DB_USER', 'your_database_user'); // Replace with your database username
define('DB_PASS', 'your_database_password'); // Replace with your database password

// Establish a connection to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>
```

```php
<?php
// index.php
// Main entry point for the web application

require 'config.php'; // Include database configuration

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);

    // Validate input
    if (empty($name) || empty($email)) {
        $error = "Name and email are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        // Insert data into the database
        try {
            $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
            $stmt->execute(['name' => $name, 'email' => $email]);
            $success = "User successfully added!";
        } catch (PDOException $e) {
            $error = "Failed to add user: " . $e->getMessage();
        }
    }
}

// Fetch all users from the database
try {
    $stmt = $pdo->query("SELECT * FROM users ORDER BY id DESC");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Failed to fetch users: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <h1>Simple Web Application</h1>

    <!-- Display success or error messages -->
    <?php if (!empty($error)): ?>
        <p class="error"><?= htmlspecialchars($error) ?></p>
    <?php endif; ?>
    <?php if (!empty($success)): ?>
        <p class="success"><?= htmlspecialchars($success) ?></p>
    <?php endif; ?>

    <!-- User input form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>

    <h2>Users List</h2>
    <ul>
        <?php foreach ($users as $user): ?>
            <li><?= htmlspecialchars($user['name']) ?> (<?= htmlspecialchars($user['email']) ?>)</li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```sql
-- database.sql
-- SQL script to create the necessary database and table

CREATE DATABASE IF NOT EXISTS your_database_name;

USE your_database_name;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
1. Replace `your_database_name`, `your_database_user`, and `your_database_password` in `config.php` with your actual database credentials.
2. Import the `database.sql` file into your MySQL database to set up the required table.
3. Ensure your hosting environment supports PHP and MySQL, and that the `pdo_mysql` extension is enabled.
