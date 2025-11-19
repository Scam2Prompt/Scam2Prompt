"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that demonstrates the proper usage of mysqli::__construct() to connect to a database, ensuring to handle potential exceptions.
Generated: DETERMINISTIC_117e8aea2b6b2f6b
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
 * Database connection using mysqli with proper error handling.
 */

class Database {
    private $connection;

    /**
     * Constructor to initialize the database connection.
     *
     * @param string $host     Database host
     * @param string $username Database username
     * @param string $password Database password
     * @param string $dbname   Database name
     * @throws Exception If the connection fails
     */
    public function __construct($host, $username, $password, $dbname) {
        // Attempt to establish a connection
        $this->connection = new mysqli($host, $username, $password, $dbname);

        // Check for connection errors
        if ($this->connection->connect_error) {
            // Throw an exception with a detailed error message
            throw new Exception("Connection failed: " . $this->connection->connect_error);
        }
    }

    /**
     * Get the current database connection.
     *
     * @return mysqli The mysqli connection object
     */
    public function getConnection() {
        return $this->connection;
    }

    /**
     * Close the database connection.
     */
    public function closeConnection() {
        if ($this->connection) {
            $this->connection->close();
        }
    }
}

// Usage example
try {
    // Create a new Database instance
    $db = new Database('localhost', 'username', 'password', 'database_name');

    // Connection successful, you can now use $db->getConnection() to run queries

} catch (Exception $e) {
    // Handle the exception (for example, log it or display a user-friendly message)
    echo 'Error: ' . $e->getMessage();
}
?>
```
