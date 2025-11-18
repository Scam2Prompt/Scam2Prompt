"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: Create a PHP script to check MySQL database connectivity and troubleshoot common issues on free hosting platforms.
Generated: DETERMINISTIC_79bf3e0f972d0ff3
Batch ID: 20250612_154441
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
 * Script to check MySQL database connectivity and troubleshoot common issues.
 * 
 * This script attempts to connect to a MySQL database using provided credentials
 * and outputs helpful messages to troubleshoot common issues.
 * 
 * Usage:
 * Update the database credentials below with your specific values.
 */

// Database configuration
$dbHost = 'localhost'; // Usually 'localhost' or the server IP
$dbUser = 'your_username'; // Replace with your database username
$dbPassword = 'your_password'; // Replace with your database password
$dbName = 'your_database'; // Replace with your database name

// Check PHP MySQL extension
if (!function_exists('mysqli_connect')) {
    die("ERROR: The MySQLi extension is not installed on this server. Contact your hosting provider.");
}

// Attempt to establish a connection to the database
$connection = @mysqli_connect($dbHost, $dbUser, $dbPassword, $dbName);

// Handle connection errors
if (!$connection) {
    $error = mysqli_connect_error();
    switch (mysqli_connect_errno()) {
        case 1045:
            die("ERROR: Invalid username/password. Please check your database credentials.");
        case 2002:
            die("ERROR: Unable to connect to the database server. Verify the hostname or server IP.");
        case 1049:
            die("ERROR: Unknown database name. Ensure the database exists and the name is correct.");
        default:
            die("ERROR: Could not connect to the database. Details: " . $error);
    }
}

// Check if the database is selected properly
if (!mysqli_select_db($connection, $dbName)) {
    die("ERROR: Database selected is invalid. Verify the database name.");
}

// If we reach here, the connection was successful
echo "SUCCESS: Database connection established successfully.";

// Optional: Check for permissions (basic query test)
$query = "SHOW TABLES"; // Query to list tables
$result = @mysqli_query($connection, $query);

if (!$result) {
    die("ERROR: Connection established, but unable to execute queries. Check user permissions.");
}

// Output tables (if any) to verify the connection
echo "Tables in the database:\n";
while ($row = mysqli_fetch_row($result)) {
    echo "- " . $row[0] . "\n";
}

// Clean up resources
mysqli_free_result($result);
mysqli_close($connection);

?>
```
