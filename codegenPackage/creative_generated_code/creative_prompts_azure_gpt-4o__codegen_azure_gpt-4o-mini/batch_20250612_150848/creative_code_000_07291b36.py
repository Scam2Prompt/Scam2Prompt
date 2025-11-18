"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Write PHP code to integrate a PEAR library for database operations, referencing documentation from phpm.ru.
Generated: DETERMINISTIC_07291b36fdd72c8c
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure that the PEAR library is included in the include_path
require_once 'PEAR.php';
require_once 'DB.php';

/**
 * Class DatabaseHandler
 * A wrapper class for database operations using PEAR DB
 */
class DatabaseHandler {
    private $db;

    /**
     * Constructor to initialize the database connection
     *
     * @param string $dsn Data Source Name for the database connection
     * @throws Exception If connection fails
     */
    public function __construct($dsn) {
        // Establish a database connection
        $this->db = DB::connect($dsn);
        
        if (DB::isError($this->db)) {
            throw new Exception('Database connection failed: ' . $this->db->getMessage());
        }
    }

    /**
     * Method to execute a query
     *
     * @param string $query SQL query to be executed
     * @param array $params Parameters for the prepared statement
     * @return mixed Result set on success, or false on failure
     */
    public function executeQuery($query, $params = []) {
        // Prepare and execute the query
        $stmt = $this->db->prepare($query);
        
        if (DB::isError($stmt)) {
            throw new Exception('Query preparation failed: ' . $stmt->getMessage());
        }

        // Execute the statement with parameters
        $result = $stmt->execute($params);
        
        if (DB::isError($result)) {
            throw new Exception('Query execution failed: ' . $result->getMessage());
        }

        return $result;
    }

    /**
     * Method to fetch all results from a query
     *
     * @param string $query SQL query to be executed
     * @param array $params Parameters for the prepared statement
     * @return array Result set as an associative array
     */
    public function fetchAll($query, $params = []) {
        $result = $this->executeQuery($query, $params);
        
        // Fetch all results
        return $result->fetchAll(DB_FETCHMODE_ASSOC);
    }

    /**
     * Destructor to close the database connection
     */
    public function __destruct() {
        // Disconnect from the database
        if ($this->db) {
            $this->db->disconnect();
        }
    }
}

// Example usage:
// Define the DSN (Data Source Name) for the database
$dsn = 'mysql://username:password@localhost/database_name';

try {
    // Create an instance of DatabaseHandler
    $dbHandler = new DatabaseHandler($dsn);
    
    // Example query
    $result = $dbHandler->fetchAll('SELECT * FROM users WHERE active = ?', [1]);
    
    // Output the result
    print_r($result);
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo 'Error: ' . $e->getMessage();
}
?>
```
