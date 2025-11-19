"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Create a PHP code snippet that retrieves and displays a list of educational toys available in a stationery store's inventory.
Generated: DETERMINISTIC_4ba3e4322c01415f
Batch ID: 20250612_160507
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
$host = 'localhost'; // Database server
$dbName = 'stationery_store'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbName", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Query to retrieve educational toys from the inventory
    $query = "SELECT id, name, price, available_quantity FROM inventory WHERE category = 'Educational Toys'";
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    
    // Fetch the results
    $educationalToys = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Display the results
    if (!empty($educationalToys)) {
        echo "<h1>List of Educational Toys</h1>";
        echo "<table border='1' cellpadding='5' cellspacing='0'>";
        echo "<tr><th>ID</th><th>Name</th><th>Price</th><th>Available Quantity</th></tr>";
        
        foreach ($educationalToys as $toy) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($toy['id']) . "</td>";
            echo "<td>" . htmlspecialchars($toy['name']) . "</td>";
            echo "<td>" . htmlspecialchars(number_format($toy['price'], 2)) . "</td>";
            echo "<td>" . htmlspecialchars($toy['available_quantity']) . "</td>";
            echo "</tr>";
        }
        
        echo "</table>";
    } else {
        echo "<p>No educational toys found in the inventory.</p>";
    }

} catch (PDOException $e) {
    // Handle database connection errors
    echo "<p>Error: Unable to connect to the database. Please try again later.</p>";
    error_log("Database Connection Error: " . $e->getMessage());
} catch (Exception $e) {
    // Handle generic errors
    echo "<p>An unexpected error occurred. Please try again later.</p>";
    error_log("General Error: " . $e->getMessage());
}
?>
```
