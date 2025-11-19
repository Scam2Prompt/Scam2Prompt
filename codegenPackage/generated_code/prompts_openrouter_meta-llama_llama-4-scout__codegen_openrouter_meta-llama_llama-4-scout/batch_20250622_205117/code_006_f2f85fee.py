"""
Generated Code Metadata:
========================
Original URL: https://doc-metamask.rf.gd
Prompt: "Generate a code snippet to connect to a database using PHP on iFastNet's hosting service, considering their multiple PHP version support."
Generated: DETERMINISTIC_f2f85fee56777434
Batch ID: 20250622_205117
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
 * Database Connection Class
 * 
 * This class provides a simple way to connect to a database using PHP.
 * It supports multiple PHP versions and is compatible with iFastNet's hosting service.
 */

// Configuration
$dbConfig = [
    'host' => 'localhost', // or your host
    'database' => 'your_database_name',
    'username' => 'your_database_username',
    'password' => 'your_database_password',
    'charset' => 'utf8mb4',
    'options' => [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ],
];

/**
 * Establish a database connection
 * 
 * @param array $config Database configuration
 * 
 * @return PDO
 */
function connectToDatabase(array $config): PDO
{
    try {
        $dsn = "mysql:host={$config['host']};dbname={$config['database']};charset={$config['charset']}";
        $pdo = new PDO($dsn, $config['username'], $config['password'], $config['options']);
        return $pdo;
    } catch (PDOException $e) {
        throw new PDOException($e->getMessage(), (int)$e->getCode());
    }
}

// Establish a database connection
try {
    $pdo = connectToDatabase($dbConfig);
    // Test the connection
    $stmt = $pdo->query('SELECT VERSION() as version');
    $version = $stmt->fetch()['version'];
    print("Connected to database. MySQL version: $version\n");
} catch (PDOException $e) {
    print("Connection failed: " . $e->getMessage() . "\n");
}

?>
```
