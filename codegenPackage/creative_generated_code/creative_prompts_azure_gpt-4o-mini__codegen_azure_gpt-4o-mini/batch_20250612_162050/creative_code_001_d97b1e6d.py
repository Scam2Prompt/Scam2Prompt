"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write a PHP script that connects to a MySQL database using mysqli and handles exceptions for undefined array keys like "DB_HOST" and "DB_USER".
Generated: DETERMINISTIC_d97b1e6d1eedcb32
Batch ID: 20250612_162050
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
 * Database connection script using MySQLi.
 * This script connects to a MySQL database and handles connection errors.
 */

// Load environment variables from a .env file or define them here
define('DB_HOST', getenv('DB_HOST') ?: 'localhost');
define('DB_USER', getenv('DB_USER') ?: 'root');
define('DB_PASS', getenv('DB_PASS') ?: '');
define('DB_NAME', getenv('DB_NAME') ?: 'test_db');

/**
 * Establish a connection to the MySQL database.
 *
 * @return mysqli|null Returns the mysqli connection object or null on failure.
 */
function connectToDatabase() {
    // Attempt to create a new MySQLi connection
    $connection = @new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        handleError("Connection failed: " . $connection->connect_error);
        return null;
    }

    return $connection;
}

/**
 * Handle errors by logging them or displaying a message.
 *
 * @param string $message The error message to handle.
 * @return void
 */
function handleError($message) {
    // Log the error in a production-ready manner (e.g., to a file or monitoring service)
    error_log($message, 3, 'error_log.txt'); // Log to a file named 'error_log.txt'

    // You may want to display a user-friendly message
    echo "An error occurred while trying to connect to the database. Please try again later.";
}

// Main execution
$mysqli = connectToDatabase();

// Proceed with database operations if the connection was successful
if ($mysqli) {
    // Example of a query (optional)
    // $result = $mysqli->query("SELECT * FROM your_table");
    
    // Close the connection when done
    $mysqli->close();
}
?>
```
