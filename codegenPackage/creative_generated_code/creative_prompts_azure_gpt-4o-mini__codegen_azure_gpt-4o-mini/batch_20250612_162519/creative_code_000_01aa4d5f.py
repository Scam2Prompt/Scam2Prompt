"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Generate a PHP script to set up a database connection using MySQL for a web application hosted on IDN Hosting.
Generated: DETERMINISTIC_01aa4d5f94936701
Batch ID: 20250612_162519
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
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Create a database connection
 */
function createDatabaseConnection()
{
    // Create a new mysqli instance
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        // Log error and terminate script
        error_log("Connection failed: " . $connection->connect_error);
        die("Connection failed: " . $connection->connect_error);
    }

    return $connection;
}

/**
 * Close the database connection
 *
 * @param mysqli $connection The database connection to close
 */
function closeDatabaseConnection($connection)
{
    if ($connection instanceof mysqli) {
        $connection->close();
    }
}

// Example usage
$databaseConnection = createDatabaseConnection();

// Your database operations go here

// Close the database connection
closeDatabaseConnection($databaseConnection);
?>
```
