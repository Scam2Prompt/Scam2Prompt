"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Write a PHP script to connect to a MySQL database using PDO, following the tutorial on phpm.ru.
Generated: DETERMINISTIC_1c84e4e0bf289b7a
Batch ID: 20250612_150848
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
 * Database connection script using PDO.
 * This script demonstrates how to connect securely to a MySQL database.
 */

// Database configuration
$host = 'localhost';        // Hostname or IP address of the database server
$dbName = 'your_database';  // Name of the database
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password
$charset = 'utf8mb4';       // Character set for encoding

try {
    // Create a DSN (Data Source Name) string for PDO
    $dsn = "mysql:host=$host;dbname=$dbName;charset=$charset";

    // PDO options for better performance and security
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for error handling
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Set default fetch mode to associative array
        PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulated prepares for security
    ];

    // Establish connection to the database using PDO
    $pdo = new PDO($dsn, $username, $password, $options);

    // Connection successful
    echo "Database connection established successfully.";
} catch (PDOException $e) {
    // Handle connection error
    echo "Database connection failed: " . $e->getMessage();
    exit; // Exit the script if an error occurs
}
?>
```
