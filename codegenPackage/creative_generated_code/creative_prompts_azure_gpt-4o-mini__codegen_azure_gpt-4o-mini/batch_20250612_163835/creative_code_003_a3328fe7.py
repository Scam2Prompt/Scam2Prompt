"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: What are the advantages of using PHP and MySQL for web development?
Generated: DETERMINISTIC_a3328fe7297d8fc8
Batch ID: 20250612_163835
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
 * Database connection script using PDO with PHP and MySQL
 * This script demonstrates the advantages of PHP and MySQL for web development.
 * Advantages include ease of use, a large community, and robust performance.
 */

class Database {
    private $host = 'localhost'; // Database host
    private $db_name = 'your_database'; // Database name
    private $username = 'your_username'; // Database username
    private $password = 'your_password'; // Database password
    private $conn; // Connection variable

    /**
     * Establish a database connection using PDO
     * 
     * @return PDO|null Returns PDO instance or null on failure
     */
    public function connect() {
        try {
            // Create a new PDO instance
            $this->conn = new PDO("mysql:host={$this->host};dbname={$this->db_name}", $this->username, $this->password);
            // Set the PDO error mode to exception for error handling
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $this->conn;
        } catch (PDOException $e) {
            // Handle connection error
            echo "Connection failed: " . $e->getMessage();
            return null;
        }
    }

    /**
     * Fetch all records from a specific table
     * 
     * @param string $table The name of the table to fetch records from
     * @return array|null Returns an array of records or null on failure
     */
    public function fetchAll($table) {
        try {
            $stmt = $this->conn->prepare("SELECT * FROM $table");
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Handle query error
            echo "Query failed: " . $e->getMessage();
            return null;
        }
    }
}

// Usage example
$db = new Database();
$conn = $db->connect();

if ($conn) {
    $records = $db->fetchAll('your_table');
    if ($records) {
        echo "<pre>";
        print_r($records); // Display fetched records in a readable format
        echo "</pre>";
    }
}
?>
```
