"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliens143.webcindario.com
Prompt: What are the steps to set up a PHP and MySQL website for free?
Generated: DETERMINISTIC_2ddf0a31a9e71efd
Batch ID: 20250612_163518
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
 * This script demonstrates how to set up a simple PHP and MySQL website.
 * It includes steps to connect to a MySQL database and perform basic CRUD operations.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'username');   // Database username
define('DB_PASS', 'password');   // Database password
define('DB_NAME', 'database_name'); // Database name

/**
 * Function to create a database connection using MySQLi
 * @return mysqli|null Returns the database connection or null on failure
 */
function createDatabaseConnection() {
    // Create a connection
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }

    return $connection;
}

/**
 * Function to create a table in the database
 * @param mysqli $connection The MySQLi connection object
 */
function createTable($connection) {
    // SQL statement to create a table
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    // Execute the query and handle errors
    if (!$connection->query($sql)) {
        echo "Error creating table: " . $connection->error;
    }
}

/**
 * Function to insert a new user into the database
 * @param mysqli $connection The MySQLi connection object
 * @param string $username The username of the user
 * @param string $email The email of the user
 */
function insertUser($connection, $username, $email) {
    // Prepare an SQL statement
    $stmt = $connection->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $email);

    // Execute and check for errors
    if (!$stmt->execute()) {
        echo "Error inserting user: " . $stmt->error;
    }

    $stmt->close();
}

/**
 * Function to fetch all users from the database
 * @param mysqli $connection The MySQLi connection object
 * @return array Returns an array of users
 */
function fetchUsers($connection) {
    $result = $connection->query("SELECT * FROM users");

    // Error handling for the query
    if (!$result) {
        echo "Error fetching users: " . $connection->error;
        return [];
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

// Main script execution
$connection = createDatabaseConnection();
createTable($connection);

// Insert a sample user
insertUser($connection, 'john_doe', 'john@example.com');

// Fetch and display all users
$users = fetchUsers($connection);
foreach ($users as $user) {
    echo "ID: " . $user['id'] . " | Username: " . $user['username'] . " | Email: " . $user['email'] . " | Created At: " . $user['created_at'] . "<br>";
}

// Close the database connection
$connection->close();
?>
```
