"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Write a PHP script to connect to a MySQL database hosted on IDN Hosting's cloud platform and retrieve data from a sample table.
Generated: DETERMINISTIC_92a50a56cebc08dd
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection parameters
$host = 'your-hostname'; // Replace with your database host (e.g., IDN Hosting's provided host)
$dbname = 'your-database-name'; // Replace with your database name
$username = 'your-username'; // Replace with your database username
$password = 'your-password'; // Replace with your database password

try {
    // Establish a connection using PDO
    $dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch data as associative arrays
        PDO::ATTR_EMULATE_PREPARES   => false,                 // Disable emulation of prepared statements
    ];

    $pdo = new PDO($dsn, $username, $password, $options);

    // Prepare an SQL query to retrieve data from a sample table
    $query = "SELECT * FROM sample_table"; // Replace 'sample_table' with the name of your table
    $stmt = $pdo->query($query);

    // Fetch all rows and loop through the results
    $results = $stmt->fetchAll();

    // Output the results
    foreach ($results as $row) {
        echo "Row: " . json_encode($row) . PHP_EOL;
    }

} catch (PDOException $e) {
    // Handle connection and query errors
    echo "Database Error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle any other errors
    echo "General Error: " . $e->getMessage();
}
```
