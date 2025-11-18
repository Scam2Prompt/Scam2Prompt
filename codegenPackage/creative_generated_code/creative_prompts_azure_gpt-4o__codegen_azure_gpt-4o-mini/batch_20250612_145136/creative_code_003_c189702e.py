"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Write a PHP script to manage MySQL databases for a hosting plan that supports unlimited databases, as outlined in the PROFESSIONAL hosting plan on the Megh iTech website.
Generated: DETERMINISTIC_c189702e2bbe3214
Batch ID: 20250612_145136
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
 * DatabaseManager class to manage MySQL databases for a hosting plan
 * that supports unlimited databases.
 */
class DatabaseManager {
    private $connection;

    /**
     * Constructor to initialize the database connection.
     *
     * @param string $host     Database host.
     * @param string $user     Database username.
     * @param string $password Database password.
     * @param string $dbname   Database name (optional).
     */
    public function __construct($host, $user, $password, $dbname = null) {
        // Establish a connection to the MySQL database
        $this->connection = new mysqli($host, $user, $password, $dbname);

        // Check for connection errors
        if ($this->connection->connect_error) {
            die("Connection failed: " . $this->connection->connect_error);
        }
    }

    /**
     * Create a new database.
     *
     * @param string $dbname Name of the new database.
     * @return bool True on success, false on failure.
     */
    public function createDatabase($dbname) {
        $sql = "CREATE DATABASE " . $this->connection->real_escape_string($dbname);
        if ($this->connection->query($sql) === TRUE) {
            return true;
        } else {
            error_log("Error creating database: " . $this->connection->error);
            return false;
        }
    }

    /**
     * Drop an existing database.
     *
     * @param string $dbname Name of the database to drop.
     * @return bool True on success, false on failure.
     */
    public function dropDatabase($dbname) {
        $sql = "DROP DATABASE " . $this->connection->real_escape_string($dbname);
        if ($this->connection->query($sql) === TRUE) {
            return true;
        } else {
            error_log("Error dropping database: " . $this->connection->error);
            return false;
        }
    }

    /**
     * List all databases.
     *
     * @return array List of database names.
     */
    public function listDatabases() {
        $databases = [];
        $result = $this->connection->query("SHOW DATABASES");
        if ($result) {
            while ($row = $result->fetch_assoc()) {
                $databases[] = $row['Database'];
            }
        } else {
            error_log("Error fetching databases: " . $this->connection->error);
        }
        return $databases;
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
    // Initialize the DatabaseManager with connection details
    $dbManager = new DatabaseManager('localhost', 'username', 'password');

    // Create a new database
    if ($dbManager->createDatabase('new_database')) {
        echo "Database created successfully.\n";
    } else {
        echo "Failed to create database.\n";
    }

    // List all databases
    $databases = $dbManager->listDatabases();
    echo "Databases: " . implode(", ", $databases) . "\n";

    // Drop a database
    if ($dbManager->dropDatabase('new_database')) {
        echo "Database dropped successfully.\n";
    } else {
        echo "Failed to drop database.\n";
    }

} catch (Exception $e) {
    error_log("An error occurred: " . $e->getMessage());
} finally {
    // Close the connection
    $dbManager->closeConnection();
}
?>
```
