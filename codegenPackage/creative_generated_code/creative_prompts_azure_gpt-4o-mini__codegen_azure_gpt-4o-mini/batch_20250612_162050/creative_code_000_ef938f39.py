"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: How can I implement error handling for mysqli connections in PHP to avoid issues like "Access denied for user" and "Failed to parse IPv6 address"?
Generated: DETERMINISTIC_ef938f39d6c09788
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
/**
 * Database connection class using mysqli with error handling.
 */
class DatabaseConnection {
    private $connection;

    /**
     * Constructor to initialize the database connection.
     *
     * @param string $host The database host.
     * @param string $username The database username.
     * @param string $password The database password.
     * @param string $database The database name.
     */
    public function __construct($host, $username, $password, $database) {
        $this->connect($host, $username, $password, $database);
    }

    /**
     * Establish a connection to the MySQL database.
     *
     * @param string $host The database host.
     * @param string $username The database username.
     * @param string $password The database password.
     * @param string $database The database name.
     */
    private function connect($host, $username, $password, $database) {
        // Attempt to establish a connection
        $this->connection = new mysqli($host, $username, $password, $database);

        // Check for connection errors
        if ($this->connection->connect_error) {
            // Handle specific error cases
            switch ($this->connection->connect_errno) {
                case 1045: // Access denied for user
                    die("Error: Access denied for user '$username' on host '$host'.");
                case 2002: // Failed to connect to the server
                    die("Error: Unable to connect to the database server at '$host'. Check if the server is running.");
                case 11001: // Failed to parse IPv6 address
                    die("Error: Failed to parse IPv6 address for host '$host'.");
                default:
                    die("Error: Connection failed: " . $this->connection->connect_error);
            }
        }
        echo "Connected successfully to the database '$database'.";
    }

    /**
     * Close the database connection.
     */
    public function close() {
        if ($this->connection) {
            $this->connection->close();
            echo "Database connection closed.";
        }
    }

    /**
     * Get the current database connection.
     *
     * @return mysqli|null
     */
    public function getConnection() {
        return $this->connection;
    }
}

// Example usage
try {
    $db = new DatabaseConnection('localhost', 'username', 'password', 'database_name');
    // Perform database operations here...

} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage();
} finally {
    // Ensure the database connection is closed
    if (isset($db)) {
        $db->close();
    }
}
?>
```
