"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: What are the steps to set up a website using PHP and MySQL as mentioned on credidavivienta?
Generated: DETERMINISTIC_d393129b9fb470e9
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// db.php - Database connection script

/**
 * Establish a connection to the MySQL database using PDO.
 * 
 * @return PDO $pdo The PDO database connection object.
 * @throws Exception If the connection fails.
 */
function getDatabaseConnection() {
    $host = 'localhost'; // Database host
    $dbname = 'your_database_name'; // Database name
    $username = 'your_username'; // Database username
    $password = 'your_password'; // Database password

    try {
        // Create a PDO instance
        $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
        // Set error mode to exception for better error handling
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection error
        throw new Exception('Database connection failed: ' . $e->getMessage());
    }
}
?>

<?php
// index.php - Entry point of the website

/**
 * Main entry point for the website.
 * Loads the database connection and handles user requests.
 */
require 'db.php';

try {
    $pdo = getDatabaseConnection(); // Get the database connection
    // Sample query to fetch data from a 'users' table
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC); // Fetch all users
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
    exit;
}

// HTML output
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
    <?php if (!empty($users)): ?>
        <ul>
            <?php foreach ($users as $user): ?>
                <li><?php echo htmlspecialchars($user['name']); ?></li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No users found.</p>
    <?php endif; ?>
</body>
</html>
```

```php
<?php
// create_user.php - Script to handle user creation

/**
 * Handles the creation of a new user in the database.
 */
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect and sanitize user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);

    if (!$name || !$email) {
        echo 'Invalid input!';
        exit;
    }

    try {
        $pdo = getDatabaseConnection(); // Get the database connection
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->execute(); // Execute the prepared statement
        echo 'User created successfully.';
    } catch (Exception $e) {
        // Handle errors gracefully
        echo 'Error: ' . $e->getMessage();
    }
}
?>

<!-- HTML form for user creation -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
</head>
<body>
    <h1>Create User</h1>
    <form action="create_user.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Create User</button>
    </form>
</body>
</html>
```

```sql
-- schema.sql - SQL script to create the necessary database table

/**
 * SQL script to create 'users' table in the MySQL database.
 */

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This code provides a basic structure for a PHP and MySQL website, including database connection, user listing, and user creation functionality, following best practices and including error handling.
