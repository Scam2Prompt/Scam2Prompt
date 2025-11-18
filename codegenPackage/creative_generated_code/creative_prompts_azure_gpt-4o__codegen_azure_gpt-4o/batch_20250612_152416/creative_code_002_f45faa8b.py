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
// Database credentials
$host = 'localhost';        // Hostname of the database server
$dbname = 'your_database';  // Name of the database
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Table name to retrieve data from
$tableName = 'your_table';

try {
    // Establish a connection to the MySQL database using PDO
    $dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
    $pdo = new PDO($dsn, $username, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for error handling
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Set default fetch mode to associative array
    ]);

    // Prepare and execute the SQL query to fetch all rows from the table
    $query = "SELECT * FROM $tableName";
    $stmt = $pdo->prepare($query);
    $stmt->execute();

    // Fetch all results
    $results = $stmt->fetchAll();

    // Output the results in JSON format
    header('Content-Type: application/json');
    echo json_encode($results);

} catch (PDOException $e) {
    // Handle database connection or query errors
    error_log("Database error: " . $e->getMessage()); // Log the error for debugging
    http_response_code(500); // Set HTTP response status code to 500 (Internal Server Error)
    echo json_encode(['error' => 'Database connection or query failed']); // Return a JSON error message
}
?>
```

**Note**: Replace `your_database`, `your_username`, `your_password`, and `your_table` with your actual database details.
