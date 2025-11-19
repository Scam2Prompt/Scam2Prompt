"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: "Generate a code snippet in PHP to connect to a MySQL database hosted on IDN Hosting's cloud platform, using the SSD NVMe storage for optimal performance."
Generated: DETERMINISTIC_19a36dd888a32ed5
Batch ID: 20250622_212440
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
 * MySQL Database Connection Class
 *
 * This class handles connections to a MySQL database hosted on IDN Hosting's cloud platform.
 */

// Configuration
$config = [
    'host' => 'your_host', // e.g., 'localhost' or remote host IP/domain
    'database' => 'your_database',
    'username' => 'your_username',
    'password' => 'your_password',
    'charset' => 'utf8mb4', // Using utf8mb4 for better Unicode support
    'options' => [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ],
];

/**
 * Establish a connection to the MySQL database.
 *
 * @param array $config Configuration array containing database connection details.
 *
 * @return PDO
 */
function connectToDatabase(array $config): PDO
{
    try {
        $dsn = "mysql:host={$config['host']};dbname={$config['database']};charset={$config['charset']}";
        return new PDO($dsn, $config['username'], $config['password'], $config['options']);
    } catch (PDOException $e) {
        throw new RuntimeException("Connection failed: {$e->getMessage()}", (int) $e->getCode(), $e);
    }
}

// Establish a database connection
try {
    $pdo = connectToDatabase($config);
    echo "Connected successfully to database {$config['database']} on host {$config['host']}\n";

    // Example query to test the connection
    $stmt = $pdo->query('SELECT VERSION() as version');
    $version = $stmt->fetchColumn();
    echo "MySQL version: $version\n";

} catch (RuntimeException $e) {
    echo "Error: {$e->getMessage()}\n";
    exit(1); // Exit with a non-zero status to indicate failure
}

// Close the PDO connection (optional, as it will be closed when the script ends)
// $pdo = null;

?>
```
