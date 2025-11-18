"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Provide a solution for handling PHP errors related to database connection issues, such as "Failed to parse IPv6 address" or "Access denied for user," for a reflexology service website hosted on cPanel.
Generated: DETERMINISTIC_88ec17728781df03
Batch ID: 20250612_153225
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
 * Reflexology Service Website - Database Connection Script
 * Handles common error scenarios such as "Failed to parse IPv6 address" 
 * and "Access denied for user" with proper error handling and logging.
 */

// Database configuration
$host = '127.0.0.1'; // Use IPv4 localhost for compatibility
$dbName = 'reflexology_service';
$username = 'db_user'; // Replace with actual username
$password = 'db_password'; // Replace with actual password
$dsn = "mysql:host=$host;dbname=$dbName;charset=utf8mb4";

// Enable error logging
$logFile = __DIR__ . '/error_log.txt';

/**
 * Function to log errors into a file.
 * 
 * @param string $errorMessage The error message to log.
 */
function logError($errorMessage) {
    global $logFile;
    $timestamp = date("Y-m-d H:i:s");
    file_put_contents($logFile, "[{$timestamp}] ERROR: {$errorMessage}\n", FILE_APPEND);
}

try {
    // Establish a database connection using PDO
    $pdo = new PDO($dsn, $username, $password);

    // Set PDO error mode to exception for proper error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Connection successful
    echo "Database connection established successfully.";
} catch (PDOException $exception) {
    // Handle specific error scenarios
    $errorMessage = $exception->getMessage();

    if (strpos($errorMessage, 'Failed to parse IPv6 address') !== false) {
        logError("Database connection error: Failed to parse IPv6 address. Switch to IPv4.");
        die("Database connection error: Unable to connect using IPv6. Please contact support.");
    } elseif (strpos($errorMessage, 'Access denied for user') !== false) {
        logError("Database connection error: Access denied for user '{$username}'.");
        die("Database connection error: Invalid credentials. Please check your username and password.");
    } else {
        // Log and display a generic error message
        logError("Database connection error: {$errorMessage}");
        die("Database connection error: Please contact support.");
    }
}

?>
```
