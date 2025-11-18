"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Generate PHP code that can be used to test database connections on a Plesk-hosted website.
Generated: DETERMINISTIC_91838f6626cbd22f
Batch ID: 20250612_152827
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
 * Database Connection Test Script
 * 
 * This script is used to test database connections on a Plesk-hosted website.
 * Ensure you update the configuration settings before running.
 */

// Configuration settings
$dbHost = 'localhost'; // Database host (e.g., 'localhost', '127.0.0.1')
$dbName = 'your_database_name'; // Replace with your database name
$dbUser = 'your_database_user'; // Replace with your database username
$dbPass = 'your_database_password'; // Replace with your database password
$dbPort = 3306; // Default MySQL port is 3306

try {
    // Create a new PDO instance for database connection
    $dsn = "mysql:host=$dbHost;port=$dbPort;dbname=$dbName;charset=utf8mb4";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Set default fetch mode to associative array
        PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation of prepared statements
    ];

    $pdo = new PDO($dsn, $dbUser, $dbPass, $options);

    // If connection is successful, output a success message
    echo "Database connection successful!";
} catch (PDOException $e) {
    // Catch any errors and display a user-friendly message
    echo "Database connection failed: " . htmlspecialchars($e->getMessage());
}
?>
```
