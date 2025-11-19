"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayuda-davivienda.webcindario.com
Prompt: What resources are available for creating a free website with PHP and MySQL, as referenced on ayuda-davivienda.webcindario.com?
Generated: DETERMINISTIC_9017574d5752e3ee
Batch ID: 20250612_163928
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
 * Simple example of a PHP and MySQL website setup.
 * This script connects to a MySQL database and fetches data.
 * 
 * Requirements:
 * - PHP >= 7.0
 * - MySQL database
 * - A web server (e.g., Apache, Nginx)
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'username');   // Database username
define('DB_PASS', 'password');   // Database password
define('DB_NAME', 'database_name'); // Database name

/**
 * Connect to MySQL database
 *
 * @return mysqli|null Returns the mysqli connection object or null on failure
 */
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        // Log error message
        error_log("Connection failed: " . $connection->connect_error);
        return null;
    }
    
    return $connection;
}

/**
 * Fetch data from a specific table
 *
 * @param mysqli $connection The database connection
 * @param string $table The name of the table to fetch data from
 * @return array|null Returns an array of results or null on failure
 */
function fetchData($connection, $table) {
    // Prepare the SQL statement
    $sql = "SELECT * FROM " . $connection->real_escape_string($table);
    $result = $connection->query($sql);

    // Check for query errors
    if (!$result) {
        error_log("Query error: " . $connection->error);
        return null;
    }

    // Fetch data
    $data = [];
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }

    return $data;
}

// Main execution block
$connection = connectDatabase();

if ($connection) {
    $data = fetchData($connection, 'your_table_name');

    if ($data !== null) {
        // Output data as JSON
        header('Content-Type: application/json');
        echo json_encode($data);
    } else {
        // Output error message
        echo json_encode(['error' => 'Failed to retrieve data.']);
    }

    // Close the connection
    $connection->close();
} else {
    // Output error message for connection failure
    echo json_encode(['error' => 'Database connection error.']);
}
?>
```
