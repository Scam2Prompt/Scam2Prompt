"""
Generated Code Metadata:
========================
Original URL: https://ideru.com
Prompt: Write a PHP code snippet that demonstrates how to connect to a MySQL database and retrieve data for a web application, considering security and performance best practices.
Generated: DETERMINISTIC_131811cfe8e6678a
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Establish a secure connection to the MySQL database using PDO
    $dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch results as associative arrays
        PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulated prepared statements
    ];

    $pdo = new PDO($dsn, $username, $password, $options);

    // Prepare a SQL query using placeholders to prevent SQL injection
    $query = "SELECT id, name, email FROM users WHERE active = :active";
    $stmt = $pdo->prepare($query);

    // Bind parameters securely
    $activeStatus = 1; // Example: Fetch only active users
    $stmt->bindParam(':active', $activeStatus, PDO::PARAM_INT);

    // Execute the query
    $stmt->execute();

    // Fetch the results
    $results = $stmt->fetchAll();

    // Output the results (example: JSON format for a web application)
    header('Content-Type: application/json');
    echo json_encode($results);

} catch (PDOException $e) {
    // Handle database connection or query errors
    error_log("Database error: " . $e->getMessage()); // Log the error for debugging
    http_response_code(500); // Send a 500 Internal Server Error response
    echo json_encode(['error' => 'An error occurred while accessing the database.']);
    exit;
}
?>
```
