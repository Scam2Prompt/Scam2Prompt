"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that demonstrates the proper usage of mysqli::__construct() to connect to a database, ensuring to handle potential exceptions.
Generated: DETERMINISTIC_117e8aea2b6b2f6b
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
 * Database connection using mysqli with exception handling.
 */

// Database connection parameters
$host = 'localhost';
$username = 'db_user';
$password = 'secure_password';
$database = 'my_database';
$port = 3306; // Default MySQL port
$socket = null; // Default socket

try {
    // Create a new mysqli connection with error reporting enabled
    $mysqli = new mysqli($host, $username, $password, $database, $port, $socket);

    // Check connection
    if ($mysqli->connect_errno) {
        throw new RuntimeException(
            "Failed to connect to MySQL: " . $mysqli->connect_error
        );
    }

    // Set the character set to ensure proper encoding
    if (!$mysqli->set_charset('utf8mb4')) {
        throw new RuntimeException(
            "Error loading character set utf8mb4: " . $mysqli->error
        );
    }

    // Connection successful - perform database operations here
    // ...

    // Close the connection when done
    $mysqli->close();

} catch (RuntimeException $e) {
    // Log the error (in a real application, use a proper logging mechanism)
    error_log($e->getMessage());

    // Display a user-friendly message (in production, don't expose raw errors)
    echo "An error occurred while connecting to the database. Please try again later.";
    exit;
}
?>
```
