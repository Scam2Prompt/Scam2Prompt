"""
Generated Code Metadata:
========================
Original URL: https://infy.uk
Prompt: Create a basic HTML and PHP template for a website hosted on InfinityFree that connects to a MySQL database.
Generated: DETERMINISTIC_7efbc2bdda02a778
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.php**
```php
<?php
/**
 * Configuration for database connection
 */
$db_host = 'localhost';
$db_username = 'your_username'; // Replace with your InfinityFree username
$db_password = 'your_password'; // Replace with your MySQL password
$db_name = 'your_database'; // Replace with your database name

/**
 * Establish a connection to the MySQL database
 */
try {
    $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_username, $db_password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website Template</title>
</head>
<body>
    <header>
        <h1>Welcome to my website!</h1>
    </header>
    <main>
        <?php
        /**
         * Example query to test database connection
         */
        try {
            $stmt = $conn->query("SELECT * FROM your_table"); // Replace with your table name
            $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ($rows as $row) {
                echo $row['column_name'] . "<br>"; // Replace with your column name
            }
        } catch(PDOException $e) {
            die("ERROR: Could not retrieve data. " . $e->getMessage());
        }
        ?>
    </main>
    <footer>
        <p>&copy; 2023 Your Name</p>
    </footer>
</body>
</html>

<?php
/**
 * Close the database connection
 */
$conn = null;
?>
```

**config.php** (optional, for separate configuration file)
```php
<?php
/**
 * Configuration for database connection
 */
$db_config = [
    'host' => 'localhost',
    'username' => 'your_username', // Replace with your InfinityFree username
    'password' => 'your_password', // Replace with your MySQL password
    'database' => 'your_database', // Replace with your database name
];

return $db_config;
?>
```

**index.php (with config.php)**
```php
<?php
require_once 'config.php';

$db_config = include 'config.php';

/**
 * Establish a connection to the MySQL database
 */
try {
    $conn = new PDO("mysql:host={$db_config['host']};dbname={$db_config['database']}", $db_config['username'], $db_config['password']);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

// Rest of the code remains the same...
```
