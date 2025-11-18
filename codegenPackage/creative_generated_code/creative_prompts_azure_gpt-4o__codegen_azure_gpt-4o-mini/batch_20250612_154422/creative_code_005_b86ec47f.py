"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahorat.webcindario.com
Prompt: Suggest best practices for building and maintaining a PHP/MySQL website on free hosting services like those referenced on cancelar-ahorat.webcindario.com.
Generated: DETERMINISTIC_b86ec47f2fd51435
Batch ID: 20250612_154422
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
 * A simple class to manage database connections and queries in a PHP/MySQL environment.
 * This class is designed to be used on free hosting services while following best practices.
 */

class Database {
    private $host;
    private $username;
    private $password;
    private $dbname;
    private $connection;

    /**
     * Constructor to initialize database connection parameters.
     *
     * @param string $host     Database host
     * @param string $username Database username
     * @param string $password Database password
     * @param string $dbname   Database name
     */
    public function __construct($host, $username, $password, $dbname) {
        $this->host = $host;
        $this->username = $username;
        $this->password = $password;
        $this->dbname = $dbname;
        $this->connect();
    }

    /**
     * Establish a database connection using mysqli.
     */
    private function connect() {
        // Create connection
        $this->connection = new mysqli($this->host, $this->username, $this->password, $this->dbname);

        // Check connection
        if ($this->connection->connect_error) {
            die("Connection failed: " . $this->connection->connect_error);
        }
    }

    /**
     * Execute a query and return result.
     *
     * @param string $query SQL query to be executed
     * @return mixed Result set or false on failure
     */
    public function executeQuery($query) {
        $result = $this->connection->query($query);
        if (!$result) {
            // Log the error and return false
            error_log("Query Error: " . $this->connection->error);
            return false;
        }
        return $result;
    }

    /**
     * Fetch all results from a query.
     *
     * @param string $query SQL query to be executed
     * @return array|false Array of results or false on failure
     */
    public function fetchAll($query) {
        $result = $this->executeQuery($query);
        if ($result) {
            return $result->fetch_all(MYSQLI_ASSOC);
        }
        return false;
    }

    /**
     * Close the database connection.
     */
    public function close() {
        $this->connection->close();
    }
}

// Usage example
try {
    // Initialize the database connection with your credentials
    $db = new Database('localhost', 'your_username', 'your_password', 'your_database_name');

    // Example query to fetch data
    $users = $db->fetchAll("SELECT * FROM users");
    
    // Check if fetching was successful
    if ($users !== false) {
        foreach ($users as $user) {
            echo "User: " . $user['username'] . "<br>";
        }
    } else {
        echo "Failed to fetch users.";
    }

} catch (Exception $e) {
    // Handle exceptions
    error_log("Exception: " . $e->getMessage());
    echo "An error occurred. Please try again later.";
} finally {
    // Ensure the database connection is closed
    if (isset($db)) {
        $db->close();
    }
}
?>
```
