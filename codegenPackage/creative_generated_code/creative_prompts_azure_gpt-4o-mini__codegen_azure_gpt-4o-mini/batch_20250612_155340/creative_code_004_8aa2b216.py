"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: How do I connect a MySQL database to a PHP website as suggested in the content?
Generated: DETERMINISTIC_8aa2b2169522038c
Batch ID: 20250612_155340
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
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    
    // Set the PDO error mode to exception for error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Example query to fetch data from a table
    $stmt = $pdo->query("SELECT * FROM your_table");

    // Fetch all results
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if results are found
    if ($results) {
        // Output the results
        foreach ($results as $row) {
            echo 'ID: ' . htmlspecialchars($row['id']) . ' - Name: ' . htmlspecialchars($row['name']) . '<br>';
        }
    } else {
        echo 'No records found.';
    }
} catch (PDOException $e) {
    // Handle connection errors
    echo 'Connection failed: ' . $e->getMessage();
}

// Close the PDO connection
$pdo = null;
?>
```
