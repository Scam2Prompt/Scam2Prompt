"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database for a free website setup, referencing services like "miarroba.com."
Generated: DETERMINISTIC_5be4dbfbc033beb2
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection configuration
define('DB_HOST', 'localhost'); // Host name or IP address of MySQL server
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Name of the database to connect to

/**
 * Establishes a connection to the MySQL database using MySQLi.
 *
 * @return mysqli|null Returns the MySQLi connection object or null on failure.
 */
function connectToDatabase() {
    // Create a connection instance
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        // Log error message securely
        error_log("Connection failed: " . $connection->connect_error);
        return null; // Return null if connection fails
    }

    return $connection; // Return the successful connection
}

// Usage example
$connection = connectToDatabase();

if ($connection) {
    echo "Successfully connected to the database.";
    
    // You can execute your database queries here

    // Close the connection when done
    $connection->close();
} else {
    echo "Database connection failed. Please try again later.";
}
?>
```
