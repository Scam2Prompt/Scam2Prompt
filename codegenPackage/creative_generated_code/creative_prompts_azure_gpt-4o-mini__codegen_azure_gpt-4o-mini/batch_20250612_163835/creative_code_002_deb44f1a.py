"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Can you provide code examples for building a website using PHP and MySQL?
Generated: DETERMINISTIC_deb44f1a00e5be19
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection file
class Database {
    private $host = 'localhost'; // Database host
    private $db_name = 'example_db'; // Database name
    private $username = 'root'; // Database username
    private $password = ''; // Database password
    public $connection;

    // Function to get the database connection
    public function getConnection() {
        $this->connection = null;
        try {
            $this->connection = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            // Handle connection error
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->connection;
    }
}
?>
```

```php
<?php
// index.php - Main page of the website
require_once 'database.php'; // Include the database connection file

// Create a new database connection
$database = new Database();
$db = $database->getConnection();

// Fetch data from the database
$query = "SELECT * FROM users"; // SQL query
$stmt = $db->prepare($query);
$stmt->execute();
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($users as $user): ?>
                <tr>
                    <td><?= htmlspecialchars($user['id']) ?></td>
                    <td><?= htmlspecialchars($user['name']) ?></td>
                    <td><?= htmlspecialchars($user['email']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

```php
<?php
// create_user.php - Script to insert new user into the database
require_once 'database.php'; // Include the database connection file

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';

    // Validate input
    if (empty($name) || empty($email)) {
        die('Please provide both name and email.');
    }

    // Create a new database connection
    $database = new Database();
    $db = $database->getConnection();

    // Insert user into the database
    $query = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $db->prepare($query);
    
    // Bind parameters and execute
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);

    if ($stmt->execute()) {
        echo "User created successfully.";
    } else {
        echo "Error creating user.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
</head>
<body>
    <h1>Create a New User</h1>
    <form action="create_user.php" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
        <br>
        <input type="submit" value="Create User">
    </form>
</body>
</html>
```

```sql
-- create_database.sql - SQL script to create the database and users table

CREATE DATABASE IF NOT EXISTS example_db;

USE example_db;

CREATE TABLE IF NOT EXISTS users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```
