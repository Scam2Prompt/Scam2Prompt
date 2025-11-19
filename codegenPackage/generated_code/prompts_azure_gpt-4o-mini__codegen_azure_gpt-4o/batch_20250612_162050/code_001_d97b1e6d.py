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
// Enable error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration array
$config = [
    'DB_HOST' => 'localhost', // Database host
    'DB_USER' => 'root',      // Database username
    'DB_PASS' => '',          // Database password
    'DB_NAME' => 'test_db'    // Database name
];

try {
    // Check if all required keys exist in the configuration array
    $requiredKeys = ['DB_HOST', 'DB_USER', 'DB_PASS', 'DB_NAME'];
    foreach ($requiredKeys as $key) {
        if (!array_key_exists($key, $config)) {
            throw new Exception("Missing required configuration key: $key");
        }
    }

    // Create a new MySQLi connection
    $mysqli = new mysqli(
        $config['DB_HOST'],
        $config['DB_USER'],
        $config['DB_PASS'],
        $config['DB_NAME']
    );

    // Check for connection errors
    if ($mysqli->connect_error) {
        throw new Exception("Connection failed: " . $mysqli->connect_error);
    }

    // If connection is successful
    echo "Connected successfully to the database.";

    // Close the connection when done
    $mysqli->close();
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "Error: " . $e->getMessage();
    // Optionally log the error to a file for production use
    // error_log($e->getMessage(), 3, '/path/to/error.log');
}
?>
```
