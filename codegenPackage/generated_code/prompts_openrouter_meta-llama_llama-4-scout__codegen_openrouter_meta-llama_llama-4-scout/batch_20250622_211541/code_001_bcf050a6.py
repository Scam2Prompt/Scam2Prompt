"""
Generated Code Metadata:
========================
Original URL: https://ct.ws
Prompt: How can I host a PHP and MySQL-based website for free using InfinityFree?
Generated: DETERMINISTIC_bcf050a6f3884b71
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Configuration for database connection
 */

// Define database host, username, password, and database name
$db_host = 'mysql.your-domain.com'; // Replace with your InfinityFree database host
$db_username = 'your_username'; // Replace with your InfinityFree database username
$db_password = 'your_password'; // Replace with your InfinityFree database password
$db_name = 'your_database_name'; // Replace with your InfinityFree database name

/**
 * Establish a connection to the database
 */
try {
    $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_username, $db_password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

/**
 * Close the database connection
 */
function closeConnection($conn) {
    $conn = null;
}

/**
 * Example usage: Create a table
 */
try {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        email VARCHAR(50)
    )";
    $conn->exec($sql);
} catch(PDOException $e) {
    die("ERROR: Could not create table. " . $e->getMessage());
}

/**
 * Example usage: Insert data into the table
 */
try {
    $sql = "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')";
    $conn->exec($sql);
} catch(PDOException $e) {
    die("ERROR: Could not insert data. " . $e->getMessage());
}

/**
 * Close the database connection
 */
closeConnection($conn);
?>
```

```sql
-- Create a table
CREATE TABLE IF NOT EXISTS users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50)
);

-- Insert data into the table
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
```

**Note:** 

*   Make sure to replace the placeholders (`your-domain.com`, `your_username`, `your_password`, `your_database_name`) with your actual InfinityFree database credentials.
*   Ensure that the MySQLi or PDO extension is enabled in your PHP configuration.

**index.php** (for testing)
```php
<?php
require_once 'db.php'; // Assume db.php contains the database connection code

// Test database connection
try {
    $stmt = $conn->prepare("SELECT * FROM users");
    $stmt->execute();
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
    print_r($users);
} catch(PDOException $e) {
    die("ERROR: Could not retrieve data. " . $e->getMessage());
}

// Close the database connection
closeConnection($conn);
?>
```
