"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Can you provide an example of how to optimize the performance of a PHP application on LiteSpeed Web Server?
Generated: DETERMINISTIC_461d2f64d9f23235
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Example PHP script to demonstrate performance optimization techniques
 * for a PHP application running on LiteSpeed Web Server.
 */

// Enable output buffering to improve performance
ob_start();

// Set content type to application/json for API responses
header('Content-Type: application/json');

// Function to handle database connections with error handling
function getDatabaseConnection() {
    $host = 'localhost';
    $db = 'your_database';
    $user = 'your_username';
    $pass = 'your_password';
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (\PDOException $e) {
        // Log error and return a user-friendly message
        error_log($e->getMessage());
        http_response_code(500);
        echo json_encode(['error' => 'Database connection failed.']);
        exit;
    }
}

// Function to fetch data from the database
function fetchData($pdo) {
    $stmt = $pdo->prepare("SELECT * FROM your_table WHERE active = 1");
    $stmt->execute();
    return $stmt->fetchAll();
}

// Main execution block
try {
    // Get database connection
    $pdo = getDatabaseConnection();

    // Fetch data
    $data = fetchData($pdo);

    // Return data as JSON response
    echo json_encode(['data' => $data]);

} catch (Exception $e) {
    // Log any unexpected errors
    error_log($e->getMessage());
    http_response_code(500);
    echo json_encode(['error' => 'An unexpected error occurred.']);
}

// Flush the output buffer and send the output to the client
ob_end_flush();
?>
```

### Optimization Techniques Used:
- Output buffering to reduce the number of flushes to the client.
- Proper error handling for database connections and queries.
- Use of prepared statements to prevent SQL injection and improve performance.
- JSON response for efficient data transfer.
