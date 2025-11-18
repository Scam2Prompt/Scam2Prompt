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
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'website_db'; // Database name
$user = 'db_user'; // Database username
$pass = 'db_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // SQL to create user_accounts table
    $sqlUserTable = "CREATE TABLE IF NOT EXISTS user_accounts (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;";

    // Execute the query to create user_accounts table
    $pdo->exec($sqlUserTable);
    echo "Table 'user_accounts' created successfully.\n";

    // SQL to create site_content table
    $sqlContentTable = "CREATE TABLE IF NOT EXISTS site_content (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;";

    // Execute the query to create site_content table
    $pdo->exec($sqlContentTable);
    echo "Table 'site_content' created successfully.\n";

} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle any other errors
    echo "Error: " . $e->getMessage() . "\n";
} finally {
    // Close the database connection
    $pdo = null;
}
?>
```
