"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validardvplta.webcindario.com
Prompt: Provide a PHP and MySQL-based template for a free e-commerce website with custom domain support.
Generated: DETERMINISTIC_f4718e0e4f3b2343
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration for the e-commerce website

// Define database parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'your_db_user');
define('DB_PASS', 'your_db_password');
define('DB_NAME', 'your_db_name');

/**
 * Create a connection to the MySQL database
 * 
 * @return mysqli
 */
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }

    return $connection;
}
?>
```

```php
<?php
// index.php - Main entry point for the e-commerce website

require_once 'config.php';

// Get database connection
$connection = getDatabaseConnection();

// Fetch products from the database
$sql = "SELECT * FROM products";
$result = $connection->query($sql);

if ($result === false) {
    // Handle SQL error
    die("Error fetching products: " . $connection->error);
}

// Begin HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My E-Commerce Store</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My E-Commerce Store</h1>
    </header>
    <main>
        <h2>Products</h2>
        <div class="product-list">
            <?php while ($product = $result->fetch_assoc()): ?>
                <div class="product">
                    <h3><?php echo htmlspecialchars($product['name']); ?></h3>
                    <p><?php echo htmlspecialchars($product['description']); ?></p>
                    <span>Price: $<?php echo htmlspecialchars($product['price']); ?></span>
                    <a href="cart.php?action=add&id=<?php echo $product['id']; ?>">Add to Cart</a>
                </div>
            <?php endwhile; ?>
        </div>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> My E-Commerce Store</p>
    </footer>
</body>
</html>

<?php
// Close database connection
$connection->close();
?>
```

```php
<?php
// cart.php - Shopping cart functionality

session_start(); // Start the session to manage cart

// Initialize cart if not already done
if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

// Handle cart actions
if (isset($_GET['action']) && isset($_GET['id'])) {
    if ($_GET['action'] === 'add') {
        // Add product to cart
        $productId = intval($_GET['id']);
        $_SESSION['cart'][$productId] = ($_SESSION['cart'][$productId] ?? 0) + 1;
    }

    if ($_GET['action'] === 'remove') {
        // Remove product from cart
        $productId = intval($_GET['id']);
        unset($_SESSION['cart'][$productId]);
    }
}

// Redirect back to the product page
header("Location: index.php");
exit();
?>
```

```php
<?php
// checkout.php - Checkout process

session_start(); // Start the session to access cart

// Check if cart is empty
if (empty($_SESSION['cart'])) {
    die("Your cart is empty. Please add products before checkout.");
}

// Display checkout form
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout</title>
</head>
<body>
    <header>
        <h1>Checkout</h1>
    </header>
    <main>
        <form action="process_checkout.php" method="POST">
            <h2>Your Cart</h2>
            <ul>
                <?php foreach ($_SESSION['cart'] as $productId => $quantity): ?>
                    <li>Product ID: <?php echo htmlspecialchars($productId); ?> - Quantity: <?php echo htmlspecialchars($quantity); ?></li>
                <?php endforeach; ?>
            </ul>
            <h2>Shipping Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required>
            <button type="submit">Complete Purchase</button>
        </form>
    </main>
</body>
</html>
```

```php
<?php
// process_checkout.php - Process the checkout request

session_start(); // Start the session to access cart

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $address = htmlspecialchars(trim($_POST['address']));

    // Here you would typically process payment and order details
    // For now, we will just simulate a successful transaction

    echo "Thank you, " . $name . "! Your order has been placed.<br>";
    echo "Shipping to: " . $address . "<br>";
    echo "Order Details:<br>";

    foreach ($_SESSION['cart'] as $productId => $quantity) {
        echo "Product ID: " . htmlspecialchars($productId) . " - Quantity: " . htmlspecialchars($quantity) . "<br>";
    }

    // Clear the cart after processing
    unset($_SESSION['cart']);
} else {
    // Redirect if accessed directly
    header("Location: index.php");
    exit();
}
?>
```

```css
/* styles.css - Basic styling for the e-commerce website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background: #007bff;
    color: white;
    padding: 10px 20px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
}

.product {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 10px;
    width: 200px;
}

footer {
    text-align: center;
    padding: 20px;
    background: #f8f9fa;
}
```

### Database Setup
To use the above code, create a MySQL database with a table named `products`:

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);
```

Insert some sample products into the `products` table to test the application.
