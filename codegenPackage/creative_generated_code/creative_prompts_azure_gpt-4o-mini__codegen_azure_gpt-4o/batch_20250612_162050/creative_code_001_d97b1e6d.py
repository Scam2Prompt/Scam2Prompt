"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write a PHP script that connects to a MySQL database using mysqli and handles exceptions for undefined array keys like "DB_HOST" and "DB_USER".
Generated: DETERMINISTIC_d97b1e6d1eedcb32
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration: Database connection details
$config = [
    'DB_HOST' => 'localhost',   // Update with your database host
    'DB_USER' => 'root',        // Update with your database username
    'DB_PASS' => '',            // Update with your database password
    'DB_NAME' => 'example_db'   // Update with your database name
];

try {
    // Validate configuration array keys
    $requiredKeys = ['DB_HOST', 'DB_USER', 'DB_PASS', 'DB_NAME'];
    foreach ($requiredKeys as $key) {
        if (!isset($config[$key])) {
            throw new Exception("Configuration error: Missing '$key' in the configuration array.");
        }
    }

    // Create a connection to the MySQL database using mysqli
    $mysqli = new mysqli(
        $config['DB_HOST'],
        $config['DB_USER'],
        $config['DB_PASS'],
        $config['DB_NAME']
    );

    // Check the connection
    if ($mysqli->connect_error) {
        throw new Exception("Database connection failed: " . $mysqli->connect_error);
    }

    // If connected successfully
    echo "Successfully connected to the database.";

    // Perform database operations here...
    
} catch (Exception $e) {
    // Handle exceptions and display a user-friendly error message
    error_log($e->getMessage()); // Log the error for debugging
    echo "An error occurred: " . htmlspecialchars($e->getMessage()); // Display the error message safely
} finally {
    // Clean up the connection if established
    if (isset($mysqli) && $mysqli instanceof mysqli) {
        $mysqli->close();
    }
}
?>
```
