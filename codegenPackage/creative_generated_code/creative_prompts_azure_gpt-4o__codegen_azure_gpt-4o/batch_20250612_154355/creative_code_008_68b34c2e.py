"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Write PHP code to test the connection to a MySQL database hosted on a free platform like miarroba.com.
Generated: DETERMINISTIC_68b34c2e62a33250
Batch ID: 20250612_154355
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
$host = "your-hostname"; // Replace with the hostname provided by miarroba.com
$username = "your-username"; // Replace with your MySQL username
$password = "your-password"; // Replace with your MySQL password
$database = "your-database-name"; // Replace with your database name

// Function to test the connection
function testDatabaseConnection($host, $username, $password, $database) {
    try {
        // Create a new PDO instance for a MySQL database connection
        $dsn = "mysql:host=$host;dbname=$database;charset=utf8mb4"; // Data Source Name
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch results as associative arrays
            PDO::ATTR_EMULATE_PREPARES => false, // Disable emulated prepares for security
        ];

        // Establish the connection
        $pdo = new PDO($dsn, $username, $password, $options);

        // If the connection is successful, return a success message
        return "Database connection successful!";
    } catch (PDOException $e) {
        // Catch any connection errors and return the error message
        return "Database connection failed: " . $e->getMessage();
    }
}

// Run the test and output the result
$result = testDatabaseConnection($host, $username, $password, $database);
echo $result;

?>
```
