"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Generate a PHP script that utilizes the ThinkPHP framework to handle database connections and queries, specifically focusing on the `think/Db.php` file.
Generated: DETERMINISTIC_1a3fa721c1a35fcf
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Import the ThinkPHP Db class
use think\Db;

// Define a class to handle database operations
class DatabaseHandler
{
    protected $db;

    // Constructor to initialize the database connection
    public function __construct()
    {
        try {
            // Connect to the database using ThinkPHP's Db class
            $this->db = Db::connect([
                'type'     => 'mysql',
                'hostname' => '127.0.0.1',
                'database' => 'your_database',
                'username' => 'your_username',
                'password' => 'your_password',
                'hostport' => '3306',
                'charset'  => 'utf8',
                'prefix'   => 'tp_',
            ]);
        } catch (\Exception $e) {
            // Handle connection errors
            die('Database connection failed: ' . $e->getMessage());
        }
    }

    // Method to fetch all records from a specified table
    public function fetchAll($tableName)
    {
        try {
            // Fetch all records from the specified table
            return $this->db->table($tableName)->select();
        } catch (\Exception $e) {
            // Handle query errors
            die('Query failed: ' . $e->getMessage());
        }
    }

    // Method to insert a new record into a specified table
    public function insertRecord($tableName, $data)
    {
        try {
            // Insert the data into the specified table
            return $this->db->table($tableName)->insert($data);
        } catch (\Exception $e) {
            // Handle query errors
            die('Insert failed: ' . $e->getMessage());
        }
    }

    // Method to update an existing record in a specified table
    public function updateRecord($tableName, $data, $condition)
    {
        try {
            // Update the record in the specified table based on the condition
            return $this->db->table($tableName)->where($condition)->update($data);
        } catch (\Exception $e) {
            // Handle query errors
            die('Update failed: ' . $e->getMessage());
        }
    }

    // Method to delete a record from a specified table
    public function deleteRecord($tableName, $condition)
    {
        try {
            // Delete the record from the specified table based on the condition
            return $this->db->table($tableName)->where($condition)->delete();
        } catch (\Exception $e) {
            // Handle query errors
            die('Delete failed: ' . $e->getMessage());
        }
    }
}

// Example usage
// Create an instance of the DatabaseHandler
$dbHandler = new DatabaseHandler();

// Fetch all records from the 'users' table
$users = $dbHandler->fetchAll('users');
print_r($users);

// Insert a new user into the 'users' table
$dbHandler->insertRecord('users', ['name' => 'John Doe', 'email' => 'john@example.com']);

// Update a user's information
$dbHandler->updateRecord('users', ['email' => 'john.doe@example.com'], ['name' => 'John Doe']);

// Delete a user from the 'users' table
$dbHandler->deleteRecord('users', ['name' => 'John Doe']);
?>
```
