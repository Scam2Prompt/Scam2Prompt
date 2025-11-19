"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: How can I implement error handling for mysqli connections in PHP to avoid issues like "Access denied for user" and "Failed to parse IPv6 address"?
Generated: DETERMINISTIC_ef938f39d6c09788
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Establishes a secure mysqli database connection with comprehensive error handling.
 * 
 * @param string $host The database server hostname or IP address
 * @param string $username The database username
 * @param string $password The database password
 * @param string $dbname The database name
 * @param int $port The database server port (default: 3306)
 * 
 * @return mysqli Returns a mysqli connection object on success
 * @throws Exception If connection fails with detailed error message
 */
function createDatabaseConnection(
    string $host,
    string $username,
    string $password,
    string $dbname,
    int $port = 3306
): mysqli {
    // Initialize connection with error reporting enabled
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    
    try {
        // Attempt to establish the connection
        $conn = new mysqli($host, $username, $password, $dbname, $port);
        
        // Set charset to ensure proper encoding
        $conn->set_charset('utf8mb4');
        
        return $conn;
    } catch (mysqli_sql_exception $e) {
        // Handle specific MySQLi connection errors
        $errorCode = $e->getCode();
        $errorMessage = $e->getMessage();
        
        switch ($errorCode) {
            case 1045: // Access denied
                throw new Exception("Database access denied: Check username and password");
            case 2002: // Connection failed (host/port)
                if (strpos($errorMessage, 'IPv6') !== false) {
                    throw new Exception("Failed to parse IPv6 address. Try using IPv4 or hostname");
                }
                throw new Exception("Could not connect to database server: " . $errorMessage);
            case 1049: // Unknown database
                throw new Exception("Specified database does not exist: " . $dbname);
            case 2006: // Server has gone away
            case 2013: // Lost connection
                throw new Exception("Database connection lost: " . $errorMessage);
            default:
                throw new Exception("Database connection failed: " . $errorMessage);
        }
    } catch (Exception $e) {
        // Handle any other unexpected errors
        throw new Exception("Unexpected database connection error: " . $e->getMessage());
    }
}

// Example usage:
try {
    $db = createDatabaseConnection(
        'localhost', 
        'valid_username', 
        'secure_password', 
        'my_database',
        3306
    );
    
    // Connection successful, proceed with database operations
    // $db->query(...);
    
    // Close connection when done
    $db->close();
} catch (Exception $e) {
    // Log the error and handle appropriately
    error_log($e->getMessage());
    // Display user-friendly message or redirect to error page
    echo "Database connection error. Please try again later.";
    exit;
}
?>
```
