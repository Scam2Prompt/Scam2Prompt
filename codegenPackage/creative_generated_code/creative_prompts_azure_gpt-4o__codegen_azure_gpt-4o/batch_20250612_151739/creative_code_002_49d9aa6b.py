"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: Create a PHP script to initialize a MySQL database for a website, including tables for user accounts and site content.
Generated: DETERMINISTIC_49d9aa6b96c6f20a
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Initialize MySQL database for a website.
 * Creates tables for user accounts and site content.
 */

// Database connection settings
$host = 'localhost'; // Change to your host
$username = 'root'; // Change to your database username
$password = ''; // Change to your database password
$database = 'website_db'; // Change to your desired database name

try {
    // Establish a connection to MySQL
    $pdo = new PDO("mysql:host=$host", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create the database if it doesn't exist
    $pdo->exec("CREATE DATABASE IF NOT EXISTS $database");
    echo "Database '$database' created successfully.\n";

    // Switch to the newly created database
    $pdo->exec("USE $database");

    // Create the `users` table
    $createUsersTableSQL = "
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    ";
    $pdo->exec($createUsersTableSQL);
    echo "Table 'users' created successfully.\n";

    // Create the `site_content` table
    $createSiteContentTableSQL = "
    CREATE TABLE IF NOT EXISTS site_content (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        author_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB;
    ";
    $pdo->exec($createSiteContentTableSQL);
    echo "Table 'site_content' created successfully.\n";

} catch (PDOException $e) {
    // Handle connection or query errors
    echo "Error: " . $e->getMessage() . "\n";
    exit();
}

// Close the connection
$pdo = null;
?>
```
