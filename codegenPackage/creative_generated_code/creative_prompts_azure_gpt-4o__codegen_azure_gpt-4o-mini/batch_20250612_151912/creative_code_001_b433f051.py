"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergiffcrypto.webcindario.com
Prompt: Recommend a PHP library for managing MySQL database queries efficiently, and provide an example of its usage.
Generated: DETERMINISTIC_b433f05161cc5480
Batch ID: 20250612_151912
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
 * This example demonstrates how to use the PDO (PHP Data Objects) extension in PHP 
 * for managing MySQL database queries efficiently.
 *
 * PDO provides a uniform interface for accessing different databases and is 
 * the recommended way to interact with databases in PHP.
 */

// Database connection settings
$dsn = 'mysql:host=your_host;dbname=your_database;charset=utf8';
$username = 'your_username';
$password = 'your_password';

try {
    // Create a PDO instance
    $pdo = new PDO($dsn, $username, $password);
    
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    /**
     * Function to fetch all users from the database.
     *
     * @return array The list of users.
     * @throws Exception If the query fails.
     */
    function fetchAllUsers($pdo) {
        $sql = 'SELECT * FROM users'; // Modify with your table name
        $stmt = $pdo->prepare($sql);
        
        // Execute the statement
        $stmt->execute();
        
        // Fetch all users as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Attempt to get users and display them
    try {
        $users = fetchAllUsers($pdo);
        foreach ($users as $user) {
            echo 'User ID: ' . htmlspecialchars($user['id']) . '<br>';
            echo 'Username: ' . htmlspecialchars($user['username']) . '<br>'; // Ensure safe output
            echo 'Email: ' . htmlspecialchars($user['email']) . '<br><br>'; // Ensure safe output
        }
    } catch (Exception $e) {
        // Handle query errors gracefully
        echo 'Error fetching users: ' . $e->getMessage();
    }

} catch (PDOException $e) {
    // Handle connection errors
    echo 'Connection failed: ' . $e->getMessage();
}
```
