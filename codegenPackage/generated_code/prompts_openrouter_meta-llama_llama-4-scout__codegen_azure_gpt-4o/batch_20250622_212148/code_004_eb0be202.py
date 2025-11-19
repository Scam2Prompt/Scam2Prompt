"""
Generated Code Metadata:
========================
Original URL: https://grupo-virtual.webcindario.com
Prompt: "Write a PHP script to connect to a MySQL database for a personal website."
Generated: DETERMINISTIC_eb0be202faa30ee7
Batch ID: 20250622_212148
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
$dbName = 'personal_website'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance to connect to the database
    $dsn = "mysql:host=$host;dbname=$dbName;charset=utf8mb4";
    $pdo = new PDO($dsn, $username, $password);

    // Set PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Set default fetch mode to associative array
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    // Connection successful
    echo "Database connection established successfully.";
} catch (PDOException $e) {
    // Handle connection errors
    error_log("Database connection failed: " . $e->getMessage()); // Log the error
    echo "An error occurred while connecting to the database. Please try again later.";
    exit; // Terminate script execution
}

// Example query to test the connection (optional)
// Uncomment the following lines to test a simple query
/*
try {
    $stmt = $pdo->query("SELECT NOW() AS current_time");
    $result = $stmt->fetch();
    echo "Current time from database: " . $result['current_time'];
} catch (PDOException $e) {
    error_log("Query failed: " . $e->getMessage());
    echo "An error occurred while executing the query.";
}
*/

// Close the connection (optional, as PHP automatically closes it at the end of the script)
$pdo = null;
?>
```
