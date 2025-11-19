"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erecargaspe.webcindario.com
Prompt: Can you provide a code example for connecting PHP to a MySQL database for a free website?
Generated: DETERMINISTIC_76d84d5723ba741e
Batch ID: 20250612_162347
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
$host = 'localhost';    // Database host (typically 'localhost' for free websites)
$dbname = 'your_database_name'; // Name of your database
$username = 'your_username';   // Database username
$password = 'your_password';   // Database password

try {
    // Establish a connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);

    // Set PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Connection successful
    echo "Connection to the database was successful!";
} catch (PDOException $e) {
    // Handle connection errors gracefully
    echo "Database connection failed: " . $e->getMessage();
}

// Example query (optional, for testing purposes)
// Uncomment below lines to test the connection with a simple query
/*
try {
    $query = $pdo->query("SELECT * FROM your_table_name");
    $results = $query->fetchAll(PDO::FETCH_ASSOC);
    
    // Output the results (for testing)
    print_r($results);
} catch (PDOException $e) {
    echo "Error executing query: " . $e->getMessage();
}
*/
?>
```
