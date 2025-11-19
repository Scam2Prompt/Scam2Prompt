"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskxx1.webcindario.com
Prompt: What are the best practices for developing a free website using PHP and MySQL?
Generated: DETERMINISTIC_16d914e9e8d5a978
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root'); // Database username
define('DB_PASS', 'password'); // Database password
define('DB_NAME', 'my_database'); // Database name

/**
 * Establish a connection to the MySQL database.
 *
 * @return mysqli The MySQLi connection object.
 * @throws Exception If the connection fails.
 */
function connectDB() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        throw new Exception('Database connection failed: ' . $connection->connect_error);
    }

    return $connection;
}

/**
 * Fetch all records from the specified table.
 *
 * @param mysqli $connection The MySQLi connection object.
 * @param string $table The name of the table to fetch records from.
 * @return array The fetched records.
 */
function fetchRecords($connection, $table) {
    $query = "SELECT * FROM $table";
    $result = $connection->query($query);

    // Check for query errors
    if (!$result) {
        throw new Exception('Query failed: ' . $connection->error);
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

/**
 * Render HTML for displaying records.
 *
 * @param array $records The records to display.
 */
function renderRecords($records) {
    if (empty($records)) {
        echo '<p>No records found.</p>';
        return;
    }

    echo '<table border="1">';
    echo '<tr><th>ID</th><th>Name</th><th>Email</th></tr>'; // Example headers

    foreach ($records as $record) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($record['id']) . '</td>'; // Assuming 'id' is a field
        echo '<td>' . htmlspecialchars($record['name']) . '</td>'; // Assuming 'name' is a field
        echo '<td>' . htmlspecialchars($record['email']) . '</td>'; // Assuming 'email' is a field
        echo '</tr>';
    }

    echo '</table>';
}

// Main execution block
try {
    $connection = connectDB();
    $records = fetchRecords($connection, 'users'); // Assuming 'users' is the table name
    renderRecords($records);
} catch (Exception $e) {
    // Handle exceptions and display an error message
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
} finally {
    // Close the database connection
    if (isset($connection)) {
        $connection->close();
    }
}
?>
```

### Key Points
- This code provides a basic structure for a PHP script that connects to a MySQL database, fetches records from a specified table, and displays them in an HTML table format.
- Error handling is implemented using exceptions to ensure any issues are caught and reported to the user.
- The code uses HTML escaping to prevent XSS attacks by sanitizing output.
