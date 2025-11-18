"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmuskcrypto.webcindario.com
Prompt: Generate PHP code to connect to a MySQL database and retrieve all entries from a "users" table.
Generated: DETERMINISTIC_aa88ab49ddc69bf8
Batch ID: 20250612_151847
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
 * Database configuration
 */
define('DB_HOST', 'localhost'); // Database host, typically localhost
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Function to connect to the MySQL database
 *
 * @return mysqli|null Returns a MySQLi connection object or null on failure
 */
function connectToDatabase() {
    // Create a new MySQLi instance
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        // Log error message
        error_log('Database connection error: ' . $connection->connect_error);
        return null; // Return null on failure
    }

    return $connection; // Return the connection object on success
}

/**
 * Function to retrieve all entries from the "users" table
 *
 * @param mysqli $connection The MySQLi connection object
 * @return array|null Returns an array of users or null on failure
 */
function getAllUsers($connection) {
    // SQL query to select all users
    $sql = "SELECT * FROM users";
    
    // Execute the query and get the result
    if ($result = $connection->query($sql)) {
        // Fetch all users as an associative array
        $users = $result->fetch_all(MYSQLI_ASSOC);
        $result->free(); // Free result set
        return $users; // Return users array
    } else {
        // Log error if the query fails
        error_log('Query error: ' . $connection->error);
        return null; // Return null on failure
    }
}

// Main execution block
$connection = connectToDatabase(); // Establish database connection

if ($connection) {
    $users = getAllUsers($connection); // Retrieve all users

    if ($users !== null) {
        // Output the users in JSON format
        header('Content-Type: application/json'); // Set content type
        echo json_encode($users); // Return JSON encoded user data
    } else {
        // Handle case where no users were retrieved
        http_response_code(500); // Internal Server Error status
        echo json_encode(['error' => 'Failed to retrieve users.']);
    }

    // Close the database connection
    $connection->close();
} else {
    // Handle database connection failure
    http_response_code(500); // Internal Server Error status
    echo json_encode(['error' => 'Failed to connect to the database.']);
}
?>
```
