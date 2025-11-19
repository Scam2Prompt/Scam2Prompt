"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muskelon547776.webcindario.com
Prompt: What are the steps to set up a PHP and MySQL website for free?
Generated: DETERMINISTIC_2ddf0a31a9e71efd
Batch ID: 20250612_160703
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
define('DB_PASS', 'password');    // Database password
define('DB_NAME', 'database_name'); // Database name

/**
 * Function to create a database connection using MySQLi
 * @return mysqli|null Returns a MySQLi connection object or null on failure
 */
function createConnection() {
    // Create a connection
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die('Connection failed: ' . $connection->connect_error);
    }
    return $connection;
}

/**
 * Function to create a table in the database
 * @param mysqli $connection The database connection
 */
function createTable($connection) {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    if ($connection->query($sql) === FALSE) {
        echo "Error creating table: " . $connection->error;
    }
}

/**
 * Function to insert a user into the database
 * @param mysqli $connection The database connection
 * @param string $username The username to insert
 * @param string $email The email to insert
 */
function insertUser($connection, $username, $email) {
    $stmt = $connection->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $email);

    if ($stmt->execute() === FALSE) {
        echo "Error inserting user: " . $stmt->error;
    } else {
        echo "User inserted successfully.";
    }

    $stmt->close();
}

/**
 * Function to retrieve all users from the database
 * @param mysqli $connection The database connection
 */
function getUsers($connection) {
    $result = $connection->query("SELECT * FROM users");

    if ($result->num_rows > 0) {
        // Output data of each row
        while ($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"] . " - Name: " . $row["username"] . " - Email: " . $row["email"] . "<br>";
        }
    } else {
        echo "No users found.";
    }
}

// Main execution
$connection = createConnection(); // Establish a database connection
createTable($connection); // Create the users table if it doesn't exist

// Example of inserting a user (this can be based on user input)
insertUser($connection, 'JohnDoe', 'john@example.com'); // Insert a sample user
getUsers($connection); // Retrieve and display all users

// Close the connection
$connection->close();
?>
```
