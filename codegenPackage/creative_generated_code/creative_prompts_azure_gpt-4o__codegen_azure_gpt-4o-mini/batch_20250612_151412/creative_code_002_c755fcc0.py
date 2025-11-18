"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayuda-davivienda.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database for a free website hosted on platforms like miarroba.com.
Generated: DETERMINISTIC_c755fcc0ecfb224c
Batch ID: 20250612_151412
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
 * Database connection script
 * 
 * This script connects to a MySQL database using MySQLi.
 * Replace the placeholders with your actual database credentials.
 */

// Database configuration
$host = 'localhost'; // Host name, typically 'localhost'
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password
$dbname = 'your_database'; // Database name

// Create a connection using MySQLi
$connection = new mysqli($host, $username, $password, $dbname);

// Check for connection errors
if ($connection->connect_error) {
    // Log the error message for debugging
    error_log("Connection failed: " . $connection->connect_error);
    // Display a user-friendly message
    die("Connection to the database failed. Please try again later.");
}

/**
 * Function to safely execute a query
 * 
 * @param mysqli $connection The MySQLi connection object
 * @param string $query The SQL query to execute
 * @return mixed The result of the query or false on failure
 */
function executeQuery($connection, $query) {
    // Execute the query
    if ($result = $connection->query($query)) {
        return $result; // Return the result set
    } else {
        // Log the error message for debugging
        error_log("Query failed: " . $connection->error);
        return false; // Return false on failure
    }
}

// Example usage of the executeQuery function
$query = "SELECT * FROM your_table"; // Replace with your actual query
$result = executeQuery($connection, $query);

// Check if the query was successful and process the results
if ($result) {
    // Fetch all results as an associative array
    $data = $result->fetch_all(MYSQLI_ASSOC);
    
    // Output the fetched data (for demonstration purposes)
    foreach ($data as $row) {
        echo "Data: " . implode(", ", $row) . "<br>";
    }
    
    // Free result set
    $result->free();
}

// Close the database connection
$connection->close();
?>
```
