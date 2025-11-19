"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingresaenlaapp.webcindario.com
Prompt: Can you provide a code example for connecting PHP to a MySQL database for a free website?
Generated: DETERMINISTIC_76d84d5723ba741e
Batch ID: 20250612_164021
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
$host = 'localhost';    // Database host (typically 'localhost' for local servers)
$dbName = 'your_database_name'; // Name of the database
$username = 'your_username';    // Database username
$password = 'your_password';    // Database password

try {
    // Establish a connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbName;charset=utf8", $username, $password);
    
    // Set PDO attributes for better error handling and performance
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Throw exceptions on errors
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC); // Fetch results as associative arrays

    // Connection successful
    echo "Connected successfully to the database!";
} catch (PDOException $e) {
    // Handle connection errors gracefully
    echo "Database connection failed: " . $e->getMessage();
    exit; // Exit the script if a connection cannot be established
}

// Example query (optional, for demonstration)
// Uncomment and modify the query below to test database interaction
/*
try {
    $query = $pdo->query("SELECT * FROM your_table_name");
    $results = $query->fetchAll();
    print_r($results); // Print the results of the query
} catch (PDOException $e) {
    echo "Query failed: " . $e->getMessage();
}
*/

// Close the connection (optional, PDO handles this automatically when the script ends)
$pdo = null;
?>
```
