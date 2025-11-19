"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erecargaspe.webcindario.com
Prompt: Can you provide a code example for connecting PHP to a MySQL database for a free website?
Generated: DETERMINISTIC_76d84d5723ba741e
Batch ID: 20250612_162347
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
 * Database connection script.
 * This script connects to a MySQL database using PDO.
 * It handles connection errors and provides feedback.
 */

// Database configuration
$host = 'localhost';     // Database host
$db   = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4';    // Character set for the database connection

// Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// PDO options
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for error handling
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch associative arrays
    PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation for prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "Database connection successful!"; // Success message
} catch (PDOException $e) {
    // Handle connection errors
    echo "Database connection failed: " . $e->getMessage();
}
?>
```
