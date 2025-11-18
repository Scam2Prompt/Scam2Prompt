"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soportedaviplata.webcindario.com
Prompt: Write PHP code to connect to a MySQL database for a free website hosted on a platform like miarroba.com. Include error handling for the connection.
Generated: DETERMINISTIC_39ac09d765eadadc
Batch ID: 20250612_154222
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
$host = 'your_host'; // Replace with your database host
$dbname = 'your_database_name'; // Replace with your database name
$username = 'your_username'; // Replace with your database username
$password = 'your_password'; // Replace with your database password

try {
    // Create a new PDO instance
    $dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4"; // Data Source Name
    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Set default fetch mode to associative array
        PDO::ATTR_EMULATE_PREPARES => false, // Disable emulation of prepared statements
    ];

    $pdo = new PDO($dsn, $username, $password, $options); // Establish the connection

    // Connection successful
    echo "Connected to the database successfully!";
} catch (PDOException $e) {
    // Handle connection error
    echo "Connection failed: " . $e->getMessage(); // Output the error message
}
?>
```
