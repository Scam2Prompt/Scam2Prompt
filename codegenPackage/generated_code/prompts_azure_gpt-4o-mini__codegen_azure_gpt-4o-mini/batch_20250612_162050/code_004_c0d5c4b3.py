"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: How can I modify my PHP code to properly handle mysqli_sql_exception when connecting to a database with potentially undefined parameters?
Generated: DETERMINISTIC_c0d5c4b39c2c5ce5
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
 * Database connection class using MySQLi with exception handling.
 */
class Database {
    private $connection;

    /**
     * Constructor to initialize the database connection.
     *
     * @param string $host     The database host.
     * @param string $username The database username.
     * @param string $password The database password.
     * @param string $dbname   The database name.
     * @throws mysqli_sql_exception If the connection fails.
     */
    public function __construct($host, $username, $password, $dbname) {
        // Check if parameters are defined and not empty
        if (empty($host) || empty($username) || empty($dbname)) {
            throw new InvalidArgumentException('Host, username, and database name must be provided.');
        }

        // Attempt to establish a connection to the database
        try {
            $this->connection = new mysqli($host, $username, $password, $dbname);

            // Check for connection errors
            if ($this->connection->connect_error) {
                throw new mysqli_sql_exception('Connection failed: ' . $this->connection->connect_error);
            }
        } catch (mysqli_sql_exception $e) {
            // Handle the exception and log the error message
            error_log($e->getMessage());
            throw $e; // Re-throw the exception for further handling
        }
    }

    /**
     * Get the database connection.
     *
     * @return mysqli The MySQLi connection object.
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

// Example usage
try {
    $db = new Database('localhost', 'username', 'password', 'database_name');
    $connection = $db->getConnection();
    // Perform database operations here...

} catch (mysqli_sql_exception $e) {
    // Handle the database connection error
    echo 'Database connection error: ' . $e->getMessage();
} catch (InvalidArgumentException $e) {
    // Handle invalid argument error
    echo 'Invalid argument: ' . $e->getMessage();
} finally {
    // Ensure the connection is closed if it was established
    if (isset($db)) {
        $db->closeConnection();
    }
}
?>
```
