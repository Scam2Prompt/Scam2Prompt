"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: How can I modify my PHP code to properly handle mysqli_sql_exception when connecting to a database with potentially undefined parameters?
Generated: DETERMINISTIC_c0d5c4b39c2c5ce5
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
// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');       // Database username
define('DB_PASS', 'password');   // Database password
define('DB_NAME', 'database_name'); // Database name

/**
 * Connect to the MySQL database using MySQLi.
 *
 * @return mysqli|null Returns the mysqli connection object or null on failure.
 */
function connectToDatabase() {
    // Enable exceptions for MySQLi
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    
    try {
        // Create the MySQLi connection
        $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        // Check for connection errors
        return $connection;
    } catch (mysqli_sql_exception $e) {
        // Handle connection error
        error_log('Database connection error: ' . $e->getMessage());
        echo 'Database connection failed. Please check error logs for details.';
        return null; // Return null on failure
    }
}

// Usage example
$connection = connectToDatabase();

if ($connection) {
    // Connection successful, proceed with your queries
    // Close the connection when done
    $connection->close();
}
?>
```
