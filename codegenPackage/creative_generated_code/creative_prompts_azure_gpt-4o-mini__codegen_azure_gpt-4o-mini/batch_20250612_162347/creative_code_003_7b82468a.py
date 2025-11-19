"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erecargaspe.webcindario.com
Prompt: What resources are available for building a website with PHP and MySQL without any cost?
Generated: DETERMINISTIC_7b82468acc183234
Batch ID: 20250612_162347
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
 * Simple PHP and MySQL Example
 * This script demonstrates how to connect to a MySQL database
 * and perform basic CRUD operations.
 * 
 * Requirements:
 * - PHP 7.0 or later
 * - MySQL server
 * - Composer (for dependency management)
 * 
 * Make sure to update the database credentials and table structure
 * according to your needs.
 */

// Database connection settings
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'your_database'); // Replace with your database name
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASS', 'your_password'); // Replace with your database password

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to fetch all records from a specified table
 *
 * @param PDO $pdo The PDO instance
 * @param string $table The name of the table
 * @return array The fetched records
 */
function fetchAllRecords($pdo, $table) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM " . $table);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle errors during fetch
        die("Error fetching records: " . $e->getMessage());
    }
}

/**
 * Function to insert a new record into a specified table
 *
 * @param PDO $pdo The PDO instance
 * @param string $table The name of the table
 * @param array $data An associative array of column => value pairs
 * @return bool True on success, false on failure
 */
function insertRecord($pdo, $table, $data) {
    // Prepare the SQL statement dynamically based on the data array
    $columns = implode(", ", array_keys($data));
    $placeholders = ":" . implode(", :", array_keys($data));
    $sql = "INSERT INTO " . $table . " ($columns) VALUES ($placeholders)";

    try {
        $stmt = $pdo->prepare($sql);
        return $stmt->execute($data);
    } catch (PDOException $e) {
        // Handle errors during insert
        die("Error inserting record: " . $e->getMessage());
    }
}

// Example Usage:
// Fetch all records from the 'users' table
$users = fetchAllRecords($pdo, 'users');
print_r($users);

// Insert a new record into the 'users' table
$newUserData = [
    'username' => 'new_user',
    'email' => 'new_user@example.com'
];
$insertSuccess = insertRecord($pdo, 'users', $newUserData);

if ($insertSuccess) {
    echo "New user inserted successfully.";
} else {
    echo "Failed to insert new user.";
}

// Close the database connection
$pdo = null;
?>
```
