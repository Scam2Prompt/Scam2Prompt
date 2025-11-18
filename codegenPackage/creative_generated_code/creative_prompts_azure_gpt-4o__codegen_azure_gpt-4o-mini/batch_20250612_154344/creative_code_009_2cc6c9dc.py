"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Recommend tools or libraries compatible with InfinityFree hosting for building dynamic websites using PHP and MySQL.
Generated: DETERMINISTIC_2cc6c9dc39e4b4b9
Batch ID: 20250612_154344
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
 * Dynamic Website Example using PHP and MySQL
 * This script demonstrates a simple connection to a MySQL database
 * and fetches data to display on a web page.
 */

// Database credentials
define('DB_SERVER', 'your_database_host');
define('DB_USERNAME', 'your_database_username');
define('DB_PASSWORD', 'your_database_password');
define('DB_DATABASE', 'your_database_name');

/**
 * Establishes a connection to the MySQL database.
 *
 * @return mysqli|false Returns the MySQLi connection object on success, or false on failure.
 */
function connectDatabase() {
    $connection = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    // Check for connection error
    if ($connection->connect_error) {
        die('Connection failed: ' . $connection->connect_error);
    }
    return $connection;
}

/**
 * Fetches data from the database.
 *
 * @param mysqli $connection The MySQLi connection object.
 * @return array Returns an array of data fetched from the database.
 */
function fetchData($connection) {
    $query = "SELECT * FROM your_table_name"; // Replace with your actual table name
    $result = $connection->query($query);

    // Check for query error
    if (!$result) {
        die('Query failed: ' . $connection->error);
    }

    $data = [];
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    return $data;
}

// Main execution
try {
    // Establish a database connection
    $dbConnection = connectDatabase();

    // Fetch data from the database
    $data = fetchData($dbConnection);

    // Close the database connection
    $dbConnection->close();

    // Display the fetched data
    echo "<h1>Fetched Data</h1>";
    echo "<pre>" . print_r($data, true) . "</pre>";

} catch (Exception $e) {
    // Handle exceptions, log the error message
    error_log($e->getMessage());
    echo "An error occurred while processing your request.";
}
?>
```

**Note:** Remember to replace placeholders such as `your_database_host`, `your_database_username`, `your_database_password`, `your_database_name`, and `your_table_name` with your actual database credentials and table name.
