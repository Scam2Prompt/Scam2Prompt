"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Create a PHP script to implement a search feature for Dolphin Iran's website that allows users to search for products like "آینه ضد بخار" or "ست سرویس بهداشتی دیواری" by keywords and price range.
Generated: DETERMINISTIC_0014cb3b9b429e71
Batch ID: 20250612_153224
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
define('DB_HOST', 'localhost');
define('DB_NAME', 'dolphin_iran');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');

// Function to connect to the database
function dbConnect() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and return false
        error_log("Database connection error: " . $e->getMessage());
        return false;
    }
}

// Function to search products
function searchProducts($keyword, $minPrice, $maxPrice) {
    // Establish connection
    $pdo = dbConnect();
    if (!$pdo) {
        return [];
    }

    // Prepare SQL query with placeholders
    $sql = "SELECT * FROM products WHERE 
            (name LIKE :keyword OR description LIKE :keyword) 
            AND price BETWEEN :minPrice AND :maxPrice";
    
    // Prepare and execute the statement
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':keyword' => "%$keyword%",
            ':minPrice' => $minPrice,
            ':maxPrice' => $maxPrice
        ]);
        
        // Fetch all results
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log error and return empty array
        error_log("Search query error: " . $e->getMessage());
        return [];
    }
}

// Check if the request is a POST request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user input
    $keyword = filter_input(INPUT_POST, 'keyword', FILTER_SANITIZE_STRING);
    $minPrice = filter_input(INPUT_POST, 'min_price', FILTER_VALIDATE_FLOAT);
    $maxPrice = filter_input(INPUT_POST, 'max_price', FILTER_VALIDATE_FLOAT);

    // Validate that prices are set correctly
    if ($minPrice === false || $maxPrice === false || $minPrice < 0 || $maxPrice < 0 || $minPrice > $maxPrice) {
        echo json_encode(['error' => 'Invalid price range']);
        exit;
    }

    // Perform the search
    $results = searchProducts($keyword, $minPrice, $maxPrice);

    // Return results as JSON
    header('Content-Type: application/json');
    echo json_encode($results);
    exit;
}
?>

<!-- HTML Form for product search -->
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>جستجوی محصول</title>
</head>
<body>
    <h1>جستجوی محصولات</h1>
    <form method="POST" action="">
        <label for="keyword">کلیدواژه:</label>
        <input type="text" name="keyword" id="keyword" required>
        <br>
        <label for="min_price">حداقل قیمت:</label>
        <input type="number" name="min_price" id="min_price" step="0.01" min="0" required>
        <br>
        <label for="max_price">حداکثر قیمت:</label>
        <input type="number" name="max_price" id="max_price" step="0.01" min="0" required>
        <br>
        <button type="submit">جستجو</button>
    </form>
</body>
</html>
```
