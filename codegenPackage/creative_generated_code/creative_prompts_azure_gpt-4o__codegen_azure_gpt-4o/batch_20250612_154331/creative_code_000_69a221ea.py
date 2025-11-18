"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giacotex.cl
Prompt: Write a PHP script for a Linux hosting environment to connect to a MySQL database, ensuring compatibility with hosting services in Chile.
Generated: DETERMINISTIC_69a221ea825e9520
Batch ID: 20250612_154331
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
 * Database Connection Script
 * 
 * This script establishes a secure connection to a MySQL database 
 * hosted in a Linux hosting environment (compatible with hosting services in Chile).
 * 
 * Best practices are followed, including proper error handling and support for UTF-8.
 */

// Set database connection credentials
$db_host = 'localhost'; // Use '127.0.0.1' for better compatibility in some hosting environments
$db_username = 'your_username'; // Replace with your database username
$db_password = 'your_password'; // Replace with your database password
$db_name = 'your_database_name'; // Replace with your database name

// Establish connection using MySQLi (improved extension)
$mysqli = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check for connection errors
if ($mysqli->connect_error) {
    // Log error message to server logs
    error_log("Database connection failed: " . $mysqli->connect_error);

    // Display a generic error message to the user
    die("There was an issue connecting to the database. Please try again later.");
}

// Set the character set to UTF-8 for proper encoding support
if (!$mysqli->set_charset("utf8")) {
    // Log error message to server logs
    error_log("Error setting character set UTF-8: " . $mysqli->error);

    // Display a generic error message to the user
    die("There was an issue setting the character encoding. Please try again later.");
}

// Connection is successful
echo "Database connection established successfully.";

/**
 * Close the connection when done (optional for short-lived scripts)
 * Uncomment the line below if needed for cleanup at the end of the script:
 */
// $mysqli->close();
?>
```
