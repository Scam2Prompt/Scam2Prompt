"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplata9.webcindario.com
Prompt: Can you provide a code example for building a simple web application with PHP and MySQL?
Generated: DETERMINISTIC_49a3be3bd4008323
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration file
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');

/**
 * Establish a database connection using PDO
 * 
 * @return PDO
 * @throws Exception if the connection fails
 */
function getDBConnection() {
    try {
        $pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        // Set the PDO error mode to exception
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection error
        throw new Exception('Database connection error: ' . $e->getMessage());
    }
}
?>

<?php
// index.php - Main entry point for the web application
require 'config.php';

// Start session
session_start();

/**
 * Handle form submission to add a new user
 */
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['username'])) {
    try {
        $pdo = getDBConnection();
        
        // Prepare and execute the insert statement
        $stmt = $pdo->prepare("INSERT INTO users (username) VALUES (:username)");
        $stmt->bindParam(':username', $_POST['username']);
        if ($stmt->execute()) {
            $_SESSION['success'] = "User added successfully!";
        }
    } catch (Exception $e) {
        $_SESSION['error'] = $e->getMessage();
    }
}

// Fetch users from the database
try {
    $pdo = getDBConnection();
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (Exception $e) {
    $_SESSION['error'] = $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>User Management System</h1>

    <?php
    // Display success or error message
    if (isset($_SESSION['success'])) {
        echo "<p style='color: green;'>".$_SESSION['success']."</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p style='color: red;'>".$_SESSION['error']."</p>";
        unset($_SESSION['error']);
    }
    ?>

    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <input type="submit" value="Add User">
    </form>

    <h2>Existing Users</h2>
    <ul>
        <?php foreach ($users as $user): ?>
            <li><?php echo htmlspecialchars($user['username']); ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```sql
-- create_database.sql - SQL script to set up the database
CREATE DATABASE your_database;

USE your_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE
);
```

```css
/* style.css - Simple CSS for user interface */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: navy;
}

form {
    margin: 20px 0;
}

input[type="text"],
input[type="submit"] {
    padding: 10px;
    margin: 5px 0;
}

ul {
    list-style-type: none;
}
``` 

Make sure to replace `your_username`, `your_password`, and `your_database` in `config.php` with your actual MySQL credentials and desired database name. Before running this code, ensure that your web server has PHP and MySQL set up, and that the database has been created using the provided SQL script.
