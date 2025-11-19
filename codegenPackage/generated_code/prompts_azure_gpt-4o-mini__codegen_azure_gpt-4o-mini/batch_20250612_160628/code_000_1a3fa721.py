"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Generate a PHP script that utilizes the ThinkPHP framework to handle database connections and queries, specifically focusing on the `think/Db.php` file.
Generated: DETERMINISTIC_1a3fa721c1a35fcf
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Import the ThinkPHP framework
require 'vendor/autoload.php';

use think\Db;
use think\Exception;

// Database configuration
$config = [
    'type'     => 'mysql', // Database type
    'hostname' => '127.0.0.1', // Database host
    'database' => 'your_database_name', // Database name
    'username' => 'your_username', // Database username
    'password' => 'your_password', // Database password
    'hostport' => '3306', // Database port
    'charset'  => 'utf8', // Database charset
    'prefix'   => 'tp_', // Table prefix
];

// Set up the database connection
try {
    Db::setConfig($config);
    $db = Db::connect();
} catch (Exception $e) {
    // Handle connection errors
    die('Database connection failed: ' . $e->getMessage());
}

/**
 * Function to fetch all records from a specified table
 *
 * @param string $table The name of the table to query
 * @return array|false Returns an array of records or false on failure
 */
function fetchAllRecords($table) {
    global $db; // Use the global database connection

    try {
        // Fetch all records from the specified table
        $results = $db->table($table)->select();
        return $results;
    } catch (Exception $e) {
        // Handle query errors
        error_log('Query failed: ' . $e->getMessage());
        return false;
    }
}

/**
 * Function to insert a new record into a specified table
 *
 * @param string $table The name of the table to insert into
 * @param array $data The data to insert
 * @return int|false Returns the ID of the inserted record or false on failure
 */
function insertRecord($table, $data) {
    global $db; // Use the global database connection

    try {
        // Insert the new record into the specified table
        $id = $db->table($table)->insertGetId($data);
        return $id;
    } catch (Exception $e) {
        // Handle insertion errors
        error_log('Insertion failed: ' . $e->getMessage());
        return false;
    }
}

// Example usage
$tableName = 'tp_users'; // Example table name

// Fetch all records
$records = fetchAllRecords($tableName);
if ($records !== false) {
    echo "Records fetched successfully:\n";
    print_r($records);
} else {
    echo "Failed to fetch records.\n";
}

// Insert a new record
$newUser = [
    'username' => 'new_user',
    'email'    => 'new_user@example.com',
    'password' => password_hash('secure_password', PASSWORD_DEFAULT),
];
$insertedId = insertRecord($tableName, $newUser);
if ($insertedId !== false) {
    echo "New user inserted with ID: $insertedId\n";
} else {
    echo "Failed to insert new user.\n";
}
?>
```
