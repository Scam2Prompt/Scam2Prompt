"""
Generated Code Metadata:
========================
Original URL: https://cryptogive.rf.gd
Prompt: Generate a code snippet in PHP to connect to a database hosted on iFastNet Web Hosting, assuming the hosting plan includes multiple versions of PHP.
Generated: DETERMINISTIC_f7466a23cc25567a
Batch ID: 20250622_212427
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
 * Database Connection Class
 *
 * This class handles connections to a database hosted on iFastNet Web Hosting.
 *
 * @author [Your Name]
 */

class DatabaseConnection
{
    /**
     * Hostname or IP address of the database server
     * @var string
     */
    private $host;

    /**
     * Database username
     * @var string
     */
    private $username;

    /**
     * Database password
     * @var string
     */
    private $password;

    /**
     * Database name
     * @var string
     */
    private $database;

    /**
     * PDO object
     * @var PDO
     */
    private $pdo;

    /**
     * Constructor
     *
     * @param string $host     Hostname or IP address of the database server
     * @param string $username Database username
     * @param string $password Database password
     * @param string $database Database name
     */
    public function __construct($host, $username, $password, $database)
    {
        $this->host     = $host;
        $this->username = $username;
        $this->password = $password;
        $this->database = $database;
    }

    /**
     * Establish a connection to the database
     *
     * @return bool True if connected, false otherwise
     */
    public function connect()
    {
        try {
            // Create a DSN (Data Source Name) string
            $dsn = "mysql:host={$this->host};dbname={$this->database};charset=utf8mb4";

            // Set PDO options
            $options = [
                PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES   => false,
            ];

            // Create a PDO object
            $this->pdo = new PDO($dsn, $this->username, $this->password, $options);

            return true;
        } catch (PDOException $e) {
            // Log the error
            error_log("Database connection failed: " . $e->getMessage());

            return false;
        }
    }

    /**
     * Close the database connection
     */
    public function close()
    {
        $this->pdo = null;
    }

    /**
     * Execute a SQL query
     *
     * @param string $sql    SQL query
     * @param array  $params Query parameters
     *
     * @return PDOStatement
     */
    public function execute($sql, $params = [])
    {
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute($params);

            return $stmt;
        } catch (PDOException $e) {
            // Log the error
            error_log("Query execution failed: " . $e->getMessage());

            return null;
        }
    }
}

// Example usage
$database = new DatabaseConnection(
    'localhost', // or your host
    'your_username',
    'your_password',
    'your_database'
);

if ($database->connect()) {
    $stmt = $database->execute("SELECT * FROM your_table");
    $rows = $stmt->fetchAll();

    foreach ($rows as $row) {
        print_r($row);
    }

    $database->close();
} else {
    echo "Failed to connect to database.";
}
```
