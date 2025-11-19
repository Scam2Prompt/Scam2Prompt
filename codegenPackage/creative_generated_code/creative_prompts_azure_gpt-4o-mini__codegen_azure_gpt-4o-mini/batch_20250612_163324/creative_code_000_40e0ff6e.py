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
/**
 * Database configuration settings
 */
define('DB_SERVER', 'localhost'); // Database server
define('DB_USERNAME', 'your_username'); // Database username
define('DB_PASSWORD', 'your_password'); // Database password
define('DB_DATABASE', 'your_database'); // Database name

/**
 * Function to create a MySQL database connection
 *
 * @return mysqli $connection - MySQLi connection object
 * @throws Exception if the connection fails
 */
function createDatabaseConnection() {
    // Create a connection
    $connection = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
    
    // Check for connection errors
    if ($connection->connect_error) {
        throw new Exception('Connection failed: ' . $connection->connect_error);
    }
    
    return $connection;
}

/**
 * Function to create a new database if it doesn't exist
 *
 * @param mysqli $connection - MySQLi connection object
 * @param string $dbName - Name of the database to create
 * @throws Exception if the database creation fails
 */
function createDatabase($connection, $dbName) {
    $sql = "CREATE DATABASE IF NOT EXISTS `$dbName`";
    
    if ($connection->query($sql) === TRUE) {
        echo "Database '$dbName' created successfully or already exists.<br>";
    } else {
        throw new Exception('Error creating database: ' . $connection->error);
    }
}

/**
 * Main execution block
 */
try {
    // Establish database connection
    $connection = createDatabaseConnection();
    
    // Create database
    createDatabase($connection, DB_DATABASE);
    
    // Close the connection
    $connection->close();
} catch (Exception $e) {
    // Log the error message (in production, you might want to log this to a file)
    error_log($e->getMessage());
    echo 'An error occurred. Please try again later.';
}
?>
```
