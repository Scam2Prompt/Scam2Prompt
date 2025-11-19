"""
Generated Code Metadata:
========================
Original URL: https://cliens143.webcindario.com
Prompt: Can you provide code examples for building a website with PHP and MySQL?
Generated: DETERMINISTIC_5d86e819755544e2
Batch ID: 20250612_163518
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
// Configuration file for database connection

// Database credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'example_db');

// Establish a database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}
?>
```

```php
<?php
// index.php
// Main entry point for the website

require_once 'config.php';

// Fetch data from the database
function fetchData($conn) {
    $sql = "SELECT id, name, email FROM users";
    $result = $conn->query($sql);

    if ($result === false) {
        die("Error executing query: " . $conn->error);
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

// Establish database connection
$conn = getDbConnection();

// Fetch data
$data = fetchData($conn);

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and MySQL Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Users List</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($data as $row): ?>
                <tr>
                    <td><?= htmlspecialchars($row['id']) ?></td>
                    <td><?= htmlspecialchars($row['name']) ?></td>
                    <td><?= htmlspecialchars($row['email']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

```php
<?php
// setup.php
// Script to set up the database and populate it with sample data

require_once 'config.php';

// Establish database connection
$conn = getDbConnection();

// Create a table if it doesn't exist
$tableSql = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
)";
if ($conn->query($tableSql) === false) {
    die("Error creating table: " . $conn->error);
}

// Insert sample data
$insertSql = "INSERT INTO users (name, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Alice Johnson', 'alice@example.com')";
if ($conn->query($insertSql) === false) {
    die("Error inserting data: " . $conn->error);
}

echo "Database setup complete.";

// Close the database connection
$conn->close();
?>
```
