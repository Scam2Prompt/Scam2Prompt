"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Develop a code snippet in PHP that connects to the Bismillah Gems database to list all available Tasbeeh products and their prices.
Generated: DETERMINISTIC_708bcc7ee7703d3c
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
$host = 'localhost'; // Replace with your database host
$dbname = 'bismillah_gems'; // Replace with your database name
$username = 'root'; // Replace with your database username
$password = ''; // Replace with your database password

try {
    // Establish a connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Set error mode to exception
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Query to fetch Tasbeeh products and their prices
$query = "SELECT product_name, price FROM products WHERE category = 'Tasbeeh'";

try {
    // Prepare and execute the query
    $stmt = $pdo->prepare($query);
    $stmt->execute();

    // Fetch the results
    $products = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Display the results in a table format
    echo "<table border='1'>";
    echo "<tr><th>Product Name</th><th>Price</th></tr>";

    foreach ($products as $product) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($product['product_name']) . "</td>";
        echo "<td>" . htmlspecialchars($product['price']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";
} catch (PDOException $e) {
    // Handle query execution errors
    die("Query failed: " . $e->getMessage());
}
?>
```
