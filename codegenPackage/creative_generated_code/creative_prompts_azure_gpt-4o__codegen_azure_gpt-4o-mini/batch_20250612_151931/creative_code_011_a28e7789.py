"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Write a ThinkPHP configuration file for database connections using `config/database.php` as a reference from the Moonpad website.
Generated: DETERMINISTIC_a28e77897917fa86
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// config/database.php

// Database configuration settings for the ThinkPHP framework
return [
    // Default database connection
    'default' => [
        'type' => 'mysql', // Database type
        'hostname' => '127.0.0.1', // Database server address
        'database' => 'your_database_name', // Database name
        'username' => 'your_username', // Database username
        'password' => 'your_password', // Database password
        'hostport' => '3306', // Database port
        'charset' => 'utf8mb4', // Character set
        'prefix' => 'tp_', // Database table prefix
        'debug' => true, // Enable debug mode
    ],

    // Additional database connections can be defined here
    'connections' => [
        'read' => [
            'type' => 'mysql',
            'hostname' => '127.0.0.1',
            'database' => 'your_database_name_read',
            'username' => 'your_username',
            'password' => 'your_password',
            'hostport' => '3306',
            'charset' => 'utf8mb4',
            'prefix' => 'tp_',
            'debug' => true,
        ],
        'write' => [
            'type' => 'mysql',
            'hostname' => '127.0.0.1',
            'database' => 'your_database_name_write',
            'username' => 'your_username',
            'password' => 'your_password',
            'hostport' => '3306',
            'charset' => 'utf8mb4',
            'prefix' => 'tp_',
            'debug' => true,
        ],
    ],

    // Connection options
    'options' => [
        // PDO Options
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for database errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch data as associative arrays
        PDO::ATTR_EMULATE_PREPARES => false, // Use real prepared statements
    ],

    // Define the database connection settings for multiple database support
    'multiple' => true, // Enable multiple database connections
];

// Note: Remember to replace 'your_database_name', 'your_username', and 'your_password' 
// with your actual database credentials before deploying the application.

```
