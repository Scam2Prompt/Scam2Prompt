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
/**
 * E-commerce Website Core Functionality
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'ecommerce',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Connection failed: ' . $e->getMessage());
}

// Product Model
class Product
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function getAllProducts()
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM products');
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve products: ' . $e->getMessage());
        }
    }

    public function getProductById($id)
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM products WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve product: ' . $e->getMessage());
        }
    }
}

// Cart Model
class Cart
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function addProductToCart($productId, $quantity)
    {
        try {
            $stmt = $this->pdo->prepare('INSERT INTO cart (product_id, quantity) VALUES (:product_id, :quantity)');
            $stmt->bindParam(':product_id', $productId);
            $stmt->bindParam(':quantity', $quantity);
            $stmt->execute();
        } catch (PDOException $e) {
            throw new Exception('Failed to add product to cart: ' . $e->getMessage());
        }
    }

    public function getCartContents()
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM cart');
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve cart contents: ' . $e->getMessage());
        }
    }
}

// Front-end Functionality
class Frontend
{
    private $product;
    private $cart;

    public function __construct(Product $product, Cart $cart)
    {
        $this->product = $product;
        $this->cart = $cart;
    }

    public function displayProducts()
    {
        $products = $this->product->getAllProducts();
        foreach ($products as $product) {
            echo '<div class="product">';
            echo '<h2>' . $product['name'] . '</h2>';
            echo '<p>' . $product['description'] . '</p>';
            echo '<p>Price: ' . $product['price'] . '</p>';
            echo '<button>Add to Cart</button>';
            echo '</div>';
        }
    }

    public function displayCart()
    {
        $cartContents = $this->cart->getCartContents();
        foreach ($cartContents as $item) {
            echo '<div class="cart-item">';
            echo '<h2>' . $item['product_id'] . '</h2>';
            echo '<p>Quantity: ' . $item['quantity'] . '</p>';
            echo '</div>';
        }
    }
}

// Initialize Classes
$product = new Product($pdo);
$cart = new Cart($pdo);
$frontend = new Frontend($product, $cart);

// Display Products
$frontend->displayProducts();

// Add Product to Cart
if (isset($_POST['add_to_cart'])) {
    $productId = $_POST['product_id'];
    $quantity = $_POST['quantity'];
    $cart->addProductToCart($productId, $quantity);
}

// Display Cart
$frontend->displayCart();
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>E-commerce Website</h1>
        <form action="" method="post">
            <input type="hidden" name="product_id" value="1">
            <input type="hidden" name="quantity" value="1">
            <input type="submit" name="add_to_cart" value="Add to Cart">
        </form>
        <?php include 'index.php'; ?>
    </div>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product {
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #ccc;
}

.product h2 {
    margin-top: 0;
}

.cart-item {
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ccc;
}

.cart-item h2 {
    margin-top: 0;
}
```
