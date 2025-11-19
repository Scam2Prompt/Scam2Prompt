"""
Generated Code Metadata:
========================
Original URL: https://idice.epizy.com
Prompt: Write a code snippet in PHP to connect to a database on iFastNet Web Hosting and perform basic CRUD operations.
Generated: DETERMINISTIC_1af604ce40828fc6
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$dbHost = 'localhost';
$dbName = 'your_database_name';
$dbUser = 'your_database_username';
$dbPass = 'your_database_password';

try {
    // Create PDO connection
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName;charset=utf8", $dbUser, $dbPass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    // CREATE operation
    function createUser($pdo, $name, $email) {
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        return $pdo->lastInsertId();
    }

    // READ operation (single record)
    function getUser($pdo, $id) {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetch();
    }

    // READ operation (all records)
    function getAllUsers($pdo) {
        $stmt = $pdo->query("SELECT * FROM users");
        return $stmt->fetchAll();
    }

    // UPDATE operation
    function updateUser($pdo, $id, $name, $email) {
        $stmt = $pdo->prepare("UPDATE users SET name = :name, email = :email WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        return $stmt->execute();
    }

    // DELETE operation
    function deleteUser($pdo, $id) {
        $stmt = $pdo->prepare("DELETE FROM users WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    }

    // Example usage:
    // $userId = createUser($pdo, 'John Doe', 'john@example.com');
    // $user = getUser($pdo, $userId);
    // $allUsers = getAllUsers($pdo);
    // updateUser($pdo, $userId, 'Jane Doe', 'jane@example.com');
    // deleteUser($pdo, $userId);

} catch (PDOException $e) {
    // Log error and display user-friendly message
    error_log("Database Error: " . $e->getMessage());
    die("A database error occurred. Please try again later.");
}
?>
```
