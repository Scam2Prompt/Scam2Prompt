"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: What are the advantages of using PHP and MySQL for building a free website?
Generated: DETERMINISTIC_31a18116fff1fe67
Batch ID: 20250612_155417
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
 * Simple PHP & MySQL Application to Demonstrate the Advantages
 * of Using PHP and MySQL for Building a Free Website
 * 
 * This script connects to a MySQL database, retrieves data,
 * and displays it on a web page, illustrating the ease of use
 * and dynamic capabilities of PHP and MySQL.
 */

// Database configuration
$host = 'localhost'; // Database host
$db_name = 'test_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // SQL query to select all records from a sample table
    $sql = "SELECT * FROM sample_table";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();

    // Fetch all results
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if any results were returned
    if (count($results) > 0) {
        echo "<h1>Data from Database</h1>";
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Name</th><th>Email</th></tr>";

        // Loop through each result and display it in a table
        foreach ($results as $row) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['id']) . "</td>";
            echo "<td>" . htmlspecialchars($row['name']) . "</td>";
            echo "<td>" . htmlspecialchars($row['email']) . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No records found.";
    }
} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . $e->getMessage();
}

// Close the database connection
$pdo = null;
?>
```
