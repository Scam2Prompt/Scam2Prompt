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
// +----------------------------------------------------------------------
// | ThinkPHP Script Example for Database Connection and Query Handling
// +----------------------------------------------------------------------
// | Author: Professional Developer
// | License: MIT
// +----------------------------------------------------------------------

// Ensure the script is being run in a ThinkPHP environment
// Assume ThinkPHP has already been installed via Composer

// Import ThinkPHP Db class
use think\Db;

// Define database configuration
$config = [
    // Database type (e.g., mysql)
    'type'        => 'mysql',
    // Server address
    'hostname'    => '127.0.0.1',
    // Database name
    'database'    => 'example_db',
    // Username
    'username'    => 'root',
    // Password
    'password'    => 'password123',
    // Port
    'hostport'    => '3306',
    // Charset
    'charset'     => 'utf8',
    // Prefix for table names
    'prefix'      => 'tp_',
];

try {
    // Establish the database connection using ThinkPHP Db
    Db::setConfig($config);

    // Perform a basic query: Fetch all rows from a table
    $users = Db::table('tp_users')->select();

    // Check if the query returned results
    if ($users) {
        // Loop through and display the results
        foreach ($users as $user) {
            echo 'User ID: ' . $user['id'] . ' | Name: ' . $user['name'] . '<br>';
        }
    } else {
        echo 'No users found.';
    }
} catch (Exception $e) {
    // Handle connection or query errors
    echo 'Error: ' . $e->getMessage();
}

?>
```
