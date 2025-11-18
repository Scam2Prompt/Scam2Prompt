"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Develop a PHP-based e-commerce website using techniques from APTRON Gurgaon’s PHP and Web Development course.
Generated: DETERMINISTIC_0c3d332ce95078a0
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Entry point for the e-commerce website

// Start session
session_start();

// Include configuration file for database connection
require 'config.php';

// Function to get all products from the database
function getProducts($conn) {
    try {
        $stmt = $conn->prepare("SELECT * FROM products");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching products: " . $e->getMessage());
        return [];
    }
}

// Function to add product to cart
function addToCart($productId) {
    if (!isset($_SESSION['cart'])) {
        $_SESSION['cart'] = [];
    }
    if (isset($_SESSION['cart'][$productId])) {
        $_SESSION['cart'][$productId]++;
    } else {
        $_SESSION['cart'][$productId] = 1;
    }
}

// Handle add to cart action
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_to_cart'])) {
    $productId = intval($_POST['product_id']);
    addToCart($productId);
    header("Location: index.php");
    exit();
}

// Fetch products
$products = getProducts($conn);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<header>
    <h1>Welcome to Our E-Commerce Store</h1>
    <a href="cart.php">View Cart (<?php echo isset($_SESSION['cart']) ? array_sum($_SESSION['cart']) : 0; ?>)</a>
</header>

<main>
    <h2>Products</h2>
    <div class="product-list">
        <?php foreach ($products as $product): ?>
            <div class="product">
                <h3><?php echo htmlspecialchars($product['name']); ?></h3>
                <p>Price: $<?php echo htmlspecialchars($product['price']); ?></p>
                <form action="" method="post">
                    <input type="hidden" name="product_id" value="<?php echo htmlspecialchars($product['id']); ?>">
                    <button type="submit" name="add_to_cart">Add to Cart</button>
                </form>
            </div>
        <?php endforeach; ?>
    </div>
</main>

<footer>
    <p>&copy; 2023 E-Commerce Store</p>
</footer>

</body>
</html>
```

```php
<?php
// config.php - Database connection configuration

// Database credentials
define('DB_HOST', 'localhost');
define('DB_NAME', 'ecommerce_db');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

// Establish database connection using PDO
try {
    $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    error_log("Database connection failed: " . $e->getMessage());
    die("Could not connect to the database.");
}
```

```php
<?php
// cart.php - Display cart contents

// Start session
session_start();

// Function to fetch product details from database
function getProductDetails($conn, $productId) {
    try {
        $stmt = $conn->prepare("SELECT * FROM products WHERE id = ?");
        $stmt->execute([$productId]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching product details: " . $e->getMessage());
        return null;
    }
}

// Check if cart is empty
if (empty($_SESSION['cart'])) {
    $cartItems = [];
} else {
    $cartItems = $_SESSION['cart'];
}

// Prepare product details for the cart
$cartDetails = [];
foreach ($cartItems as $productId => $quantity) {
    $productDetails = getProductDetails($conn, $productId);
    if ($productDetails) {
        $cartDetails[] = [
            'product' => $productDetails,
            'quantity' => $quantity
        ];
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Cart</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<header>
    <h1>Your Cart</h1>
    <a href="index.php">Continue Shopping</a>
</header>

<main>
    <?php if (empty($cartDetails)): ?>
        <p>Your cart is empty.</p>
    <?php else: ?>
        <table>
            <tr>
                <th>Product</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total</th>
            </tr>
            <?php $total = 0; ?>
            <?php foreach ($cartDetails as $item): ?>
                <tr>
                    <td><?php echo htmlspecialchars($item['product']['name']); ?></td>
                    <td>$<?php echo htmlspecialchars($item['product']['price']); ?></td>
                    <td><?php echo htmlspecialchars($item['quantity']); ?></td>
                    <td>
                        <?php
                        $itemTotal = $item['product']['price'] * $item['quantity'];
                        $total += $itemTotal;
                        echo "$" . htmlspecialchars($itemTotal);
                        ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            <tr>
                <td colspan="3">Total</td>
                <td>$<?php echo htmlspecialchars($total); ?></td>
            </tr>
        </table>
    <?php endif; ?>
</main>

<footer>
    <p>&copy; 2023 E-Commerce Store</p>
</footer>

</body>
</html>
```

```css
/* styles.css - Basic stylesheet for the e-commerce website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.product {
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 1rem;
    padding: 1rem;
    width: 200px;
    text-align: center;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 1rem;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

This code provides a basic structure for a PHP-based e-commerce website with functionality for displaying products and managing a shopping cart. Adjust the database connection details and other specific configurations as necessary for deployment.
