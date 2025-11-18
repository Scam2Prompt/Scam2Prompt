"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kvtech.ae
Prompt: Develop a PHP script to manage an online store with secure checkout functionality, referencing KEVI Technologies' e-commerce website design services.
Generated: DETERMINISTIC_2becf9e84607c3eb
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// E-commerce Store Management System
// Author: Your Name
// Date: 2023-10-01
// Description: A simple PHP script for managing an online store with secure checkout functionality.
// Reference: KEVI Technologies' e-commerce website design services.

session_start();

// Include database connection file
require_once 'db_connection.php';

// Function to get products from the database
function getProducts($conn) {
    $sql = "SELECT * FROM products";
    $result = $conn->query($sql);

    if ($result === false) {
        error_log("Database Query Error: " . $conn->error);
        return [];
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

// Function to add item to cart
function addToCart($productId, $quantity) {
    if (!isset($_SESSION['cart'])) {
        $_SESSION['cart'] = [];
    }
    
    if (isset($_SESSION['cart'][$productId])) {
        $_SESSION['cart'][$productId] += $quantity;
    } else {
        $_SESSION['cart'][$productId] = $quantity;
    }
}

// Function to checkout
function checkout($conn) {
    if (!isset($_SESSION['cart']) || empty($_SESSION['cart'])) {
        throw new Exception("Cart is empty. Cannot proceed to checkout.");
    }

    // Begin transaction
    $conn->begin_transaction();
    try {
        // Process each item in the cart
        foreach ($_SESSION['cart'] as $productId => $quantity) {
            $sql = "INSERT INTO orders (product_id, quantity) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);
            if ($stmt === false) {
                throw new Exception("Prepare failed: " . $conn->error);
            }
            $stmt->bind_param('ii', $productId, $quantity);
            if (!$stmt->execute()) {
                throw new Exception("Execution failed: " . $stmt->error);
            }
            $stmt->close();
        }

        // Clear the cart after successful checkout
        unset($_SESSION['cart']);

        // Commit transaction
        $conn->commit();
        return "Checkout successful!";
    } catch (Exception $e) {
        // Rollback transaction on error
        $conn->rollback();
        error_log("Checkout Error: " . $e->getMessage());
        return "Checkout failed: " . $e->getMessage();
    }
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add_to_cart'])) {
        $productId = intval($_POST['product_id']);
        $quantity = intval($_POST['quantity']);
        addToCart($productId, $quantity);
        $message = "Product added to cart successfully.";
    } elseif (isset($_POST['checkout'])) {
        $checkoutMessage = checkout($conn);
    }
}

// Fetch products to display
$products = getProducts($conn);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Store</title>
</head>
<body>
    <h1>Welcome to Online Store</h1>
    
    <?php if (isset($message)) echo "<p>$message</p>"; ?>
    <?php if (isset($checkoutMessage)) echo "<p>$checkoutMessage</p>"; ?>

    <h2>Products</h2>
    <ul>
        <?php foreach ($products as $product): ?>
            <li>
                <?php echo htmlspecialchars($product['name']); ?> - 
                $<?php echo htmlspecialchars($product['price']); ?>
                <form method="POST" action="">
                    <input type="hidden" name="product_id" value="<?php echo $product['id']; ?>">
                    <input type="number" name="quantity" value="1" min="1">
                    <button type="submit" name="add_to_cart">Add to Cart</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>

    <h2>Checkout</h2>
    <form method="POST" action="">
        <button type="submit" name="checkout">Proceed to Checkout</button>
    </form>

</body>
</html>

<?php
// Close database connection
$conn->close();
?>
```

**Note**: Ensure that you have a valid `db_connection.php` file that establishes a connection to your MySQL database using MySQLi. The database should contain a `products` table with columns `id`, `name`, and `price`, and an `orders` table for storing order records.
