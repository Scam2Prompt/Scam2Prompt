"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Create a PHP script that interacts with a MySQL database using PEAR libraries.
Generated: DETERMINISTIC_2fbef771f7193172
Batch ID: 20250622_212723
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
 * MySQL Database Interaction Script using PEAR
 */

// Configuration
$dbHost = 'localhost';
$dbUsername = 'your_username';
$dbPassword = 'your_password';
$dbName = 'your_database';

// Initialize PEAR DB library
require_once 'DB.php';

// Establish database connection
function connectToDatabase($dbHost, $dbUsername, $dbPassword, $dbName) {
    $dsn = "mysql://$dbUsername:$dbPassword@$dbHost/$dbName";
    $db =& DB::connect($dsn);
    
    if (PEAR::isError($db)) {
        die($db->getMessage());
    }
    
    return $db;
}

// Perform a query on the database
function performQuery($db, $query) {
    $result =& $db->query($query);
    
    if (PEAR::isError($result)) {
        die($result->getMessage());
    }
    
    return $result;
}

// Main function
function main() {
    // Connect to database
    $db = connectToDatabase($GLOBALS['dbHost'], $GLOBALS['dbUsername'], $GLOBALS['dbPassword'], $GLOBALS['dbName']);
    
    // Example query
    $query = "SELECT * FROM your_table";
    
    try {
        // Perform query
        $result = performQuery($db, $query);
        
        // Fetch and display results
        while ($row = $result->fetchRow(DB_FETCHMODE_ASSOC)) {
            print_r($row);
            echo "\n";
        }
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage();
    } finally {
        // Close database connection
        $db->disconnect();
    }
}

// Run main function
main();

?>
```
