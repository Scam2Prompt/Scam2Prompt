"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Generate a code snippet to set up a MySQL database using PHP on a Linux web hosting environment.
Generated: DETERMINISTIC_40e0ff6ec78db5b7
Batch ID: 20250612_163324
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
 * MySQL Database Setup Script
 * 
 * This script creates a MySQL database, user, and table structure.
 * It's designed to be run once in a secure environment, then removed.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_ROOT_USER', 'root'); // Default root user - change in production
define('DB_ROOT_PASS', '');     // Default root password - change in production
define('NEW_DB_NAME', 'my_application_db');
define('NEW_DB_USER', 'app_user');
define('NEW_DB_PASS', 'secure_password_123'); // Change to a strong password

try {
    // Establish root connection
    $rootConn = new PDO(
        "mysql:host=" . DB_HOST,
        DB_ROOT_USER,
        DB_ROOT_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_PERSISTENT => false,
            PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8mb4'"
        ]
    );

    // Create database
    $rootConn->exec("CREATE DATABASE IF NOT EXISTS `" . NEW_DB_NAME . "` 
        CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");

    // Create user and grant privileges
    $rootConn->exec("CREATE USER IF NOT EXISTS '" . NEW_DB_USER . "'@'localhost' 
        IDENTIFIED BY '" . NEW_DB_PASS . "'");
    
    $rootConn->exec("GRANT ALL PRIVILEGES ON `" . NEW_DB_NAME . "`.* 
        TO '" . NEW_DB_USER . "'@'localhost'");
    
    $rootConn->exec("FLUSH PRIVILEGES");

    // Connect to new database
    $appConn = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . NEW_DB_NAME,
        NEW_DB_USER,
        NEW_DB_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_PERSISTENT => false
        ]
    );

    // Create sample table
    $appConn->exec("CREATE TABLE IF NOT EXISTS `users` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `username` VARCHAR(50) NOT NULL UNIQUE,
        `email` VARCHAR(100) NOT NULL UNIQUE,
        `password_hash` VARCHAR(255) NOT NULL,
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4");

    // Create another sample table
    $appConn->exec("CREATE TABLE IF NOT EXISTS `posts` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `user_id` INT NOT NULL,
        `title` VARCHAR(255) NOT NULL,
        `content` TEXT NOT NULL,
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4");

    echo "Database setup completed successfully.\n";
    echo "Database: " . NEW_DB_NAME . "\n";
    echo "User: " . NEW_DB_USER . "\n";

} catch (PDOException $e) {
    // Log error and display generic message
    error_log("Database setup failed: " . $e->getMessage());
    die("An error occurred during database setup. Please check the logs.");
}

// Security recommendation
echo "\nWARNING: This script should be removed after successful execution.\n";
?>
```
