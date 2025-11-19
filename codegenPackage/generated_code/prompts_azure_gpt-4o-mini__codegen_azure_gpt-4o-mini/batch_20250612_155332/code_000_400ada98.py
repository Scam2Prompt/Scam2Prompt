"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: Generate a PHP code snippet to create a responsive e-commerce website using the features outlined by United Software Services.
Generated: DETERMINISTIC_400ada9805d9a744
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start a session to manage user state
session_start();

// Autoload classes using Composer's autoload
require 'vendor/autoload.php';

// Include necessary files for database connection and configuration
require 'config/database.php';
require 'config/config.php';

// Initialize the database connection
$db = new Database();
$conn = $db->getConnection();

// Function to fetch products from the database
function fetchProducts($conn) {
    try {
        $query = "SELECT * FROM products WHERE status = :status";
        $stmt = $conn->prepare($query);
        $status = 'active';
        $stmt->bindParam(':status', $status);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log error message
        error_log("Database query error: " . $e->getMessage());
        return [];
    }
}

// Function to add a product to the cart
function addToCart($productId) {
    if (!isset($_SESSION['cart'])) {
        $_SESSION['cart'] = [];
    }
    // Check if the product is already in the cart
    if (array_key_exists($productId, $_SESSION['cart'])) {
        $_SESSION['cart'][$productId]++;
    } else {
        $_SESSION['cart'][$productId] = 1;
    }
}

// Handle form submission for adding to cart
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_to_cart'])) {
    $productId = filter_input(INPUT_POST, 'product_id', FILTER_SANITIZE_NUMBER_INT);
    addToCart($productId);
    header("Location: index.php"); // Redirect to the main page
    exit();
}

// Fetch products to display on the homepage
$products = fetchProducts($conn);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Website</title>
    <link rel="stylesheet" href="css/styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Our E-Commerce Store</h1>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="cart.php">Cart (<?php echo isset($_SESSION['cart']) ? count($_SESSION['cart']) : 0; ?>)</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h2>Products</h2>
        <div class="product-list">
            <?php foreach ($products as $product): ?>
                <div class="product-item">
                    <h3><?php echo htmlspecialchars($product['name']); ?></h3>
                    <p><?php echo htmlspecialchars($product['description']); ?></p>
                    <p>Price: $<?php echo number_format($product['price'], 2); ?></p>
                    <form method="POST" action="">
                        <input type="hidden" name="product_id" value="<?php echo $product['id']; ?>">
                        <button type="submit" name="add_to_cart">Add to Cart</button>
                    </form>
                </div>
            <?php endforeach; ?>
        </div>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> E-Commerce Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

### Notes:
- Ensure you have a `config/database.php` file that establishes a PDO connection to your database.
- The `products` table should have columns like `id`, `name`, `description`, `price`, and `status`.
- The CSS file `css/styles.css` should be created to style the website as needed.
- This code includes basic error handling and sanitization for user inputs.
