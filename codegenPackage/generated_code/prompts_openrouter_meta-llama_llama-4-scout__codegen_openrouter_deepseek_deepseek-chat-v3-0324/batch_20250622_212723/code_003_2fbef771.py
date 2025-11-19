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
 * Database Interaction Script using PEAR DB
 * 
 * This script demonstrates basic CRUD operations using PEAR DB library
 * with MySQL database. Includes error handling and connection management.
 */

// Require PEAR DB library
require_once 'DB.php';

/**
 * Database configuration
 */
$db_config = array(
    'phptype'  => 'mysql',
    'username' => 'db_user',
    'password' => 'db_password',
    'hostspec' => 'localhost',
    'database' => 'test_db'
);

/**
 * Establishes database connection using PEAR DB
 * 
 * @return object DB connection object
 * @throws Exception If connection fails
 */
function connectToDatabase($config) {
    $dsn = "{$config['phptype']}://{$config['username']}:{$config['password']}@{$config['hostspec']}/{$config['database']}";
    $db = DB::connect($dsn);
    
    if (DB::isError($db)) {
        throw new Exception("Database connection failed: " . $db->getMessage());
    }
    
    return $db;
}

/**
 * Creates a sample table if it doesn't exist
 * 
 * @param object $db PEAR DB connection object
 * @throws Exception If table creation fails
 */
function createSampleTable($db) {
    $query = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    
    $result = $db->query($query);
    
    if (DB::isError($result)) {
        throw new Exception("Table creation failed: " . $result->getMessage());
    }
}

/**
 * Inserts a new user record
 * 
 * @param object $db PEAR DB connection object
 * @param string $name User name
 * @param string $email User email
 * @return int The ID of the inserted record
 * @throws Exception If insertion fails
 */
function insertUser($db, $name, $email) {
    $query = "INSERT INTO users (name, email) VALUES (?, ?)";
    $params = array($name, $email);
    
    $result = $db->query($query, $params);
    
    if (DB::isError($result)) {
        throw new Exception("Insert failed: " . $result->getMessage());
    }
    
    return $db->lastInsertID();
}

/**
 * Gets all users from the database
 * 
 * @param object $db PEAR DB connection object
 * @return array Array of user records
 * @throws Exception If query fails
 */
function getAllUsers($db) {
    $query = "SELECT * FROM users";
    $result = $db->query($query);
    
    if (DB::isError($result)) {
        throw new Exception("Query failed: " . $result->getMessage());
    }
    
    $users = array();
    while ($row = $result->fetchRow(DB_FETCHMODE_ASSOC)) {
        $users[] = $row;
    }
    
    return $users;
}

/**
 * Updates a user record
 * 
 * @param object $db PEAR DB connection object
 * @param int $id User ID
 * @param string $name New name
 * @param string $email New email
 * @return int Number of affected rows
 * @throws Exception If update fails
 */
function updateUser($db, $id, $name, $email) {
    $query = "UPDATE users SET name = ?, email = ? WHERE id = ?";
    $params = array($name, $email, $id);
    
    $result = $db->query($query, $params);
    
    if (DB::isError($result)) {
        throw new Exception("Update failed: " . $result->getMessage());
    }
    
    return $result->numRows();
}

/**
 * Deletes a user record
 * 
 * @param object $db PEAR DB connection object
 * @param int $id User ID to delete
 * @return int Number of affected rows
 * @throws Exception If deletion fails
 */
function deleteUser($db, $id) {
    $query = "DELETE FROM users WHERE id = ?";
    $params = array($id);
    
    $result = $db->query($query, $params);
    
    if (DB::isError($result)) {
        throw new Exception("Deletion failed: " . $result->getMessage());
    }
    
    return $result->numRows();
}

// Main execution
try {
    // Connect to database
    $db = connectToDatabase($db_config);
    
    // Set error handling mode
    $db->setErrorHandling(PEAR_ERROR_EXCEPTION);
    
    // Create sample table
    createSampleTable($db);
    
    // Insert sample data
    $newUserId = insertUser($db, 'John Doe', 'john@example.com');
    echo "Inserted new user with ID: $newUserId\n";
    
    // Update user
    $affectedRows = updateUser($db, $newUserId, 'John Updated', 'john.updated@example.com');
    echo "Updated $affectedRows user(s)\n";
    
    // Get all users
    $users = getAllUsers($db);
    echo "Current users:\n";
    print_r($users);
    
    // Delete user
    $affectedRows = deleteUser($db, $newUserId);
    echo "Deleted $affectedRows user(s)\n";
    
    // Close connection
    $db->disconnect();
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
    if (isset($db) && is_object($db)) {
        $db->disconnect();
    }
    exit(1);
}
?>
```
