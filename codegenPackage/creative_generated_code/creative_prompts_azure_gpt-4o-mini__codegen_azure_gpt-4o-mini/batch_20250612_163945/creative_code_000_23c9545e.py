"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivihnasd1.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the page?
Generated: DETERMINISTIC_23c9545e9c016905
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection file using MySQLi

/**
 * Creates a database connection using MySQLi.
 *
 * @return mysqli Returns a connection object on success, or exits on failure.
 */
function getDatabaseConnection() {
    // Database configuration
    $host = 'localhost'; // MySQL server host
    $username = 'root'; // MySQL username
    $password = ''; // MySQL password
    $database = 'website_db'; // MySQL database name

    // Create connection
    $connection = new mysqli($host, $username, $password, $database);

    // Check connection
    if ($connection->connect_error) {
        die('Connection failed: ' . $connection->connect_error);
    }

    return $connection;
}
?>

<?php
// index.php - Main entry point for the website

/**
 * A simple PHP and MySQL based web application.
 */

// Include database connection
require_once 'database.php';

// Connect to the database
$connection = getDatabaseConnection();

// Set default timezone
date_default_timezone_set('UTC');

// Fetch records from the database
function fetchRecords($connection) {
    $sql = "SELECT * FROM users"; // SQL Query to select all users
    $result = $connection->query($sql);
    
    if ($result === false) {
        // Log error and return empty array
        error_log('Database query failed: ' . $connection->error);
        return [];
    }
    
    return $result->fetch_all(MYSQLI_ASSOC);
}

// Fetch records for display
$users = fetchRecords($connection);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Free Website</h1>
    </header>
    
    <main>
        <h2>User List</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Created At</th>
            </tr>
            <?php foreach ($users as $user): ?>
            <tr>
                <td><?php echo htmlspecialchars($user['id']); ?></td>
                <td><?php echo htmlspecialchars($user['name']); ?></td>
                <td><?php echo htmlspecialchars($user['email']); ?></td>
                <td><?php echo htmlspecialchars($user['created_at']); ?></td>
            </tr>
            <?php endforeach; ?>
        </table>
    </main>
    
    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Website</p>
    </footer>
</body>
</html>

<?php
// Close the database connection
$connection->close();
?>
```

```sql
-- setup.sql - SQL script to create the database and a users table

-- Create a database
CREATE DATABASE IF NOT EXISTS website_db;

USE website_db;

-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (name, email) VALUES
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com');
```

```css
/* styles.css - Basic styles for the website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 15px;
    text-align: center;
}

main {
    padding: 20px;
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
    background-color: #f2f2f2;
}
```

Make sure to run the `setup.sql` in your MySQL database to create the necessary database and table before testing the PHP files. Adjust the database connection credentials in `database.php` as needed.
