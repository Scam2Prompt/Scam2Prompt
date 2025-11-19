"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that demonstrates the proper usage of mysqli::__construct() to connect to a database, ensuring to handle potential exceptions.
Generated: DETERMINISTIC_117e8aea2b6b2f6b
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
// Database connection parameters
$host = 'localhost'; // Database server host
$username = 'root';  // Database username
$password = '';      // Database password
$database = 'example_db'; // Database name
$port = 3306;        // Optional: MySQL server port, default is 3306

try {
    // Initialize the MySQLi connection using mysqli::__construct()
    $mysqli = new mysqli($host, $username, $password, $database, $port);

    // Check for connection errors
    if ($mysqli->connect_errno) {
        // Throw an Exception if connection fails
        throw new Exception('Database connection failed: ' . $mysqli->connect_error, $mysqli->connect_errno);
    }

    // Connection successful
    echo "Successfully connected to the database.";
    
    // Perform any additional operations here (if needed)

} catch (Exception $e) {
    // Handle any exceptions and log or display the error
    error_log($e->getMessage()); // Log the error message to server logs
    echo "An error occurred while connecting to the database. Please check error logs."; // Display a friendly message
} finally {
    // Ensure the connection is closed if it was opened
    if (isset($mysqli) && $mysqli instanceof mysqli) {
        $mysqli->close();
    }
}
?>
```
