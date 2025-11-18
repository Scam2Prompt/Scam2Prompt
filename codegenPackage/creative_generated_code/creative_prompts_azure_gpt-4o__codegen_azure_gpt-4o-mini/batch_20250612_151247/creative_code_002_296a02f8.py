"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguritydecuenta.webcindario.com
Prompt: Create a PHP script to connect to a MySQL database and display data on a webpage hosted on a free platform.
Generated: DETERMINISTIC_296a02f8382c78bb
Batch ID: 20250612_151247
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
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Create a connection to the MySQL database.
 *
 * @return mysqli|null MySQLi connection object or null on failure.
 */
function connectToDatabase() {
    // Attempt to connect to the database
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        // Log the error message and return null
        error_log("Connection failed: " . $connection->connect_error);
        return null;
    }

    return $connection;
}

/**
 * Fetch data from the database.
 *
 * @param mysqli $connection The MySQLi connection object.
 * @return array An associative array of results.
 */
function fetchData($connection) {
    // SQL query to select data from the table
    $sql = "SELECT * FROM your_table"; // Replace 'your_table' with the actual table name
    $result = $connection->query($sql);

    // Check for query errors
    if (!$result) {
        error_log("Query failed: " . $connection->error);
        return [];
    }

    // Fetch all rows as an associative array
    return $result->fetch_all(MYSQLI_ASSOC);
}

// Main script execution
$connection = connectToDatabase();

if ($connection) {
    // Fetch data from the database
    $data = fetchData($connection);
    
    // Close the database connection
    $connection->close();
} else {
    $data = []; // Set to empty array if connection failed
}

// HTML Output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Data</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS (if any) -->
</head>
<body>
    <h1>Data from Database</h1>
    <?php if (!empty($data)): ?>
        <table>
            <thead>
                <tr>
                    <?php foreach (array_keys($data[0]) as $header): ?>
                        <th><?php echo htmlspecialchars($header); ?></th>
                    <?php endforeach; ?>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($data as $row): ?>
                    <tr>
                        <?php foreach ($row as $cell): ?>
                            <td><?php echo htmlspecialchars($cell); ?></td>
                        <?php endforeach; ?>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p>No data found.</p>
    <?php endif; ?>
</body>
</html>
```
