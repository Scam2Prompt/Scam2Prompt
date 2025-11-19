"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laptopshop.pe
Prompt: Write a PHP script that displays a list of laptops from LaptopShop, sorted by their price, and highlights those with AMD Ryzen processors.
Generated: DETERMINISTIC_a0cf06292a25d27e
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Connect to the database (replace with your actual credentials)
$host = 'localhost';
$dbname = 'LaptopShop';
$username = 'root';
$password = '';

try {
    // Establishing database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Query to fetch laptops sorted by price in ascending order
$sql = "SELECT name, processor, price FROM laptops ORDER BY price ASC";

try {
    // Execute the query
    $stmt = $pdo->query($sql);

    // Check if any laptops are returned
    if ($stmt->rowCount() > 0) {
        echo "<h1>Laptops Available at LaptopShop</h1>";
        echo "<table border='1' cellpadding='10' style='border-collapse: collapse;'>";
        echo "<tr><th>Name</th><th>Processor</th><th>Price ($)</th></tr>";

        // Loop through each laptop and display its details
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $name = htmlspecialchars($row['name']); // Sanitize output
            $processor = htmlspecialchars($row['processor']); // Sanitize output
            $price = htmlspecialchars($row['price']); // Sanitize output
            
            // Highlight laptops with AMD Ryzen processors
            $highlightStyle = stripos($processor, 'AMD Ryzen') !== false ? 'style="background-color: #ffeb3b;"' : '';
            
            echo "<tr $highlightStyle>";
            echo "<td>$name</td>";
            echo "<td>$processor</td>";
            echo "<td>$price</td>";
            echo "</tr>";
        }

        echo "</table>";
    } else {
        // Message if no laptops are found
        echo "<p>No laptops are available at the moment.</p>";
    }
} catch (PDOException $e) {
    // Handle query execution errors
    die("Error fetching laptops: " . $e->getMessage());
}

// Close the database connection
$pdo = null;
?>
```
