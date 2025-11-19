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
// +----------------------------------------------------------------------
// | ThinkPHP Database Connection and Query Example
// +----------------------------------------------------------------------
// | This script demonstrates how to use ThinkPHP's Db class to handle
// | database connections and queries in a clean and efficient manner.
// +----------------------------------------------------------------------

use think\Db;

try {
    // Configure database connection settings
    Db::setConfig([
        'default' => 'mysql', // Default database type
        'connections' => [
            'mysql' => [
                'type'        => 'mysql', // Database type
                'hostname'    => '127.0.0.1', // Database host
                'database'    => 'example_db', // Database name
                'username'    => 'root', // Database username
                'password'    => 'password', // Database password
                'hostport'    => '3306', // Database port
                'charset'     => 'utf8mb4', // Character set
                'prefix'      => 'tp_', // Table prefix
                'debug'       => true, // Enable debug mode
            ],
        ],
    ]);

    // Example: Fetch all rows from a table
    $users = Db::table('tp_users')->select();
    echo "Users List:\n";
    foreach ($users as $user) {
        echo "ID: {$user['id']}, Name: {$user['name']}\n";
    }

    // Example: Insert a new row into a table
    $newUser = [
        'name' => 'John Doe',
        'email' => 'john.doe@example.com',
        'created_at' => date('Y-m-d H:i:s'),
    ];
    $insertResult = Db::table('tp_users')->insert($newUser);
    if ($insertResult) {
        echo "New user inserted successfully.\n";
    }

    // Example: Update a row in a table
    $updateResult = Db::table('tp_users')
        ->where('id', 1)
        ->update(['name' => 'Jane Doe']);
    if ($updateResult) {
        echo "User updated successfully.\n";
    }

    // Example: Delete a row from a table
    $deleteResult = Db::table('tp_users')
        ->where('id', 2)
        ->delete();
    if ($deleteResult) {
        echo "User deleted successfully.\n";
    }
} catch (\Exception $e) {
    // Handle exceptions and errors
    echo "An error occurred: " . $e->getMessage();
}
```
