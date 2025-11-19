"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Create a PHP script to implement a search feature for Dolphin Iran's website that allows users to search for products like "آینه ضد بخار" or "ست سرویس بهداشتی دیواری" by keywords and price range.
Generated: DETERMINISTIC_0014cb3b9b429e71
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database connection parameters
$host = 'localhost'; // Database host
$db = 'dolphin_iran'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to search products by keywords and price range
function searchProducts($pdo, $keywords, $minPrice, $maxPrice) {
    // Prepare the SQL query with placeholders
    $sql = "SELECT * FROM products WHERE (name LIKE :keywords OR description LIKE :keywords) 
            AND price BETWEEN :minPrice AND :maxPrice";
    
    // Prepare the statement
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters
    $stmt->bindValue(':keywords', '%' . $keywords . '%', PDO::PARAM_STR);
    $stmt->bindValue(':minPrice', $minPrice, PDO::PARAM_INT);
    $stmt->bindValue(':maxPrice', $maxPrice, PDO::PARAM_INT);
    
    // Execute the statement
    $stmt->execute();
    
    // Fetch all matching products
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Check if the search form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the search parameters from the form
    $keywords = isset($_POST['keywords']) ? trim($_POST['keywords']) : '';
    $minPrice = isset($_POST['min_price']) ? (int)$_POST['min_price'] : 0;
    $maxPrice = isset($_POST['max_price']) ? (int)$_POST['max_price'] : PHP_INT_MAX;

    // Validate input
    if (empty($keywords)) {
        echo "Please enter a search term.";
    } else {
        // Search for products
        $products = searchProducts($pdo, $keywords, $minPrice, $maxPrice);
        
        // Check if any products were found
        if (count($products) > 0) {
            // Display the results
            foreach ($products as $product) {
                echo "<div>";
                echo "<h2>" . htmlspecialchars($product['name']) . "</h2>";
                echo "<p>" . htmlspecialchars($product['description']) . "</p>";
                echo "<p>Price: " . htmlspecialchars($product['price']) . " IRR</p>";
                echo "</div>";
            }
        } else {
            echo "No products found matching your criteria.";
        }
    }
}
?>

<!-- HTML form for searching products -->
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Products</title>
</head>
<body>
    <h1>جستجوی محصولات</h1>
    <form method="POST" action="">
        <label for="keywords">کلمات کلیدی:</label>
        <input type="text" id="keywords" name="keywords" required>
        
        <label for="min_price">حداقل قیمت:</label>
        <input type="number" id="min_price" name="min_price" value="0">
        
        <label for="max_price">حداکثر قیمت:</label>
        <input type="number" id="max_price" name="max_price" value="10000000">
        
        <button type="submit">جستجو</button>
    </form>
</body>
</html>
```
