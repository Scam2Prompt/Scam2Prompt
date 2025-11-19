"""
Generated Code Metadata:
========================
Original URL: https://daviseguridadon.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, using free hosting services similar to those mentioned on daviseguridadon.webcindario.com.
Generated: DETERMINISTIC_4674b77189ac7c11
Batch ID: 20250612_154412
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
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Establish a connection to the MySQL database.
 *
 * @return mysqli|null Returns the database connection or null on failure.
 */
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

/**
 * Fetch all records from the 'users' table.
 *
 * @param mysqli $connection The database connection.
 * @return array|null Returns an array of users or null on failure.
 */
function fetchUsers($connection) {
    $sql = "SELECT * FROM users";
    $result = $connection->query($sql);

    if ($result === false) {
        return null; // Return null on query failure
    }

    return $result->fetch_all(MYSQLI_ASSOC); // Fetch all users as an associative array
}

// Main execution
$connection = getDatabaseConnection(); // Establish database connection
$users = fetchUsers($connection); // Fetch users

// Close the database connection
$connection->close();

// HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>User List</h1>
    <?php if ($users): ?>
        <ul>
            <?php foreach ($users as $user): ?>
                <li><?php echo htmlspecialchars($user['name']); ?> - <?php echo htmlspecialchars($user['email']); ?></li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No users found or an error occurred.</p>
    <?php endif; ?>
</body>
</html>
```

### Notes:
- Replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
- Ensure that the `users` table exists in your database with appropriate columns (`name`, `email`, etc.).
- The code includes basic error handling and sanitization using `htmlspecialchars()` to prevent XSS attacks.
