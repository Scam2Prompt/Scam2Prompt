"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Write a PHP script to generate a dynamic product catalog page that mirrors the design and functionality of the "Glisten" website's iPhone case section.
Generated: DETERMINISTIC_8cd82517a26235a6
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start the session
session_start();

// Database connection parameters
$host = 'localhost';
$db = 'product_catalog';
$user = 'root';
$pass = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to fetch products from the database
function fetchProducts($pdo) {
    $sql = "SELECT id, name, description, price, image FROM products WHERE category = 'iPhone Cases'";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Fetch products
$products = fetchProducts($pdo);

// HTML structure for the product catalog
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Product Catalog - iPhone Cases</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>iPhone Cases</h1>
    </header>
    <main>
        <section class="product-catalog">
            <?php if (count($products) > 0): ?>
                <?php foreach ($products as $product): ?>
                    <div class="product-card">
                        <img src="<?php echo htmlspecialchars($product['image']); ?>" alt="<?php echo htmlspecialchars($product['name']); ?>">
                        <h2><?php echo htmlspecialchars($product['name']); ?></h2>
                        <p><?php echo htmlspecialchars($product['description']); ?></p>
                        <p class="price">$<?php echo number_format($product['price'], 2); ?></p>
                        <button class="add-to-cart" data-id="<?php echo $product['id']; ?>">Add to Cart</button>
                    </div>
                <?php endforeach; ?>
            <?php else: ?>
                <p>No products available at this time.</p>
            <?php endif; ?>
        </section>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Your Company Name. All rights reserved.</p>
    </footer>
    <script src="script.js"></script> <!-- Link to external JavaScript -->
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

.product-catalog {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
}

.product-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 200px;
    text-align: center;
}

.product-card img {
    max-width: 100%;
    height: auto;
}

.price {
    font-weight: bold;
    color: #333;
}

.add-to-cart {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover {
    background: #218838;
}
```

```javascript
// script.js
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.add-to-cart');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-id');
            // Logic to add the product to the cart
            alert('Product ' + productId + ' added to cart!');
        });
    });
});
```
