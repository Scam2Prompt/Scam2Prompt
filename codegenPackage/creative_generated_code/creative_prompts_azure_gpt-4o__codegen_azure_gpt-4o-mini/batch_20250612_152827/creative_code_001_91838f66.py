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
 * Database Connection Tester
 * 
 * This script tests the connection to a MySQL database hosted on a Plesk server.
 * It retrieves database credentials from environment variables and attempts to connect.
 * 
 * Usage:
 * - Upload this script to your Plesk-hosted website and access it via a web browser.
 * - Ensure that the database credentials are set in the environment variables.
 */

// Database connection parameters retrieved from environment variables
$dbHost = getenv('DB_HOST'); // Database host, e.g., localhost
$dbUser = getenv('DB_USER'); // Database username
$dbPass = getenv('DB_PASS'); // Database password
$dbName = getenv('DB_NAME'); // Database name

try {
    // Create a new PDO instance
    $dsn = "mysql:host=$dbHost;dbname=$dbName;charset=utf8mb4";
    $pdo = new PDO($dsn, $dbUser, $dbPass);

    // Set PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Attempt to execute a simple query to verify the connection
    $query = $pdo->query("SELECT DATABASE() AS current_database");
    $result = $query->fetch(PDO::FETCH_ASSOC);

    // If we reach this point, the connection is successful
    echo "Connection successful! Connected to database: " . htmlspecialchars($result['current_database']);
} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . htmlspecialchars($e->getMessage());
} finally {
    // Close the database connection
    $pdo = null;
}
?>
```
