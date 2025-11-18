"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and retrieve data from a specific table.
Generated: DETERMINISTIC_f45faa8b2d925d36
Batch ID: 20250612_152416
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
 * This script connects to a MySQL database and retrieves data from a specific table.
 * 
 * @package DatabaseConnection
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASSWORD', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name
define('TABLE_NAME', 'your_table'); // Table name to retrieve data from

/**
 * Connect to MySQL database
 *
 * @return mysqli|null Returns a mysqli object on success, or null on failure
 */
function connectToDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        error_log("Connection failed: " . $connection->connect_error);
        return null;
    }

    return $connection;
}

/**
 * Retrieve data from the specified table
 *
 * @param mysqli $connection The MySQLi connection object
 * @return array|false Returns an associative array of results or false on failure
 */
function fetchData($connection) {
    $sql = "SELECT * FROM " . TABLE_NAME;
    $result = $connection->query($sql);

    // Check for query errors
    if (!$result) {
        error_log("Query error: " . $connection->error);
        return false;
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

// Main execution
$databaseConnection = connectToDatabase();

if ($databaseConnection) {
    $data = fetchData($databaseConnection);
    
    // Check if data retrieval was successful
    if ($data !== false) {
        // Output the retrieved data in JSON format
        header('Content-Type: application/json');
        echo json_encode($data);
    } else {
        echo json_encode(["error" => "Failed to retrieve data"]);
    }

    // Close the database connection
    $databaseConnection->close();
} else {
    echo json_encode(["error" => "Failed to connect to the database"]);
}
?>
```
