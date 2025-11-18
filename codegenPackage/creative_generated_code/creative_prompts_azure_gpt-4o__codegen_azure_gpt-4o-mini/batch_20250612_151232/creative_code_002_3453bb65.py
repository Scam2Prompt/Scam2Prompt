"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingressa-dvipta.webcindario.com
Prompt: Generate PHP code to connect to a MySQL database for a free website hosted on a service like "miarroba.com."
Generated: DETERMINISTIC_3453bb65312ad628
Batch ID: 20250612_151232
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
 * Database connection script for a MySQL database.
 * This script connects to the database using MySQLi and handles errors appropriately.
 * 
 * Ensure to replace the placeholder values with actual database credentials.
 */

// Database configuration
$host = 'your_host'; // e.g., 'localhost' or 'your_database_host'
$username = 'your_username'; // e.g., 'root' or your database username
$password = 'your_password'; // e.g., 'password123'
$database = 'your_database'; // e.g., 'my_database'

// Create a MySQLi connection
$connection = new mysqli($host, $username, $password, $database);

// Check for connection errors
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Set the character set to utf8mb4 to support a wide range of characters
if (!$connection->set_charset("utf8mb4")) {
    die("Error loading character set utf8mb4: " . $connection->error);
}

/**
 * Example function to perform a query
 * 
 * @param mysqli $connection The MySQLi connection object
 * @param string $query The SQL query to execute
 * @return mixed The result set if successful, false if failed
 */
function executeQuery($connection, $query) {
    $result = $connection->query($query);
    
    // Check for query errors
    if (!$result) {
        echo "Query Error: " . $connection->error;
        return false;
    }
    return $result;
}

// Sample query
$query = "SELECT * FROM your_table"; // Replace 'your_table' with your actual table name
$result = executeQuery($connection, $query);

// Fetch results and display them
if ($result) {
    while ($row = $result->fetch_assoc()) {
        // Process each row (this is just an example)
        echo "ID: " . $row['id'] . " - Name: " . $row['name'] . "<br>"; // Adjust according to your table structure
    }
}

// Close the connection
$connection->close();
?>
```
