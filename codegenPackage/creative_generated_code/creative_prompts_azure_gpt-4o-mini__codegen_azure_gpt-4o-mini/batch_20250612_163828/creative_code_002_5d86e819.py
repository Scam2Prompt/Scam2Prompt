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
// database.php
// Database connection configuration

// Database configuration constants
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root'); // Database username
define('DB_PASS', ''); // Database password
define('DB_NAME', 'my_database'); // Database name

/**
 * Establishes a connection to the MySQL database.
 *
 * @return mysqli The MySQLi connection object on success, or terminates the script on failure.
 */
function getDbConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}
```

```php
<?php
// add_user.php
// Script to add a new user to the database

require 'database.php';

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);

    // Input validation
    if (empty($name) || empty($email)) {
        die("Name and email are required.");
    }

    // Establish database connection
    $connection = getDbConnection();

    // Prepare and bind
    $stmt = $connection->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    $stmt->bind_param("ss", $name, $email);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        echo "New user added successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add User</title>
</head>
<body>
    <h1>Add New User</h1>
    <form method="POST" action="add_user.php">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <input type="submit" value="Add User">
    </form>
</body>
</html>
```

```php
<?php
// view_users.php
// Script to display all users from the database

require 'database.php';

// Establish database connection
$connection = getDbConnection();

// Prepare the query
$sql = "SELECT name, email FROM users";
$result = $connection->query($sql);

// Check if any users exist
if ($result->num_rows > 0) {
    echo "<h1>User List</h1>";
    echo "<table border='1'><tr><th>Name</th><th>Email</th></tr>";
    
    // Output data of each row
    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>" . htmlspecialchars($row['name']) . "</td><td>" . htmlspecialchars($row['email']) . "</td></tr>";
    }
    echo "</table>";
} else {
    echo "No users found.";
}

// Close the connection
$connection->close();
?>
```

```sql
-- schema.sql
-- SQL script to create the users table

CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```plaintext
// .htaccess
# Rewrite rules to remove .php extension for cleaner URLs

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([a-zA-Z0-9_-]+)/?$ $1.php [L]
```

Make sure to create the database and the `users` table using the provided SQL script before running the PHP scripts.
