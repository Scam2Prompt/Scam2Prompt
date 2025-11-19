"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that demonstrates the proper usage of mysqli::__construct() to connect to a database, ensuring to handle potential exceptions.
Generated: DETERMINISTIC_117e8aea2b6b2f6b
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
 * Database connection class using mysqli.
 */
class DatabaseConnection
{
    private $host;
    private $username;
    private $password;
    private $database;
    private $mysqli;

    /**
     * Constructor to initialize database connection properties.
     *
     * @param string $host     The hostname or IP address of the database server.
     * @param string $username The username to use for the connection.
     * @param string $password The password to use for the connection.
     * @param string $database The name of the database to connect to.
     */
    public function __construct($host, $username, $password, $database)
    {
        $this->host = $host;
        $this->username = $username;
        $this->password = $password;
        $this->database = $database;
    }

    /**
     * Establish a connection to the database.
     *
     * @return bool True if the connection is successful, false otherwise.
     */
    public function connect()
    {
        try {
            // Attempt to establish a connection to the database.
            $this->mysqli = new mysqli($this->host, $this->username, $this->password, $this->database);

            // Check for connection errors.
            if ($this->mysqli->connect_errno) {
                throw new Exception("Connection failed: " . $this->mysqli->connect_error);
            }

            // Connection successful.
            return true;
        } catch (Exception $e) {
            // Handle any exceptions that occur during connection.
            echo "Error connecting to database: " . $e->getMessage() . PHP_EOL;
            return false;
        }
    }

    /**
     * Close the database connection.
     */
    public function close()
    {
        if (isset($this->mysqli) && $this->mysqli instanceof mysqli) {
            $this->mysqli->close();
        }
    }
}

// Example usage.
$databaseHost = 'localhost';
$databaseUsername = 'your_username';
$databasePassword = 'your_password';
$databaseName = 'your_database';

$connection = new DatabaseConnection($databaseHost, $databaseUsername, $databasePassword, $databaseName);

if ($connection->connect()) {
    echo "Connected to database successfully." . PHP_EOL;

    // Perform database operations here...

    $connection->close();
} else {
    echo "Failed to connect to database." . PHP_EOL;
}

?>
```
