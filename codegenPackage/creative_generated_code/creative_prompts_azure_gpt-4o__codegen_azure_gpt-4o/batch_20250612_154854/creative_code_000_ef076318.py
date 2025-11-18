"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2acnmzzlink.webcindario.com
Prompt: Write PHP code to create a simple webpage that connects to a MySQL database, referencing free hosting services like the one mentioned on "miarroba.com."
Generated: DETERMINISTIC_ef07631889aa7d5d
Batch ID: 20250612_154854
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
// Database configuration file

// Database credentials
define('DB_HOST', 'your-database-host'); // Replace with your host (e.g., "sql.miarrorba.com")
define('DB_NAME', 'your-database-name'); // Replace with your database name
define('DB_USER', 'your-username');     // Replace with your username
define('DB_PASS', 'your-password');     // Replace with your password
```

```php
<?php
// index.php
// Main webpage script

// Include the configuration file
require_once 'config.php';

// Function to connect to the database
function connectToDatabase() {
    try {
        // Create a new PDO instance for the database connection
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Set default fetch mode to associative array
            PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation of prepared statements
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Display a user-friendly error message
        die("Database connection failed: " . htmlspecialchars($e->getMessage()));
    }
}

// Connect to the database
$db = connectToDatabase();

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #fafafa;
        }
        h1 {
            color: #333;
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
            text-align: left;
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Simple PHP Webpage</h1>
    <p>This page connects to a MySQL database and retrieves data.</p>

    <?php
    // Example query to fetch data from the database
    try {
        $query = $db->query("SELECT id, name FROM example_table"); // Replace 'example_table' with your actual table name
        $results = $query->fetchAll();

        // Check if there are any rows returned
        if ($results) {
            echo "<table>";
            echo "<tr><th>ID</th><th>Name</th></tr>";
            foreach ($results as $row) {
                echo "<tr><td>" . htmlspecialchars($row['id']) . "</td><td>" . htmlspecialchars($row['name']) . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "<p>No data found in the database.</p>";
        }
    } catch (PDOException $e) {
        // Handle query errors
        echo "<p>Error retrieving data: " . htmlspecialchars($e->getMessage()) . "</p>";
    }
    ?>
</body>
</html>
```
