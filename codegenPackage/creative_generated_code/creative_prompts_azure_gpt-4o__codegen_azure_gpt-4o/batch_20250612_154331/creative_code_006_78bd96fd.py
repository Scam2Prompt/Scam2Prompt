"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundacionbuenaventura.cl
Prompt: Generate PHP code for connecting to a MySQL database hosted on a Linux server in Chile.
Generated: DETERMINISTIC_78bd96fd62aeb113
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection script for MySQL on a Linux server

// Configuration settings for the database
define('DB_HOST', 'your_server_ip_or_hostname'); // Replace with the server's IP or hostname
define('DB_PORT', '3306'); // Default MySQL port
define('DB_NAME', 'your_database_name'); // Replace with the name of your database
define('DB_USER', 'your_database_user'); // Replace with your database username
define('DB_PASSWORD', 'your_database_password'); // Replace with your database password

try {
    // Create a new PDO instance for database connection
    $dsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME . ";charset=utf8mb4";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for error handling
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch results as associative arrays
        PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation of prepared statements
    ];

    // Establish the connection
    $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, $options);

    // If the connection is successful, display a success message
    echo "Database connection established successfully!";
} catch (PDOException $e) {
    // Handle connection errors
    error_log("Database connection error: " . $e->getMessage()); // Log the error for debugging
    echo "Failed to connect to the database. Please contact the administrator."; // Display a user-friendly message
    exit;
}

// Example query to test the connection (optional)
// $stmt = $pdo->query("SELECT * FROM your_table_name LIMIT 1"); // Replace with your query
// $result = $stmt->fetchAll(); // Fetch the result
// print_r($result); // Print the result (for debugging)

?>
```
