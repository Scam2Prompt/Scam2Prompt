"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: What are the steps to set up a website with PHP and MySQL on myarroba.com?
Generated: DETERMINISTIC_6aa918d690cb9160
Batch ID: 20250612_155417
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
 * A simple PHP script to demonstrate database connection and basic CRUD operations
 * using MySQL. This script assumes you have a MySQL database set up and accessible.
 */

// Database configuration
$host = 'localhost'; // Change this to your database host
$db = 'your_database'; // Change this to your database name
$user = 'your_username'; // Change this to your database username
$pass = 'your_password'; // Change this to your database password

// Create a connection to the MySQL database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully to the database.";
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to create a new record in the database
 * @param string $name The name of the user
 */
function createUser($name) {
    global $pdo;
    $sql = "INSERT INTO users (name) VALUES (:name)";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->execute();
        echo "New user created successfully.";
    } catch (PDOException $e) {
        // Handle query error
        echo "Error creating user: " . $e->getMessage();
    }
}

/**
 * Function to read user data from the database
 */
function readUsers() {
    global $pdo;
    $sql = "SELECT * FROM users";

    try {
        $stmt = $pdo->query($sql);
        $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $users;
    } catch (PDOException $e) {
        // Handle query error
        echo "Error reading users: " . $e->getMessage();
        return [];
    }
}

/**
 * Function to update a user in the database
 * @param int $id The ID of the user to update
 * @param string $name The new name of the user
 */
function updateUser($id, $name) {
    global $pdo;
    $sql = "UPDATE users SET name = :name WHERE id = :id";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        echo "User updated successfully.";
    } catch (PDOException $e) {
        // Handle query error
        echo "Error updating user: " . $e->getMessage();
    }
}

/**
 * Function to delete a user from the database
 * @param int $id The ID of the user to delete
 */
function deleteUser($id) {
    global $pdo;
    $sql = "DELETE FROM users WHERE id = :id";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        echo "User deleted successfully.";
    } catch (PDOException $e) {
        // Handle query error
        echo "Error deleting user: " . $e->getMessage();
    }
}

// Example usage
createUser('John Doe'); // Create a new user
$users = readUsers(); // Read all users
var_dump($users); // Display users

// Update a user (assuming user with ID 1 exists)
updateUser(1, 'Jane Doe');

// Delete a user (assuming user with ID 1 exists)
deleteUser(1);

// Close the database connection
$pdo = null;
?>
```

In the code above:
- Replace the placeholder values for `$host`, `$db`, `$user`, and `$pass` with your actual database credentials.
- Ensure that you have a table named `users` with at least an `id` (auto-increment) and `name` column in your MySQL database.
