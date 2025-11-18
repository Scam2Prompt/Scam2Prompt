"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validaciondavi.webcindario.com
Prompt: Write PHP code to set up a basic MySQL database for a free website hosted on a platform like miarroba.com.
Generated: DETERMINISTIC_bf3e363b313943ba
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Database configuration for setting up a MySQL database.
 */

// Database configuration constants
define('DB_HOST', 'localhost'); // Database host, typically 'localhost'
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Function to create a MySQL database connection.
 *
 * @return mysqli|false Returns the MySQLi connection object on success, or false on failure.
 */
function createDatabaseConnection() {
    // Create a new connection
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die('Connection failed: ' . $connection->connect_error);
    }

    return $connection;
}

/**
 * Function to create a new database if it doesn't exist.
 *
 * @param mysqli $connection The MySQLi connection object.
 * @param string $dbName The name of the database to create.
 * @return void
 */
function createDatabase($connection, $dbName) {
    // SQL statement to create a database
    $sql = "CREATE DATABASE IF NOT EXISTS $dbName";

    // Execute the query and check for errors
    if ($connection->query($sql) === TRUE) {
        echo "Database '$dbName' created successfully.\n";
    } else {
        echo "Error creating database: " . $connection->error . "\n";
    }
}

/**
 * Function to create a sample table within the specified database.
 *
 * @param mysqli $connection The MySQLi connection object.
 * @return void
 */
function createSampleTable($connection) {
    // SQL statement to create a sample table
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    // Execute the query and check for errors
    if ($connection->query($sql) === TRUE) {
        echo "Table 'users' created successfully.\n";
    } else {
        echo "Error creating table: " . $connection->error . "\n";
    }
}

// Main execution
$dbConnection = createDatabaseConnection();
createDatabase($dbConnection, DB_NAME);
$dbConnection->select_db(DB_NAME); // Select the newly created database 
createSampleTable($dbConnection);

// Close the database connection
$dbConnection->close();
?>
```

**Note:** Make sure to replace `'your_username'`, `'your_password'`, and `'your_database'` with actual credentials and database name before running the code.
