"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pekana.pk
Prompt: Write a PHP script to integrate a search functionality that mimics the "Search for" feature on https://www.pekana.pk, allowing users to find products by name or category.
Generated: DETERMINISTIC_5af85fe511b70b32
Batch ID: 20250612_152109
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
$db   = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create a connection
$conn = new mysqli($host, $user, $pass, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/**
 * Function to search for products based on name or category
 *
 * @param mysqli $conn Database connection
 * @param string $searchTerm The term to search for
 * @return array Array of search results
 */
function searchProducts($conn, $searchTerm) {
    // Prepare the SQL statement to prevent SQL injection
    $stmt = $conn->prepare("SELECT * FROM products WHERE name LIKE ? OR category LIKE ?");
    
    // Use wildcards for LIKE clause
    $searchTermParam = '%' . $searchTerm . '%';
    $stmt->bind_param('ss', $searchTermParam, $searchTermParam);
    
    // Execute the statement
    $stmt->execute();
    
    // Get the result
    $result = $stmt->get_result();
    
    // Fetch all results as an associative array
    $products = $result->fetch_all(MYSQLI_ASSOC);
    
    // Close the statement
    $stmt->close();
    
    return $products;
}

// Check if a search term is provided
if (isset($_GET['search']) && !empty(trim($_GET['search']))) {
    // Sanitize user input
    $searchTerm = htmlspecialchars(trim($_GET['search']));
    
    // Search for products
    $products = searchProducts($conn, $searchTerm);
} else {
    $products = []; // No search term, return empty array
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Search</title>
</head>
<body>
    <h1>Search for Products</h1>
    <form method="GET" action="">
        <input type="text" name="search" placeholder="Search by name or category" required>
        <button type="submit">Search</button>
    </form>

    <?php if (!empty($products)): ?>
        <h2>Search Results:</h2>
        <ul>
            <?php foreach ($products as $product): ?>
                <li><?php echo htmlspecialchars($product['name']); ?> - <?php echo htmlspecialchars($product['category']); ?></li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No products found.</p>
    <?php endif; ?>
</body>
</html>
```
