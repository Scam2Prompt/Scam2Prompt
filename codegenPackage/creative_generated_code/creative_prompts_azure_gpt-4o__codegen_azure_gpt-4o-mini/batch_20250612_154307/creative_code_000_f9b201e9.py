"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Write PHP code to connect to a MySQL database hosted on an InfinityFree server and retrieve data from a sample table.
Generated: DETERMINISTIC_f9b201e9cf9cbf59
Batch ID: 20250612_154307
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
 * Database connection configuration.
 */
define('DB_HOST', 'your_host'); // e.g., 'sqlXXX.epizy.com'
define('DB_USER', 'your_username'); // e.g., 'epiz_12345678'
define('DB_PASS', 'your_password'); // Your database password
define('DB_NAME', 'your_database_name'); // e.g., 'epiz_12345678_test'

// Function to establish a connection to the MySQL database
function getDatabaseConnection() {
    // Create a new mysqli instance
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }

    return $connection;
}

/**
 * Function to fetch data from the sample table.
 *
 * @return array|false Returns an array of results or false on failure.
 */
function fetchSampleData() {
    // Establish database connection
    $connection = getDatabaseConnection();
    
    // SQL query to retrieve data from the sample table
    $sql = "SELECT * FROM sample_table"; // Replace 'sample_table' with your actual table name
    
    // Execute the query
    $result = $connection->query($sql);
    
    // Check for query errors
    if (!$result) {
        echo "Query failed: " . $connection->error;
        $connection->close();
        return false;
    }

    // Fetch all results as an associative array
    $data = $result->fetch_all(MYSQLI_ASSOC);
    
    // Free result set and close the connection
    $result->free();
    $connection->close();
    
    return $data;
}

// Usage example
$data = fetchSampleData();
if ($data !== false) {
    // Output the retrieved data
    echo "<pre>";
    print_r($data);
    echo "</pre>";
} else {
    echo "Failed to retrieve data.";
}
?>
```
