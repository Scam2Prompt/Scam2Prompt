"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: How do I integrate PHP and MySQL to create a fully functional website?
Generated: DETERMINISTIC_4e356955ac5278dd
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php
// Database configuration file
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', 'password');  // Database password
define('DB_NAME', 'my_database'); // Database name

/**
 * Establish a database connection using MySQLi.
 * Returns: $conn (mysqli object)
 */
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}
?>
```

```php
<?php
// index.php
// Main entry point for the website

require 'config.php'; // Include database configuration file

// Initialize the database connection
$conn = getDatabaseConnection();

// Handle form submission for adding a new record
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['name']) && isset($_POST['email'])) {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);

    // Insert data into the database
    $sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";
    if ($conn->query($sql) === TRUE) {
        $message = "New record created successfully!";
    } else {
        $message = "Error: " . $conn->error;
    }
}

// Fetch all records from the database
$sql = "SELECT id, name, email FROM users";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and MySQL Integration</title>
</head>
<body>
    <h1>PHP and MySQL Integration Example</h1>

    <!-- Display a success/error message -->
    <?php if (isset($message)): ?>
        <p><?php echo htmlspecialchars($message); ?></p>
    <?php endif; ?>

    <!-- User input form -->
    <form method="POST" action="">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Submit</button>
    </form>

    <h2>User List</h2>
    <ul>
        <?php if ($result->num_rows > 0): ?>
            <?php while ($row = $result->fetch_assoc()): ?>
                <li><?php echo htmlspecialchars($row['name']); ?> (<?php echo htmlspecialchars($row['email']); ?>)</li>
            <?php endwhile; ?>
        <?php else: ?>
            <li>No users found.</li>
        <?php endif; ?>
    </ul>

</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
```

```sql
-- users.sql
-- SQL script to create the required database and table

CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
1. Save the PHP files `config.php` and `index.php` in your web server root directory.
2. Execute the SQL script `users.sql` to create the database and table.
3. Replace `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` in `config.php` with your actual database credentials.
4. Ensure your web server has PHP and MySQL installed and properly configured.
