"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Generate a PHP script that uses the PDO driver-specific subclasses introduced in PHP 8.4 to interact with a MySQL database.
Generated: DETERMINISTIC_4f82188346111bca
Batch ID: 20250612_154339
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
 * A PHP script using PDO driver-specific subclasses (introduced in PHP 8.4) for MySQL interaction.
 * This script performs basic CRUD operations in a production-ready manner.
 */

// Database configuration
define('DB_HOST', '127.0.0.1');
define('DB_NAME', 'example_database');
define('DB_USER', 'example_user');
define('DB_PASS', 'example_password');

try {
    // Establish a connection using PDO MySQL driver
    $pdo = new PDO\MySQL("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch associative arrays by default
    ]);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to get all records from the `users` table
 */
function getAllUsers(PDO\MySQL $pdo): array {
    try {
        $stmt = $pdo->query("SELECT * FROM users");
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        error_log("Error fetching users: " . $e->getMessage());
        return [];
    }
}

/**
 * Function to insert a new user into the `users` table
 */
function insertUser(PDO\MySQL $pdo, string $name, string $email): bool {
    try {
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error inserting user: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to update a user's email in the `users` table
 */
function updateUserEmail(PDO\MySQL $pdo, int $id, string $email): bool {
    try {
        $stmt = $pdo->prepare("UPDATE users SET email = :email WHERE id = :id");
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error updating user email: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to delete a user from the `users` table
 */
function deleteUser(PDO\MySQL $pdo, int $id): bool {
    try {
        $stmt = $pdo->prepare("DELETE FROM users WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error deleting user: " . $e->getMessage());
        return false;
    }
}

// Example usage
// Uncomment the lines below to test the script:

// Insert a new user
// if (insertUser($pdo, 'John Doe', 'john.doe@example.com')) echo "User inserted successfully.\n";

// Get all users
// $users = getAllUsers($pdo);
// print_r($users);

// Update a user's email
// if (updateUserEmail($pdo, 1, 'new.email@example.com')) echo "User email updated successfully.\n";

// Delete a user
// if (deleteUser($pdo, 1)) echo "User deleted successfully.\n";

?>
```
