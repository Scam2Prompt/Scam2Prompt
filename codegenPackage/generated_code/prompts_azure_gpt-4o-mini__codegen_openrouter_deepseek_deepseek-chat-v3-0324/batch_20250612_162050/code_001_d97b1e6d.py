"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Write a PHP script that connects to a MySQL database using mysqli and handles exceptions for undefined array keys like "DB_HOST" and "DB_USER".
Generated: DETERMINISTIC_d97b1e6d1eedcb32
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * PHP script to connect to a MySQL database using mysqli with proper error handling.
 * Handles exceptions for undefined array keys in database configuration.
 */

// Database configuration array with default values
$dbConfig = [
    'DB_HOST' => 'localhost',
    'DB_USER' => 'root',
    'DB_PASS' => '',
    'DB_NAME' => 'test_db'
];

try {
    // Check if required configuration keys exist
    if (!isset($dbConfig['DB_HOST']) || !isset($dbConfig['DB_USER']) || 
        !isset($dbConfig['DB_NAME'])) {
        throw new RuntimeException('Missing required database configuration parameters');
    }

    // Create database connection
    $mysqli = new mysqli(
        $dbConfig['DB_HOST'],
        $dbConfig['DB_USER'],
        $dbConfig['DB_PASS'] ?? '', // Use empty string if password not set
        $dbConfig['DB_NAME']
    );

    // Check connection
    if ($mysqli->connect_error) {
        throw new RuntimeException('Database connection failed: ' . $mysqli->connect_error);
    }

    // Set charset to utf8mb4 for proper encoding support
    if (!$mysqli->set_charset('utf8mb4')) {
        throw new RuntimeException('Error setting charset: ' . $mysqli->error);
    }

    // Connection successful - you can perform database operations here
    echo "Connected successfully to database: " . $dbConfig['DB_NAME'];

    // Close connection when done (this would normally be in a function that uses the connection)
    $mysqli->close();

} catch (RuntimeException $e) {
    // Log the error (in production, you would log to a file or monitoring system)
    error_log($e->getMessage());
    
    // Display user-friendly error message
    echo "An error occurred while connecting to the database. Please try again later.";
    exit(1);
}
?>
```
