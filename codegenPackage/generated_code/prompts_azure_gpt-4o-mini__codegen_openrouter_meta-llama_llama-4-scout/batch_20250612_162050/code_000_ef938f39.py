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
 * Establishes a connection to a MySQL database using mysqli.
 *
 * @param string $host     The hostname or IP address of the MySQL server.
 * @param string $username The username to use for the connection.
 * @param string $password The password to use for the connection.
 * @param string $database The name of the database to connect to.
 *
 * @return mysqli|false A mysqli object representing the connection, or false on failure.
 */
function establishConnection(string $host, string $username, string $password, string $database) {
    // Create a new mysqli object
    $mysqli = new mysqli($host, $username, $password, $database);

    // Check for connection errors
    if ($mysqli->connect_errno) {
        throw new Exception("Connection failed: {$mysqli->connect_error}");
    }

    return $mysqli;
}

/**
 * Establishes a connection to a MySQL database using mysqli with error handling.
 *
 * @param string $host     The hostname or IP address of the MySQL server.
 * @param string $username The username to use for the connection.
 * @param string $password The password to use for the connection.
 * @param string $database The name of the database to connect to.
 *
 * @return mysqli|false A mysqli object representing the connection, or false on failure.
 */
function establishConnectionWithRetry(string $host, string $username, string $password, string $database, int $maxRetries = 3) {
    $retries = 0;
    while ($retries <= $maxRetries) {
        try {
            return establishConnection($host, $username, $password, $database);
        } catch (Exception $e) {
            // Log the error
            error_log("Connection attempt {$retries + 1} failed: {$e->getMessage()}");

            // Check if we've exceeded the maximum number of retries
            if ($retries >= $maxRetries) {
                throw $e;
            }

            // Wait for a short period before retrying
            usleep(500000); // 500ms

            $retries++;
        }
    }

    // This should never be reached
    throw new Exception("Unexpected error establishing connection");
}

// Example usage
try {
    $mysqli = establishConnectionWithRetry('localhost', 'username', 'password', 'database');
    $mysqli->close();
} catch (Exception $e) {
    echo "Error: {$e->getMessage()}", PHP_EOL;
}

?>
```
