"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepro10000.webcindario.com
Prompt: Can you provide code examples for building a website with PHP and MySQL?
Generated: DETERMINISTIC_5d86e819755544e2
Batch ID: 20250612_160703
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
define('DB_PASS', 'password'); // Database password
define('DB_NAME', 'my_database'); // Database name

/**
 * Function to establish a database connection
 * 
 * @return mysqli|null Returns mysqli object on success, null on failure
 */
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        error_log('Database connection error: ' . $connection->connect_error);
        return null; // Return null if connection failed
    }

    return $connection; // Return the connection object
}
?>
```

```php
<?php
// index.php
// Main entry point for the website

require_once 'database.php'; // Include database connection file

// Fetch records from the database
function fetchRecords() {
    $connection = getDatabaseConnection(); // Get database connection
    if ($connection === null) {
        return []; // Return empty array if connection failed
    }

    // SQL query to select data from a table
    $sql = 'SELECT * FROM users';
    $result = $connection->query($sql);

    // Check for query errors
    if (!$result) {
        error_log('Query error: ' . $connection->error);
        $connection->close();
        return [];
    }

    // Fetch all records as an associative array
    $records = $result->fetch_all(MYSQLI_ASSOC);
    $connection->close(); // Close the database connection
    return $records; // Return the fetched records
}

// Render records in HTML
function renderRecords($records) {
    if (empty($records)) {
        echo '<p>No records found.</p>';
        return;
    }

    echo '<table border="1">';
    echo '<tr><th>ID</th><th>Name</th><th>Email</th></tr>';
    foreach ($records as $record) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($record['id']) . '</td>';
        echo '<td>' . htmlspecialchars($record['name']) . '</td>';
        echo '<td>' . htmlspecialchars($record['email']) . '</td>';
        echo '</tr>';
    }
    echo '</table>';
}

// Main execution
$records = fetchRecords(); // Fetch records from the database
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Records</title>
</head>
<body>
    <h1>User Records</h1>
    <?php renderRecords($records); // Render the records ?>
</body>
</html>
```

```sql
-- schema.sql
-- SQL script to create the users table

CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Sample data insertion
INSERT INTO users (name, email) VALUES
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com');
```

Make sure to run the SQL script to create the database and table before executing the PHP code. Adjust the database configuration in `database.php` as necessary for your environment.
ing: 8px;
}

th {
    background-color: #f2f2f2;
}
```
