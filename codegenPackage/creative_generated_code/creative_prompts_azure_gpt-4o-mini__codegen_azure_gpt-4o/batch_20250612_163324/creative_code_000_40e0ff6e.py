"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Generate a code snippet to set up a MySQL database using PHP on a Linux web hosting environment.
Generated: DETERMINISTIC_40e0ff6ec78db5b7
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration constants for database connection
define("DB_HOST", "localhost");     // Database host, e.g., localhost
define("DB_USER", "your_username"); // MySQL user (replace 'your_username' with your actual username)
define("DB_PASS", "your_password"); // MySQL password (replace 'your_password' with your actual password)
define("DB_NAME", "your_database"); // Database name (replace 'your_database' with your desired database name)

// Create a connection to MySQL
$connection = new mysqli(DB_HOST, DB_USER, DB_PASS);

// Check the connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// SQL query to create the database
$sqlCreateDB = "CREATE DATABASE IF NOT EXISTS " . DB_NAME;
if ($connection->query($sqlCreateDB) === TRUE) {
    echo "Database '" . DB_NAME . "' created successfully.";
} else {
    echo "Error creating database: " . $connection->error;
}

// Select the database
$connection->select_db(DB_NAME);

// SQL query to create a sample table (optional)
$sqlCreateTable = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if ($connection->query($sqlCreateTable) === TRUE) {
    echo "Table 'users' created successfully.";
} else {
    echo "Error creating table: " . $connection->error;
}

// Close the database connection
$connection->close();
?>
```
