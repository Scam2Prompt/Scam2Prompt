"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Implement a basic CRUD (Create, Read, Update, Delete) operation using PHP and MySQL."
Generated: DETERMINISTIC_66a55fab8829642b
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
$host = 'localhost'; // Database host
$dbname = 'test_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new record
function createRecord($name, $email) {
    global $pdo;
    $sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    return $stmt->execute();
}

// Function to read all records
function readRecords() {
    global $pdo;
    $sql = "SELECT * FROM users";
    $stmt = $pdo->query($sql);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to update a record
function updateRecord($id, $name, $email) {
    global $pdo;
    $sql = "UPDATE users SET name = :name, email = :email WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    return $stmt->execute();
}

// Function to delete a record
function deleteRecord($id) {
    global $pdo;
    $sql = "DELETE FROM users WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':id', $id);
    return $stmt->execute();
}

// Example usage
try {
    // Create a new user
    createRecord('John Doe', 'john@example.com');

    // Read all users
    $users = readRecords();
    print_r($users);

    // Update a user (assuming the user with ID 1 exists)
    updateRecord(1, 'Jane Doe', 'jane@example.com');

    // Delete a user (assuming the user with ID 1 exists)
    deleteRecord(1);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

**Note:** Ensure that you have a MySQL database named `test_db` and a table named `users` with columns `id`, `name`, and `email` for this code to work. The `id` column should be an auto-incrementing primary key.
