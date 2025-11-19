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
// Database connection parameters
$host = 'localhost'; // Database host
$username = 'root';  // Database username
$password = '';      // Database password
$database = 'example_db'; // Database name

try {
    // Create a new mysqli instance and establish a connection
    $mysqli = new mysqli($host, $username, $password, $database);

    // Check for connection errors
    if ($mysqli->connect_error) {
        throw new Exception('Connection failed: ' . $mysqli->connect_error);
    }

    // Connection successful
    echo "Database connection established successfully.";

    // Perform database operations here...

} catch (Exception $e) {
    // Handle exceptions and display error message
    error_log($e->getMessage()); // Log the error message
    echo "An error occurred while connecting to the database. Please try again later.";
} finally {
    // Close the connection if it was successfully established
    if (isset($mysqli) && $mysqli instanceof mysqli) {
        $mysqli->close();
    }
}
?>
```
