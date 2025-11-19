"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Write a PHP script that connects to a MySQL database and retrieves user data using PDO.
Generated: DETERMINISTIC_0f36c331ff4d60e1
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$db = 'your_database_name'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4'; // Charset for the database connection

// Data source name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// PDO options
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Throw exceptions on errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch data as associative array
    PDO::ATTR_EMULATE_PREPARES   => false,                  // Use real prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);

    // Prepare a SQL statement to retrieve user data
    $stmt = $pdo->prepare('SELECT id, username, email FROM users');

    // Execute the prepared statement
    $stmt->execute();

    // Fetch all user data
    $users = $stmt->fetchAll();

    // Check if any users were retrieved
    if ($users) {
        // Output user data
        foreach ($users as $user) {
            echo "ID: " . htmlspecialchars($user['id']) . "<br>";
            echo "Username: " . htmlspecialchars($user['username']) . "<br>";
            echo "Email: " . htmlspecialchars($user['email']) . "<br><br>";
        }
    } else {
        echo "No users found.";
    }
} catch (PDOException $e) {
    // Handle connection errors
    echo "Database connection failed: " . htmlspecialchars($e->getMessage());
}
?>
```
