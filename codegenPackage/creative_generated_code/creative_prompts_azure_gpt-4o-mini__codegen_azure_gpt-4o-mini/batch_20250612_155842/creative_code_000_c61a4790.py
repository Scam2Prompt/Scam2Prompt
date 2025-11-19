"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Generate a PHP script for a web application hosted on Linux that utilizes MySQL for database management.
Generated: DETERMINISTIC_c61a47901111a65c
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Simple PHP script to connect to a MySQL database and fetch records.
 * This script demonstrates best practices, including error handling and documentation.
 */

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Prepare the SQL statement
    $sql = "SELECT * FROM your_table_name"; // Change 'your_table_name' to your actual table
    $stmt = $pdo->prepare($sql);
    
    // Execute the statement
    $stmt->execute();
    
    // Fetch all results
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Check if there are results
    if (count($results) > 0) {
        // Display results
        foreach ($results as $row) {
            echo "ID: " . htmlspecialchars($row['id']) . "<br>";
            echo "Name: " . htmlspecialchars($row['name']) . "<br>";
            echo "Email: " . htmlspecialchars($row['email']) . "<br><br>";
        }
    } else {
        echo "No records found.";
    }

} catch (PDOException $e) {
    // Handle connection errors or query errors
    echo "Error: " . $e->getMessage();
}

// Close the connection
$pdo = null;
?>
```
