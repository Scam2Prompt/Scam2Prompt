"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: How can I modify my PHP code to properly handle mysqli_sql_exception when connecting to a database with potentially undefined parameters?
Generated: DETERMINISTIC_c0d5c4b39c2c5ce5
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

// Enable exceptions for mysqli_sql_exception
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

try {
    // Database configuration - replace with your own values
    $host = getenv('DB_HOST') ?: 'localhost'; // Default to 'localhost' if not defined
    $username = getenv('DB_USERNAME') ?: 'root'; // Default to 'root' if not defined
    $password = getenv('DB_PASSWORD') ?: ''; // Default to empty string if not defined
    $dbname = getenv('DB_NAME') ?: 'test'; // Default to 'test' if not defined

    // Establish connection to the database
    $connection = new mysqli($host, $username, $password, $dbname);

    // If successful, connection is established
    echo "Database connection established successfully.";

} catch (mysqli_sql_exception $e) {
    // Handle database connection errors gracefully
    error_log("Database connection error: " . $e->getMessage());
    http_response_code(500); // Send HTTP 500 Internal Server Error response
    echo "An error occurred while connecting to the database. Please try again later.";
} finally {
    // Clean up resources if the connection exists
    if (isset($connection) && $connection instanceof mysqli) {
        $connection->close();
    }
}

?>
```
