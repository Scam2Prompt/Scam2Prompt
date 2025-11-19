"""
Generated Code Metadata:
========================
Original URL: https://coosella5554.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display data on a webpage, suitable for hosting on a free platform like miarroba.com.
Generated: DETERMINISTIC_4798641dd453d12f
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
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
    
    // Prepare and execute a SQL query to fetch data
    $stmt = $pdo->prepare("SELECT * FROM your_table_name");
    $stmt->execute();
    
    // Fetch all results
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Check if results are not empty
    if ($results) {
        echo "<h1>Data from Database</h1>";
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Name</th><th>Email</th></tr>"; // Adjust headers based on your table structure
        
        // Loop through the results and display them in a table
        foreach ($results as $row) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['id']) . "</td>"; // Adjust based on your table structure
            echo "<td>" . htmlspecialchars($row['name']) . "</td>"; // Adjust based on your table structure
            echo "<td>" . htmlspecialchars($row['email']) . "</td>"; // Adjust based on your table structure
            echo "</tr>";
        }
        
        echo "</table>";
    } else {
        echo "<p>No data found.</p>";
    }
} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . htmlspecialchars($e->getMessage());
}

// Close the database connection
$pdo = null;
?>
```
