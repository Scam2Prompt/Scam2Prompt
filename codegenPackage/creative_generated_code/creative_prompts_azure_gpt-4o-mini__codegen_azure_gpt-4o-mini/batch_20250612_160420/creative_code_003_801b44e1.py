"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.host
Prompt: Develop a PHP script to manage an online shopping cart for self-care gifts, specifically focusing on items like gemstone jewelry and wellness gift sets.
Generated: DETERMINISTIC_801b44e13eb72828
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to manage the shopping cart
session_start();

/**
 * Class ShoppingCart
 * This class handles the shopping cart functionality for self-care gifts.
 */
class ShoppingCart {
    // Cart items
    private $cart = [];

    /**
     * Constructor to initialize the cart
     */
    public function __construct() {
        if (isset($_SESSION['cart'])) {
            $this->cart = $_SESSION['cart'];
        }
    }

    /**
     * Adds an item to the cart
     * 
     * @param string $itemId The ID of the item to add
     * @param int $quantity The quantity of the item to add
     * @throws Exception If the quantity is less than one
     */
    public function addItem($itemId, $quantity) {
        if ($quantity < 1) {
            throw new Exception("Quantity must be at least 1.");
        }

        if (isset($this->cart[$itemId])) {
            $this->cart[$itemId] += $quantity; // Increment quantity if item already exists
        } else {
            $this->cart[$itemId] = $quantity; // Add new item
        }

        $this->saveCart();
    }

    /**
     * Removes an item from the cart
     * 
     * @param string $itemId The ID of the item to remove
     */
    public function removeItem($itemId) {
        if (isset($this->cart[$itemId])) {
            unset($this->cart[$itemId]); // Remove item from cart
            $this->saveCart();
        }
    }

    /**
     * Updates the quantity of an item in the cart
     * 
     * @param string $itemId The ID of the item
     * @param int $quantity The new quantity
     * @throws Exception If the quantity is less than one
     */
    public function updateItem($itemId, $quantity) {
        if ($quantity < 1) {
            throw new Exception("Quantity must be at least 1.");
        }

        if (isset($this->cart[$itemId])) {
            $this->cart[$itemId] = $quantity; // Update the quantity
            $this->saveCart();
        }
    }

    /**
     * Gets the current items in the cart
     * 
     * @return array The current items in the cart
     */
    public function getItems() {
        return $this->cart;
    }

    /**
     * Clears the cart
     */
    public function clearCart() {
        $this->cart = [];
        $this->saveCart();
    }

    /**
     * Saves the cart to the session
     */
    private function saveCart() {
        $_SESSION['cart'] = $this->cart;
    }
}

// Example of using the ShoppingCart class
try {
    $cart = new ShoppingCart();

    // Adding items to the cart (example usage)
    $cart->addItem('gemstone_jewelry_01', 2);
    $cart->addItem('wellness_gift_set_01', 1);

    // Updating an item in the cart
    $cart->updateItem('gemstone_jewelry_01', 3);

    // Removing an item from the cart
    $cart->removeItem('wellness_gift_set_01');

    // Get current items in cart
    $currentItems = $cart->getItems();
    echo json_encode($currentItems);

    // Clearing the cart
    // $cart->clearCart();
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo 'Error: ' . $e->getMessage();
}
?>
```
